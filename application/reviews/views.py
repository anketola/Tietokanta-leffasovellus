from flask import render_template, request, url_for, redirect
from flask_login import login_required

from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews/new/")
def reviews_form():
    return render_template("reviews/new.html", form = ReviewForm())