from flask import Flask, render_template
from fitconnect.auth import auth 
from .db import create_app  # Importiere create_app Funktion aus db.py

# Es wird überprüft, ob das Skript direkt ausgeführt wird und die Flask-Anwendung wird im Debug-Modus gestartet
if __name__ == '__main__':
    app.run(debug=True)

# Flask App mit create_app Funktion erstellen
app = create_app()

#Route für login.html
@app.route('/')
def login():
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