from flask import Flask, render_template
from .auth import auth 
from .db import create_app  # Importiere create_app Funktion aus db.py

app = Flask(__name__)

# Flask App mit create_app Funktion erstellen
app = create_app()
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
@app.route('/settings')
def account_settings():
    return render_template('accountSettings.html')
if __name__ == '__main__':
    app.run(debug=True)
