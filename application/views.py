from flask import render_template
from application import app
from application.movies.models import Movie

@app.route("/")
def index():
    return render_template("index.html", topmovies = Movie.list_movies_with_highest_scores())