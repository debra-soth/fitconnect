from flask import render_template, redirect, url_for, flash
from .db import create_app, db  # Importiere create_app Funktion aus db.py
from .auth import auth, PersonalizeProfileForm
from .models import User, Event  # Import the User model
from .forms import CreateEventForm

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
    return render_template('eventDetails.html', event=event)

# Route für userProfileDetail.html
@app.route('/user/<int:user_id>')
def user_profile_detail(user_id):
    user = User.query.get(user_id)  # Holt den User mit der gegebenen ID aus der Datenbank
    #print("Profile Photo Path:", user.profile_photo)
    return render_template('userProfileDetail.html', user=user)  # Übergibt den User an das Template

# Route für yourMatches.html
@app.route('/your-matches')
def your_matches():
    return render_template('yourMatches.html')

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)

