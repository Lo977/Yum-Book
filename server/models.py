
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt
# from config import db
from config import db

db = SQLAlchemy()

# Models go here!

class Favorite(db.Model, SerializerMixin):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    note = db.Column(db.String) 

    user = db.relationship("User", back_populates="favorites")
    recipe = db.relationship("Recipe", back_populates="favorites")

class User(db.Model, SerializerMixin):
    __tablenane__ = 'users' 

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)   

    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")
    favorites = db.relationship("Favorite", back_populates="usesr")

class Recipe(db.Model,SerializerMixin):
    __tablename__ = 'recipes'   

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.Foreign_key('users.id'))

    user = db.relationship("User", back_populates="recipes")
    favorites = db.relationship("Favorite", back_populates="recipe")