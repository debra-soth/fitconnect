# Module und Klassen aus Flask werden importiert
from flask import Blueprint, render_template, redirect, url_for, flash

# Funktionen und Klassen aus Flask-Login und Werkzeug werden importiert
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

# User-Modell, Registrieruns-Forms und DB-Verbindung werden importiert
from . import db
from .models import User
from .forms import RegistrationForm

# Blueprint für Authentifizierurng wird definiert
auth = Blueprint('auth', __name__)

# Route für die Registrierung von Benutzern
@auth.route('/register', methods=['GET', 'POST'])
def register():
    # RegistrationsForm-Objekt wird erstellt
    form = RegistrationForm()
    # Wenn Formular validiert wurde, indem Post-request mit Daten gesendet wurde, überprüfe, ob ein Benutzer mit dem angegebenen Benutzernamen bereits existiert 
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        # Wenn Benutzer existiert, dann Fehlermeldung ausgeben
        if existing_user:
            flash('The username is already taken. Please choose another one.', 'error')
        else:
            # Passwort wird gehasht mit pbkdf2: sha 256-Methode
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            # Neuen Benutzer erstellen und zur Datenbank hinzufügen
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            #Ausgabe einer Erfolgsmeldung und Weiterleitung zur Login-Page zum direkten Einloggen nach erfolgreichem Registrieren
            flash('Successfully registered! Please log in.', 'success')
            return redirect(url_for('views.index'))
    # Registerformular wird gerendert
    return render_template('register.html', form=form, signup_success=False)

