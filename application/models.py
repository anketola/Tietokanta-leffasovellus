from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

# This is the joint table declaration for the many-to-many relationship between movies and categories
moviescategories = db.Table('moviescategories',
                    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                    db.Column('category_id', db.Integer, db.ForeignKey('category.id')))