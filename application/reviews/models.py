from application import db
from application.models import Base

class Review(Base):

    reviewtext = db.Column(db.String(144), nullable=False)
    rating = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def __init__(self, reviewtext, rating):
        self.text = reviewtext
        self.rating = rating