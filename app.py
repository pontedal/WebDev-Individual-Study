from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"

db = SQLAlchemy(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    author=db.Column(db.String(60), nullable=False)

def validate_review(form):
    errors = {}
    game = form.get("game", "").strip()
    title = form.get("title", "").strip()
    author = form.get("author", "").strip()
    body = form.get("body", "").strip()
    rating_text = form.get("rating", "").strip()

    if not game:
        errors["game"] = "Game is required."
    elif len(game) > 100:
        errors["game"] = "Game must be at most 100 characters."
    if not title:
        errors["title"] = "Title is required."
    elif len(title) > 150:
        errors["title"] = "Title must be at most 150 characters."
    if not author:
        errors["author"] = "Author is required."
    elif len(author) > 60:
        errors["author"] = "Author must be at most 60 characters."
    if not body:
        errors["body"] = "Review text is required."
    elif len(body) > 500:
        errors["body"] = "Review text must be at most 500 characters."
    rating = None
    try:
        rating = int(rating_text)
    except ValueError:
        errors["rating"] = "Rating must be a whole number."
    else:
        if not 1 <= rating <= 10:
            errors["rating"] = "Rating must be between 1 and 10."

    data = {"game": game, "title": title, "author": author, "body": body, "rating": rating}
    return errors, data

@app.route("/")
def index():
    reviews = Review.query.all()
    return render_template("index.html", reviews=reviews)

@app.route("/reviews/<int:review_id>")
def details(review_id):
    review=db.get_or_404(Review, review_id)
    return render_template("details.html", review=review)

@app.route("/reviews/new", methods=["GET", "POST"])
def create():
    errors = {}
    form = {}
    if request.method == "POST":
        form = request.form
        errors, data = validate_review(form)
        if not errors:
            review = Review(**data)
            db.session.add(review)
            db.session.commit()
            return redirect(url_for("details", review_id=review.id))

    return render_template("create.html", errors=errors, form=form)

@app.route("/reviews/<int:review_id>/edit", methods=["GET", "POST"])
def edit(review_id):
    review = db.get_or_404(Review, review_id)
    errors = {}
    form = {
        "game": review.game, "title": review.title, "author": review.author,
        "rating": review.rating, "body": review.body,
    }
    if request.method == "POST":
        form = request.form
        errors, data = validate_review(form)
        if not errors:
            review.game = data["game"]
            review.title = data["title"]
            review.author = data["author"]
            review.body = data["body"]
            review.rating = data["rating"]
            db.session.commit()
            return redirect(url_for("details", review_id=review.id))
    return render_template("edit.html", review=review, errors=errors, form=form)

@app.route("/reviews/<int:review_id>/delete", methods=["POST"])
def delete_review(review_id):
    review = db.get_or_404(Review, review_id)

    db.session.delete(review)
    db.session.commit()

    return redirect(url_for("index"))