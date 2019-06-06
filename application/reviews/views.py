from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application import app, db
from application.reviews.models import Review
from application.movies.models import Movie
from application.reviews.forms import ReviewForm

@app.route("/reviews/new/<movie_id>", methods=["GET"])
@login_required
def reviews_form(movie_id):
    return render_template("reviews/new.html", form = ReviewForm(), movie = Movie.query.get(movie_id))

@app.route("/reviews/new/<movie_id>", methods=["POST"])
@login_required
def reviews_create(movie_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form = form, movie = Movie.query.get(movie_id))
    
    r = Review(form.reviewtext.data, form.rating.data)
    r.account_id = current_user.id
    r.movie_id = movie_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("movies_index"))

@app.route("/reviews/list/<movie_id>")
def reviews_for_movie(movie_id):
    r = Review.query.filter_by(movie_id = movie_id).all()
    return render_template("reviews/list.html", reviews = r, movie = Movie.query.get(movie_id))