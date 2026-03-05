from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(120), unique=True)

    # Password is stored as a HASH instead of plain text
    # This protects user data if the database is compromised
    password = db.Column(db.String(200))