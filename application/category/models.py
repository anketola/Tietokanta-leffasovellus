from application import db
from application.models import moviescategories

class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    moviescategories = db.relationship("Movie", secondary = moviescategories, backref='categories')

    def __init__(self, name):
        self.name = name
