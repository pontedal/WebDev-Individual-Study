from flask import Flask, abort, render_template

app = Flask(__name__)

reviews = [
    {"id": 1, "game": "Hades", "title": "Great loop", "rating": 9, "author": "Anna"},
    {"id": 2, "game": "Hollow Knight", "title": "Beautiful but hard", "rating": 8, "author": "Anna"},
    {"id": 3, "game": "Stardew Valley", "title": "Cozy", "rating": 10, "author": "Anna"},
]

@app.route("/")
def index():
    return render_template("index.html", reviews=reviews)

@app.route("/reviews/<int:review_id>")
def details(review_id):
    for r in reviews:
        if r["id"]==review_id:
            return render_template("details.html", review=r)
    abort(404)