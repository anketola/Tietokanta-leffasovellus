from flask import render_template, request, url_for, redirect
from flask_login import login_required

from application import app, db
from application.movies.models import Movie
from application.movies.forms import MovieForm, EditMovieForm

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
@login_required
def movies_form():
    return render_template("movies/new.html", form = MovieForm())

@app.route("/movies/<movie_id>")
@login_required
def movies_edit_form(movie_id):
    
    m = Movie.query.get(movie_id)

    form = EditMovieForm(name = m.name, released = m.released, description = m.description)

    return render_template("movies/edit.html", form = form, movie = m)

@app.route("/movies/edit/<movie_id>", methods=["POST"])
@login_required
def movies_edit_entry(movie_id):
    form = EditMovieForm(request.form)

    if not form.validate():
        return render_template("movies/edit.html", form = form, movie = Movie.query.get(movie_id))

    m = Movie.query.get(movie_id)
    m.name = form.name.data
    m.released = form.released.data
    m.description = form.description.data

    db.session().commit()

    return redirect(url_for("movies_index"))

@app.route("/movies/", methods=["POST"])
@login_required
def movies_create():
    form = MovieForm(request.form)
    
    if not form.validate():
        return render_template("movies/new.html", form = form)

    m = Movie(form.name.data, form.released.data, form.description.data)

    db.session().add(m)
    db.session().commit()

    return redirect(url_for("movies_index"))

@app.route("/movies/delete/<movie_id>", methods=["POST"])
@login_required
def movies_delete(movie_id):
    m = Movie.query.get(movie_id)

    db.session().delete(m)
    db.session().commit()

    return redirect(url_for("movies_index"))