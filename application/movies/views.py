from flask import render_template, request, url_for, redirect

from application import app, db
from application.movies.models import Movie
from application.movies.forms import MovieForm

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
def movies_form():
    return render_template("movies/new.html", form = MovieForm())

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
    form = MovieForm(request.form)
    
    if not form.validate():
        return render_template("movies/new.html", form = form)

    m = Movie(form.name.data, form.description.data)

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("movies_index"))