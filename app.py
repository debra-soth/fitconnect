from flask import Flask, render_template
from .auth import auth 
from .db import create_app  # Importiere create_app Funktion aus db.py
from .auth import LoginForm
from .auth import PersonalizeProfileForm

# Flask App mit create_app Funktion erstellen
app = create_app()
@app.route('/')
def index():
#Route für login.html
    return render_template('login.html', form=LoginForm())  # Übergebe das Formular an das Template
#Route für register.html
@app.route('/register')
def register():
    return render_template('register.html')
#Route für personalizeProfile.html
@app.route('/personalize')
def personalize_profile():
    return render_template('personalizeProfile.html', form=PersonalizeProfileForm())  # Übergebe das Formular an das Template
@app.route('/settings')
def account_settings():
    return render_template('accountSettings.html')
if __name__ == '__main__':
    app.run(debug=True)
