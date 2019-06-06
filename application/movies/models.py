from application import db
from application.models import Base

class Movie(Base):

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=False)

    reviews = db.relationship("Review", backref='movie', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description