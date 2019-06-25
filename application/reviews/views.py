from flask import render_template, request, url_for, redirect
from flask_login import current_user

from application import app, db, login_required
from application.reviews.models import Review
from application.movies.models import Movie
from application.reviews.forms import ReviewForm, EditReviewForm

# Returns the view and form for adding a review, access restricted to user status
@app.route("/reviews/new/<movie_id>", methods=["GET"])
@login_required(role="USER")
def reviews_form(movie_id):
    return render_template("reviews/new.html", form = ReviewForm(), movie = Movie.query.get(movie_id))

# Method for post request to add a new review, access restricted to user status
@app.route("/reviews/new/<movie_id>", methods=["POST"])
@login_required(role="USER")
def reviews_create(movie_id):
    form = ReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/new.html", form = form, movie = Movie.query.get(movie_id))
    
    r = Review(form.reviewtext.data, form.rating.data)
    r.account_id = current_user.id
    r.movie_id = movie_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("reviews_for_movie", movie_id = movie_id))

# Returns the view for all reviews for a certain movie
@app.route("/reviews/list/<movie_id>", methods=["GET"])
def reviews_for_movie(movie_id):
    r = Review.query.filter_by(movie_id = movie_id).all()
    return render_template("reviews/list.html", reviews = r, movie = Movie.query.get(movie_id))

# Returns the view for a particular review
@app.route("/reviews/view/<movie_id>/<review_id>", methods=["GET"])
def reviews_view(movie_id, review_id):
    m = Movie.query.get(movie_id)
    r = Review.query.get(review_id)
    return render_template("reviews/view.html", review = r, movie = m, r_count = Movie.review_count_for_movie(movie_id))

# Method for post request to delete a review, access restricted to user status (note that admin has it too)
@app.route("/reviews/delete/<movie_id>/<review_id>", methods=["POST"])
@login_required(role="USER")
def reviews_delete(movie_id, review_id):
    r = Review.query.get(review_id)

    # Checks if the current user posted the review or the user is logged on admin account
    if r.account_id != current_user.id or current_user.admin == False:
        redirect(url_for("index"))

    db.session().delete(r)
    db.session().commit()

    return redirect(url_for("reviews_for_movie", movie_id = movie_id))

# Returns the view and form to edit a review, access restricted to user status (note that admin has it too)
@app.route("/reviews/edit/<movie_id>/<review_id>", methods=["GET"])
@login_required(role="USER")
def reviews_edit_form(movie_id, review_id):
    r = Review.query.get(review_id)
    
    # Checks if the current user posted the review or the user is logged on admin account
    if r.account_id != current_user.id or current_user.admin == False:
        redirect(url_for("reviews_for_movie", movie_id = movie_id))

    m = Movie.query.get(movie_id)
    form = EditReviewForm(rating = r.rating, reviewtext = r.reviewtext)

    return render_template("reviews/edit.html", form = form, movie = m, review = r)

# Method for post request to edit a review, access restricted to user status (note that admin has it too)
@app.route("/reviews/edit/<movie_id>/<review_id>", methods=["POST"])
@login_required(role="USER")
def reviews_edit_entry(movie_id, review_id):
    r = Review.query.get(review_id)
    
    # Checks if the current user posted the review or the user is logged on admin account
    if r.account_id != current_user.id or current_user.admin == False:
        redirect(url_for("reviews_for_movie", movie_id = movie_id))

    form = EditReviewForm(request.form)

    if not form.validate():
        return render_template("reviews/edit.html", form = form, movie = Movie.query.get(movie_id))
    
    r.rating = form.rating.data
    r.reviewtext = form.reviewtext.data

    db.session().commit()

    return redirect(url_for("reviews_view", review_id = review_id, movie_id = movie_id))