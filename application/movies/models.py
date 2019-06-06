from application import db
from application.models import Base

from sqlalchemy.sql import text

class Movie(Base):

    name = db.Column(db.String(144), nullable=False)
    released = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)

    reviews = db.relationship("Review", backref='movie', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, released, description):
        self.name = name
        self.released = released
        self.description = description
    
    @staticmethod
    def list_movies_with_highest_scores():
        stmt = text("SELECT Movie.name, AVG(Review.rating) FROM MOVIE"
                    " INNER JOIN Review on Movie.id = Review.movie_id"
                    " GROUP BY Movie.id"
                    " ORDER BY AVG(Review.rating) DESC"
                    " LIMIT 5")
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"name":row[0], "averagescore":row[1]})

        return response