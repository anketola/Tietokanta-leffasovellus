from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    reviews = db.relationship("Review", backref='account', lazy=True)

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
   
    def roles(self):
        if self.admin == True:
            return ["USER", "ADMIN"]
        else:
            return ["USER"]
    
    @staticmethod
    def user_reviews_list(userid):
        stmt = text("SELECT Review.id, Review.rating, Review.date_created, Movie.name, Movie.id FROM Review, Movie"
                    " WHERE Review.account_id = Account_id AND Movie.id = Review.movie_id AND Account_id = :userid").params(userid = userid)
        res = db.engine.execute(stmt)
        response = []

        for row in res:
            response.append({"review_id":row[0], "rating":row[1], "added": row[2], "name": row[3], "movie_id": row[4]})

        return response    