from application import app, db
from flask import render_template, request, url_for, redirect
from application.movies.models import Movie

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
def movies_form():
    return render_template("movies/new.html")

@app.route("/movies/<movie_id>")
def movies_edit_form(movie_id):
    return render_template("movies/edit.html", movie = Movie.query.get(movie_id))

@app.route("/movies/edit/<movie_id>", methods=["POST"])
def movies_edit_entry(movie_id):
    m = Movie.query.get(movie_id)
    m.name = request.form.get("name")
    m.description = request.form.get("description")

    db.session().commit()

    return redirect(url_for("movies_index"))

@app.route("/movies/", methods=["POST"])
def movies_create():
    print(request.form.get("name"))
    
    m = Movie(request.form.get("name"), request.form.get("description"))

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("movies_index"))