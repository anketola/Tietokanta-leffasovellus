from flask import render_template, request, url_for, redirect

from application import app, db, login_required
from application.movies.models import Movie
from application.movies.forms import MovieForm, EditMovieForm
from application.category.models import Category

@app.route("/movies", methods=["GET"])
def movies_index():
    return render_template("movies/list.html", movies = Movie.query.all())

@app.route("/movies/new/")
@login_required(role="ADMIN")
def movies_form():
    form = MovieForm()
    
    # Fills the choices based on database entries in Category
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]
    
    return render_template("movies/new.html", form = form)

@app.route("/movies/<movie_id>")
@login_required(role="ADMIN")
def movies_edit_form(movie_id):
    
    m = Movie.query.get(movie_id)

    form = EditMovieForm(name = m.name, released = m.released, description = m.description)
    
    # Fills the choices based on database entries in Category
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]
    
    return render_template("movies/edit.html", form = form, movie = m)

@app.route("/movies/edit/<movie_id>", methods=["POST"])
@login_required(role="ADMIN")
def movies_edit_entry(movie_id):
    form = EditMovieForm(request.form)

    # Fills the choices list to prevent validation error
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]

    if not form.validate():
        return render_template("movies/edit.html", form = form, movie = Movie.query.get(movie_id))

    categories = form.category.data
    m = Movie.query.get(movie_id)
    m.name = form.name.data
    m.released = form.released.data
    m.description = form.description.data
    m.categories.clear()

    for id in categories:
        category = Category.query.get(id)
        m.categories.append(category)
    
    db.session.commit()

    return redirect(url_for("movies_index"))

@app.route("/movies/", methods=["POST"])
@login_required(role="ADMIN")
def movies_create():
    form = MovieForm(request.form)
    
    # Fills the choices list to prevent validation error
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]

    if not form.validate():
        return render_template("movies/new.html", form = form)

    m = Movie(form.name.data, form.released.data, form.description.data)
    categories = form.category.data
    
    db.session().add(m)
    db.session().commit()

    db.session().refresh(m)

    for id in categories:
        category = Category.query.get(id)
        m.categories.append(category)
        db.session.commit()

    return redirect(url_for("movies_index"))

@app.route("/movies/delete/<movie_id>", methods=["POST"])
@login_required(role="ADMIN")
def movies_delete(movie_id):
    m = Movie.query.get(movie_id)

    m.categories.clear()

    db.session().delete(m)
    db.session().commit()


    return redirect(url_for("movies_index"))