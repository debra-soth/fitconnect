# UserMixin-Klasse und DB werden importiert
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from fitconnect.db import db
#Datenbankmodell Erstellen für User 
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_photo = db.Column(db.String(200), nullable=True) #gespeichert als Dateipfad
    favorite_activities = db.Column(db.PickleType, nullable=True)  # Mit PickleType können die Aktivitäten als Phython-Liste gespeichert werden
    gym_membership = db.Column(db.String(100), nullable=True)
    availability = db.Column(db.PickleType, nullable=True)  # PickleType ermöglicht die Speicherung der Liste von Strings (hier Wochentage)
    fitness_level = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    motivation_text = db.Column(db.Text, nullable=True)
