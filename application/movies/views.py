from flask import render_template, request, url_for, redirect

from application import app, db, login_required
from application.movies.models import Movie
from application.movies.forms import MovieForm, EditMovieForm
from application.category.models import Category
from application.category.forms import CategoryViewForm

# Returns as a response list of all movies and a form for selecting a category
@app.route("/movies", methods=["GET"])
def movies_index():
    form = CategoryViewForm()

    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]

    return render_template("movies/list.html", form = form, movies = Movie.query.all())

# Returns as a response information on one movie
@app.route("/movies/view/<movie_id>", methods=["GET"])
def movies_view(movie_id):
    m = Movie.query.get(movie_id)
    return render_template("movies/view.html", movie = m, r_count = Movie.review_count_for_movie(movie_id), r_avg = Movie.average_rating_for_movie(movie_id))

# Responses to a form post-requst by user for best movies in a certain category, redirects to the relevant category view
@app.route("/movies/view/category/", methods=["POST"])
def movies_for_category_request():
    form = CategoryViewForm(request.form)
    
    # Fills the choices based on database entries in Category
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]

    if not form.validate():
        return render_template("movies/list.html", form = form, movies = Movie.query.all())
    
    return redirect(url_for("movies_for_category_view", category_id = form.category.data))

# Returns a view of movies in certain category based on best ratings
@app.route("/movies/view/category/<category_id>", methods=["GET"])
def movies_for_category_view(category_id):
    return render_template("movies/viewcategory.html", movies=Movie.movies_category_best(category_id))

# Method for adding a new movie, restricted to admin
@app.route("/movies/new/", methods=["GET"])
@login_required(role="ADMIN")
def movies_form():
    form = MovieForm()
    
    # Fills the choices based on database entries in Category
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]
    
    return render_template("movies/new.html", form = form)

# Returns the view and form for editing a movie, restricted to admin
@app.route("/movies/edit/<movie_id>", methods=["GET"])
@login_required(role="ADMIN")
def movies_edit_form(movie_id):
    
    m = Movie.query.get(movie_id)

    form = EditMovieForm(name = m.name, released = m.released, description = m.description)
    
    # Fills the choices based on database entries in Category
    categories = Category.query.all()
    form.category.choices = [(categorychoice.id, categorychoice.name) for categorychoice in categories]
    
    return render_template("movies/edit.html", form = form, movie = m)

# Method for post request to edit a movie entry, restricted to admin
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

# Method for post request to add a new movie, restricted to admin
@app.route("/movies/new", methods=["POST"])
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

# Method for post request to delete a movie entry, restricted to admin
@app.route("/movies/delete/<movie_id>", methods=["POST"])
@login_required(role="ADMIN")
def movies_delete(movie_id):
    m = Movie.query.get(movie_id)

    m.categories.clear()

    db.session().delete(m)
    db.session().commit()

    return redirect(url_for("movies_index"))