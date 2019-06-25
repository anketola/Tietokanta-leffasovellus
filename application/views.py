from flask import render_template
from application import app
from application.movies.models import Movie
from application.reviews.models import Review

# The method returns the main page of the application, and performs various queries to gather
# all the data to populate the statistics on the first page
@app.route("/")
def index():
    return render_template("index.html", topmovies = Movie.list_movies_with_highest_scores(), 
        latestmovies = Movie.list_latest_movie_additions(),
        latestreviews = Review.list_latest_reviews())