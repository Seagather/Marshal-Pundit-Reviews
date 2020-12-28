import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": request.form.get("password")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
        
    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        star_rating = "on" if request.form.getlist("star_rating") else "off"
        review = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "book_review": request.form.get("book_review"),
            "star_rating": star_rating,
            "published_date": request.form.get("published_date"),
            "url_link": request.form.get("url_link"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Book Successfully Added")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("add_review.html", genres=genres)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):

    if request.method == "POST":
        star_rating = "on" if request.form.getlist("star_rating") else "off"
        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "book_review": request.form.get("book_review"),
            "star_rating": star_rating,
            "published_date": request.form.get("published_date"),
            "url_link": request.form.get("url_link"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genres=genres)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            