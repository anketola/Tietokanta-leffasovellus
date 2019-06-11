from flask import render_template
from application import app
from application.movies.models import Movie
from application.reviews.models import Review

@app.route("/")
def index():
    return render_template("index.html", topmovies = Movie.list_movies_with_highest_scores(), 
        latestmovies = Movie.list_latest_movie_additions(),
        latestreviews = Review.list_latest_reviews())