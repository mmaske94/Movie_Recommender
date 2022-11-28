from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))