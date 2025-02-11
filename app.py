from flask import render_template, redirect, url_for
from .db import create_app  # Importiere create_app Funktion aus db.py
from .auth import auth, PersonalizeProfileForm

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

#Route für accountSettings
@app.route('/settings')
def account_settings():
    return render_template('accountSettings.html')

#Route für userOverview.html
@app.route('/user')
def user_overview():
    users = User.query.all() 
    return render_template('userOverview.html') 

#Route für eventOverview.html
@app.route('/events') 
def event_overview():
    return render_template('eventOverview.html') 

#Route für eventDetails.html
@app.route('/event-details') 
def event_details():
    return render_template('eventDetails.html') 

#Route für createEvent.html
@app.route('/create-event') 
def create_event():
    return render_template('createEvent.html') 

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)

