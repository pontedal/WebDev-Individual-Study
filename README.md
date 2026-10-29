Game Review Application – Flask Prototype

Description

This project is a small web application developed using Flask as part of an individual study comparing Flask with ASP.NET Core MVC.

The application is based on the Review entity from lab2 involving a game review website. Its purpose is to demonstrate how basic CRUD functionality can be implemented using Flask and compared with an equivalent implementation in ASP.NET Core MVC.

The application uses a local SQLite database for persistent storage.

Features

The application supports the following operations:

Create a new game review.

View all existing reviews.

View the details of an individual review.

Edit an existing review.

Delete a review.

Validate submitted review data.

Each review contains a game name, title, body, rating and author.

Technologies

Python

Flask

Flask-SQLAlchemy

SQLite

Jinja2 templates

HTML

Installation

Python must be installed before running the application.

1. Create a virtual environment:

python -m venv .venv

2. Activate the virtual environment:

Windows (PowerShell):

.venv\Scripts\Activate.ps1

macOS/Linux:

source .venv/bin/activate

3. Install the required packages:

pip install -r requirements.txt

Database Setup

The application uses a local SQLite database.

If the database has not already been created, open a Python terminal in the project directory and run:

from app import app, db

with app.app_context():
    db.create_all()

This creates the database tables defined by the application's SQLAlchemy models.

Note that db.create_all() creates missing tables but does not update existing table structures. Database migrations were not implemented because the prototype has a limited scope.

Running the Application

Start the application from the project directory using:

flask run --debug

Then open the given address in a web browser, which will most likely be http://127.0.0.1:5000/

Project Structure

The main application logic, routes and database model are defined in app.py.

HTML templates are stored in the templates directory. The application uses Jinja template inheritance, where base.html defines the shared page structure and other templates extend it.

The SQLite database is stored locally in the application's instance directory.

Scope and Limitations

This application was developed as a small standalone prototype rather than a complete production-ready website.

The implementation focuses on CRUD operations for a single entity. Compared with the original ASP.NET Core MVC laboratory assignment, the data model has been simplified by representing the game name as a string rather than a separate Game entity.

Authentication, user accounts, cloud deployment, database migrations and additional production security features are outside the scope of this prototype.

Purpose

The project serves as a practical implementation for comparing Flask and ASP.NET Core MVC, particularly regarding application architecture, routing, templates, database integration, form handling and developer experience.