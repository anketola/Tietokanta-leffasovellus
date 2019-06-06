from application import db
from application.models import Base

class Review(Base):

    rating = db.Column(db.Integer, nullable=False)
    reviewtext = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __init__(self, reviewtext, rating):
        self.rating = rating
        self.reviewtext = reviewtext
    