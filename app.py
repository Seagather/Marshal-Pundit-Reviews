# import os
# from flask import (
#     Flask, flash, render_template,
#     redirect, request, session, url_for)
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, check_password_hash
# if os.path.exists("env.py"):
#     import env


# app = Flask(__name__)

# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# app.secret_key = os.environ.get("SECRET_KEY")

# mongo = PyMongo(app)


# @app.route("/")
# @app.route("/get_reviews")
# def get_reviews():
#     reviews = list(mongo.db.reviews.find())
#     return render_template("reviews.html", reviews=reviews)


# @app.route("/search", methods=["GET", "POST"])
# def search():
#     query = request.form.get("query")
#     reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
#     return render_template("reviews.html", reviews=reviews)


# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         # check if username already exists in db
#         existing_user = mongo.db.users.find_one(
#             {"username": request.form.get("username").lower()})

#         if existing_user:
#             flash("Username already exists")
#             return redirect(url_for("register"))

#         register = {
#             "username": request.form.get("username").lower(),
#             "password": generate_password_hash(request.form.get("password"))
#         }
#         mongo.db.users.insert_one(register)

#         # put the new user into 'session' cookie
#         session["user"] = request.form.get("username").lower()
#         flash("Registration Successful!")
#         return redirect(url_for("profile", username=session["user"]))
        
#     return render_template("register.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         # check if username exists in db
#         existing_user = mongo.db.users.find_one(
#             {"username": request.form.get("username").lower()})

#         if existing_user:
#             # ensure hashed password matches user input
#             if check_password_hash(
#                     existing_user["password"], request.form.get("password")):
#                         session["user"] = request.form.get("username").lower()
#                         flash("Welcome, {}".format(
#                             request.form.get("username")))
#                         return redirect(url_for(
#                             "profile", username=session["user"]))
#             else:
#                 # invalid password match
#                 flash("Incorrect Username and/or Password")
#                 return redirect(url_for("login"))

#         else:
#             # username doesn't exist
#             flash("Incorrect Username and/or Password")
#             return redirect(url_for("login"))

#     return render_template("login.html")


# @app.route("/profile/<username>", methods=["GET", "POST"])
# def profile(username):
#     # grab the session user's username from db
#     username = mongo.db.users.find_one(
#         {"username": session["user"]})["username"]

#     if session["user"]:
#         return render_template("profile.html", username=username)

#     return redirect(url_for("login"))
    

# @app.route("/logout")
# def logout():
#     # remove user from session cookie
#     flash("You have been logged out")
#     session.pop("user")
#     return redirect(url_for("login"))


# @app.route("/add_review", methods=["GET", "POST"])
# def add_review():
#     if request.method == "POST":
#         star_rating = "on" if request.form.get("star_rating") else "off"
#         star_rating2 = "on" if request.form.get("star_rating2") else "off"
#         star_rating3 = "on" if request.form.get("star_rating3") else "off"
#         star_rating4 = "on" if request.form.get("star_rating4") else "off"
#         star_rating5 = "on" if request.form.get("star_rating5") else "off"
#         review = {
#             "genre_name": request.form.get("genre_name"),
#             "book_name": request.form.get("book_name"),
#             "author_name": request.form.get("author_name"),
#             "book_review": request.form.get("book_review"),
#             "star_rating": star_rating,
#             "star_rating2": star_rating2,
#             "star_rating3": star_rating3,
#             "star_rating4": star_rating4,
#             "star_rating5": star_rating5,
#             "published_date": request.form.get("published_date"),
#             "url_link": request.form.get("url_link"),
#             "created_by": session["user"]
#         }
#         mongo.db.reviews.insert_one(review)
#         flash("Book Successfully Added")
#         return redirect(url_for("get_reviews"))

#     genres = mongo.db.genres.find().sort("genre_name", 1)
#     return render_template("add_review.html", genres=genres)


# @app.route("/edit_review/<review_id>", methods=["GET", "POST"])
# def edit_review(review_id):

#     if request.method == "POST":
#         star_rating = "on" if request.form.get("star_rating") else "off"
#         star_rating2 = "on" if request.form.get("star_rating2") else "off"
#         star_rating3 = "on" if request.form.get("star_rating3") else "off"
#         star_rating4 = "on" if request.form.get("star_rating4") else "off"
#         star_rating5 = "on" if request.form.get("star_rating5") else "off"
#         submit = {
#             "genre_name": request.form.get("genre_name"),
#             "book_name": request.form.get("book_name"),
#             "author_name": request.form.get("author_name"),
#             "book_review": request.form.get("book_review"),
#             "star_rating": star_rating,
#             "star_rating2": star_rating2,
#             "star_rating3": star_rating3,
#             "star_rating4": star_rating4,
#             "star_rating5": star_rating5,
#             "published_date": request.form.get("published_date"),
#             "url_link": request.form.get("url_link"),
#             "created_by": session["user"]
#         }
#         mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
#         flash("Review Successfully Updated")

#     review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
#     genres = mongo.db.genres.find().sort("genre_name", 1)
#     return render_template("edit_review.html", review=review, genres=genres)


# @app.route("/delete_review/<review_id>")
# def delete_review(review_id):
#     mongo.db.reviews.remove({"_id": ObjectId(review_id)})
#     flash("Review Successfully Deleted")
#     return redirect(url_for("get_reviews"))


