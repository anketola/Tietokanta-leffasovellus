from application import db
from application.models import Base, moviescategories

from sqlalchemy.sql import text

# Movie is the entity that is the object of reviews and it has a many-to-many relationship to categories
class Movie(Base):

    name = db.Column(db.String(144), nullable=False)
    released = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)

    reviews = db.relationship("Review", backref='movie', lazy=True, cascade="all, delete-orphan")

    moviescategories = db.relationship("Category", secondary = moviescategories, backref='movies')

    def __init__(self, name, released, description):
        self.name = name
        self.released = released
        self.description = description
    
    # The query returns a top five list of all rated movies and additionally the average scores for those movies
    @staticmethod
    def list_movies_with_highest_scores():
        stmt = text("SELECT Movie.name, Movie.id, CAST(AVG(Review.rating) AS DECIMAL(10,2)) FROM MOVIE"
                    " INNER JOIN Review on Movie.id = Review.movie_id"
                    " GROUP BY Movie.id"
                    " ORDER BY AVG(Review.rating) DESC"
                    " LIMIT 5")
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"name":row[0], "id":row[1], "averagescore":row[2]})

        return response
    
    # Returns latest 5 movies added by the admin
    @staticmethod
    def list_latest_movie_additions():
        stmt = text("SELECT Movie.id, Movie.name, Movie.date_created FROM Movie"
                    " ORDER BY Movie.date_created DESC"
                    " LIMIT 5")
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"id":row[0], "name":row[1], "added":row[2]})
        
        return response

    # Returns the total number of reviews for a given movie
    @staticmethod
    def review_count_for_movie(movieid):
        stmt = text("SELECT COUNT(Review.id) FROM Movie, Review WHERE Movie.id = Review.movie_id AND Movie.id = :movieid").params(movieid = movieid)
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"revcount":row[0]})

        return response
    
    # Returns the average rating for a given movie
    @staticmethod
    def average_rating_for_movie(movieid):
        stmt = text("SELECT CAST(AVG(Review.rating) AS DECIMAL(10,2)) FROM Movie, Review WHERE Movie.id = Review.movie_id AND Movie.id = :movieid").params(movieid = movieid)
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"average":row[0]})

        return response
    
    # Query used to list best rated movies in a category, used via form in the "Selaa elokuvia" view
    @staticmethod
    def movies_category_best(categoryid):
        stmt = text("SELECT Movie.id, Movie.name, Movie.released, AVG(Review.rating) FROM Movie"
                    " INNER JOIN Review ON Review.movie_id = Movie.id"
                    " INNER JOIN Moviescategories ON Moviescategories.movie_id = Movie.id"
                    " INNER JOIN Category ON Category.id = Moviescategories.category_id"
                    " WHERE Category.id = :categoryid"
                    " GROUP BY Movie.id"
                    " ORDER BY AVG(Review.rating) DESC").params(categoryid = categoryid)
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"movie_id":row[0], "movie_name":row[1], "movie_released":row[2], "avg_rating":row[3]})

        return response