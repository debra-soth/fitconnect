from flask import render_template, redirect, url_for, flash
from .db import create_app, db  # Importiere create_app Funktion aus db.py
from .auth import auth, PersonalizeProfileForm
from .models import User, Event, UserLikes # Importiere Datenmodelle
from .forms import JoinEventForm, LikeForm
from flask_login import current_user

# Flask App mit create_app Funktion erstellen
app = create_app()

#Route für login.html
@app.route('/')
def index():
     return redirect(url_for('auth.login'))

#Route für personalizeProfile.html
@app.route('/personalize')
def personalize_profile():
    return render_template('personalizeProfile.html', form=PersonalizeProfileForm())  # Übergebe das Formular an das Template

#Route für userOverview.html
@app.route('/user')
def user_overview():
    users = User.query.all()  # Fetch all users from the database
    return render_template('userOverview.html', users=users)  # Pass the user data to the template

#Route für eventOverview.html
@app.route('/events') 
def event_overview():
    events = Event.query.all()  # Retrieve all events from the database
    return render_template('eventOverview.html', events=events)

#Route für eventDetails.html
@app.route('/event-details/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)  # Holt das Event oder gibt 404 zurück
    form = JoinEventForm()  # Initialisiere ein Formular für das Beitreten des Events
    return render_template('eventDetails.html', event=event, form=form)

@app.route('/user/<int:user_id>')
def user_profile_detail(user_id):
    user = User.query.get_or_404(user_id)  # Holt den User oder gibt 404-Fehler zurück

    # Alle Matches abrufen (gegenseitige Likes)
    matched_users = [
        like.liker for like in UserLikes.query.filter_by(liked_id=current_user.id).all()
        if UserLikes.query.filter_by(liker_id=current_user.id, liked_id=like.liker.id).first()
    ]

    form = LikeForm()  # Initialisiere Like-Formular

    return render_template('userProfileDetail.html', user=user, matched_users=matched_users, form=form)

@app.route('/your-matches')
def your_matches():
    # Alle User, die current_user geliked haben
    users_who_liked_you = [like.liker for like in UserLikes.query.filter_by(liked_id=current_user.id).all()]

    # Alle Matches (gegenseitige Likes)
    matched_users = [
        like.liker for like in UserLikes.query.filter_by(liked_id=current_user.id).all()
        if UserLikes.query.filter_by(liker_id=current_user.id, liked_id=like.liker.id).first()
    ]

    # Entferne gematchte User aus "Your Likes"
    users_who_liked_you = [user for user in users_who_liked_you if user not in matched_users]

    # Alle Events, in denen current_user Teilnehmer ist
    joined_events = current_user.joined_events

    return render_template('yourMatches.html', 
                           users_who_liked_you=users_who_liked_you, 
                           joined_events=joined_events, 
                           matched_users=matched_users)

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)