# @app.route("/get_genres")
# def get_genres():
#     genres = list(mongo.db.genres.find().sort("genre_name", 1))
#     return render_template("genres.html", genres=genres)


# @app.route("/add_genre", methods=["GET", "POST"])
# def add_genre():
#     if request.method == "POST":
#         genre = {
#             "genre_name": request.form.get("genre_name")
#         }
#         mongo.db.genres.insert_one(genre)
#         flash("New Genre Added")
#         return redirect(url_for("get_genres"))

#     return render_template("add_genre.html")


# @app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
# def edit_genre(genre_id):
#     if request.method == "POST":
#         submit = {
#             "genre_name": request.form.get("genre_name")
#         }
#         mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
#         flash("Genres Successfully Updated")
#         return redirect(url_for("get_genres"))

#     genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
#     return render_template("edit_genre.html", genre=genre)


# @app.route("/delete_genre/<genre_id>")
# def delete_genre(genre_id):
#     mongo.db.genres.remove({"_id": ObjectId(genre_id)})
#     flash("Genre Successfully Deleted")
#     return redirect(url_for("get_genres"))


# if __name__ == "__main__":
#     app.run(host=os.environ.get("IP"),
#             port=int(os.environ.get("PORT")),
#             debug=False)
            

import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# login_manager.init_app(app)
mongo = PyMongo(app)


@app.route("/")
# @login_required
def home():
    # if session["user"]:
    if not session.get("user") is None:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("login"))


@app.route("/get_reviews")
# @login_required
def get_reviews():
    # if session["user"]:
    if not session.get("user") is None:
        reviews = list(mongo.db.reviews.find())
        return render_template("reviews.html", reviews=reviews)

    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form.get("username").lower())
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
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

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        star_rating = "on" if request.form.get("star_rating") else "off"
        star_rating2 = "on" if request.form.get("star_rating2") else "off"
        star_rating3 = "on" if request.form.get("star_rating3") else "off"
        star_rating4 = "on" if request.form.get("star_rating4") else "off"
        star_rating5 = "on" if request.form.get("star_rating5") else "off"
        #  create amazon link
        name = request.form.get("book_name")
        name_array = name.split(" ")
        k = ''  # k is the search query
        for obj in name_array:
            # if item in name array is not empty add to k
            if obj != ' ':
                if k == '':   # if k is empty done add '+'
                    k = k + obj
                else:
                    k = k + "+" + obj

        amazon_link = "https://www.amazon.com/s?tag=patrickfaketag384909&k=" + k

        review = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "book_review": request.form.get("book_review"),
            "star_rating": star_rating,
            "star_rating2": star_rating2,
            "star_rating3": star_rating3,
            "star_rating4": star_rating4,
            "star_rating5": star_rating5,
            "published_date": request.form.get("published_date"),
            "url_link": request.form.get("url_link"),
            "amazon_link": amazon_link,
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
        star_rating = "on" if request.form.get("star_rating") else "off"
        star_rating2 = "on" if request.form.get("star_rating2") else "off"
        star_rating3 = "on" if request.form.get("star_rating3") else "off"
        star_rating4 = "on" if request.form.get("star_rating4") else "off"
        star_rating5 = "on" if request.form.get("star_rating5") else "off"
        #  create amazon link
        name = request.form.get("book_name")
        name_array = name.split(" ")
        k = ''  # k is the search query
        for obj in name_array:
            # if item in name array is not empty add to k
            if obj != ' ':
                if k == '':   # if k is empty done add '+'
                    k = k + obj
                else:
                    k = k + "+" + obj

        amazon_link = "https://www.amazon.com/s?tag=patrickfaketag384909&k=" + k

        submit = {
            "genre_name": request.form.get("genre_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "book_review": request.form.get("book_review"),
            "star_rating": star_rating,
            "star_rating2": star_rating2,
            "star_rating3": star_rating3,
            "star_rating4": star_rating4,
            "star_rating5": star_rating5,
            "published_date": request.form.get("published_date"),
            "url_link": request.form.get("url_link"),
            "amazon_link": amazon_link,
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("edit_review.html", review=review, genres=genres)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_reviews"))


@app.route("/get_genres")
def get_genres():
    genres = list(mongo.db.genres.find().sort("genre_name", 1))
    return render_template("genres.html", genres=genres)


@app.route("/add_genre", methods=["GET", "POST"])
def add_genre():
    if request.method == "POST":
        genre = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.insert_one(genre)
        flash("New Genre Added")
        return redirect(url_for("get_genres"))

    return render_template("add_genre.html")


@app.route("/edit_genre/<genre_id>", methods=["GET", "POST"])
def edit_genre(genre_id):
    if request.method == "POST":
        submit = {
            "genre_name": request.form.get("genre_name")
        }
        mongo.db.genres.update({"_id": ObjectId(genre_id)}, submit)
        flash("Genres Successfully Updated")
        return redirect(url_for("get_genres"))

    genre = mongo.db.genres.find_one({"_id": ObjectId(genre_id)})
    return render_template("edit_genre.html", genre=genre)


@app.route("/delete_genre/<genre_id>")
def delete_genre(genre_id):
    mongo.db.genres.remove({"_id": ObjectId(genre_id)})
    flash("Genre Successfully Deleted")
    return redirect(url_for("get_genres"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

    # app.run(host="localhost",
    #         port=4000,
    #         debug=True)
