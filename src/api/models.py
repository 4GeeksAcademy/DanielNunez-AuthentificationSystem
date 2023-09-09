# from flask_sqlalchemy import SQLAlchemy
# from uuid import uuid4

# db = SQLAlchemy()

# def get_uuid():
#     return uuid4().hex

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.String, primary_key=True, unique=True, default=get_uuid)
#     name = db.Column(db.String, unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)