from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Creds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
