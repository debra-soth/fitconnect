from flask import Flask, render_template

app = app = Flask(__name__)

@app.route('/')
def index():
#Route für login.html
    return render_template('login.html')

#Route für register.html
@app.route('/register')
def register():
    return render_template('register.html')

#Route für personalizeProfile.html
@app.route('/personalize')
def personalize_profile():
    return render_template('personalizeProfile.html')

#Route für accountSettings.html
@app.route('/settings')
def account_settings():
    return render_template('accountSettings.html')

#Route für userOverview.html
@app.route('/user')
def user_overview():
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

if __name__ == '__main__':
    app.run(debug=True)
