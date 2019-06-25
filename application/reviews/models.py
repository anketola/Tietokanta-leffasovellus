from application import db
from application.models import Base

from sqlalchemy.sql import text

# Review is the entity that a registered and logged in user gives for a movie
class Review(Base):

    rating = db.Column(db.Integer, nullable=False)
    reviewtext = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __init__(self, reviewtext, rating):
        self.rating = rating
        self.reviewtext = reviewtext
    
    # Query returns the five most recent reviews posted in the application
    @staticmethod
    def list_latest_reviews():
        stmt = text("SELECT Review.id, Review.rating, Review.date_created, Movie.name, Movie.id FROM Review"
                    " INNER JOIN Movie on Movie.id = Review.movie_id"
                    " ORDER BY Review.date_created DESC"
                    " LIMIT 5")
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"id":row[0], "rating":row[1], "added":row[2], "name":row[3], "movie_id":row[4]})
        
        return response