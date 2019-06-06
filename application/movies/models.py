from application import db
from application.models import Base

class Movie(Base):

    name = db.Column(db.String(144), nullable=False)
    released = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)

    reviews = db.relationship("Review", backref='movie', lazy=True)

    def __init__(self, name, released, description):
        self.name = name
        self.released = released
        self.description = description