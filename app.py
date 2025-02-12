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
@app.route('/event-details') 
def event_details():
    return render_template('eventDetails.html') 

#Route für createEvent.html
@app.route('/create-event', methods=['GET', 'POST'])
def create_event():
    form = CreateEventForm()
    if form.validate_on_submit():
        event = Event(
            name=form.event_name.data,
            description=form.event_description.data,
            date=form.event_date.data,
            start_time=form.event_starttime.data,
            end_time=form.event_endtime.data,
            location=form.event_location.data,
            max_participants=form.participants.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('event_overview'))
    return render_template('createEvent.html', form=form)

# Route für userProfileDetail.html
@app.route('/user/<int:user_id>')
def user_profile_detail(user_id):
    user = User.query.get(user_id)  # Holt den User mit der gegebenen ID aus der Datenbank
    return render_template('userProfileDetail.html', user=user)  # Übergibt den User an das Template

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)