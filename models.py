# UserMixin-Klasse und DB werden importiert
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from .db import db

#Datenbankmodell erstellen für User 
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
# Beziehungen
    hosted_events = db.relationship('Event', backref='host', lazy=True)  # Events, die dieser User hostet
    joined_events = db.relationship('Event', secondary='event_participants', backref='participants', lazy='dynamic')  # Events, an denen der User teilnimmt
    sent_likes = db.relationship('UserLikes', foreign_keys='UserLikes.liker_id', backref='liker', lazy=True)
    received_likes = db.relationship('UserLikes', foreign_keys='UserLikes.liked_id', backref='liked', lazy=True)

#Datenbankmodell erstellen für Event 
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(150), nullable=False)
    event_description = db.Column(db.Text, nullable=True)
    event_date = db.Column(db.Date, nullable=False)
    event_starttime = db.Column(db.Time, nullable=False)
    event_endtime = db.Column(db.Time, nullable=False)
    event_location = db.Column(db.String(200), nullable=False)
    max_participants = db.Column(db.Integer, nullable=True, default=10)
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link event to a user


# Datenbankbeziehung zwischen Event und User
event_participants = db.Table(
    'event_participants',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

# Datenmodell für UserLikes (Matches)
class UserLikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    liker_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Nutzer, der das Like sendet
    liked_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Nutzer, der das Like erhält
