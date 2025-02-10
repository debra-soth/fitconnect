# Module und Klassen aus Flask werden importiert
from flask import Blueprint, render_template, redirect, url_for, flash, flash, request
import os

# Funktionen und Klassen aus Flask-Login und Werkzeug werden importiert
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename

# User-Modell, Registrieruns-Forms, PersonalizeProfile-Forms und DB-Verbindung werden importiert
from .db import db
from .models import User
from .forms import RegistrationForm
from .forms import PersonalizeProfileForm

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
        existing_user_by_email = User.query.filter_by(email=form.email.data).first()
        # Wenn Benutzer oder die E-Mail-Adresse existiert, dann Fehlermeldung ausgeben
        if existing_user:
            flash('The username is already taken. Please choose another one.', 'error')
        elif existing_user_by_email:
            flash('The email address is already registered. Please use a different one.', 'error')
        else:
            # Passwort wird gehasht mit pbkdf2: sha 256-Methode
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            # Neuen Benutzer erstellen und zur Datenbank hinzufügen
            new_user = User(username=form.username.data, first_name=form.first_name.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            #Ausgabe einer Erfolgsmeldung und Weiterleitung zur Login-Page zum direkten Einloggen nach erfolgreichem Registrieren
            flash('Successfully registered! Please log in.', 'success')
            return redirect(url_for('auth.login'))
    # Registerformular wird gerendert
    return render_template('register.html', form=form, signup_success=False)

# Route zum Einloggen von Benutzern
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #Wenn request empfangen wird und Formular gesendet wurde, nehme Benutzernamen und Passwort aus dem Formular
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Aussgabe der Anmeldeinformationen zum Debuggen 
        print(f"Received login request for username: {username}, password: {password}")
        
        #Abgleich des eingebenen Benutzernamens mit den Nutzern in der Datenbank
        user = User.query.filter_by(username=username).first()

        #Wenn Benutzer in DB nicht gefunden wurde, wird Fehlermeldung ausgegeben. Wenn doch, gib Benutzer und Passworthash aus (wieder zum Debuggen)
        if not user:
            flash('User not found. Please check your username.', category='error')
        else:
            print(f"User found in the database: {user.username}")
            print(f"Stored password hash: {user.password}")
        #PW wird mit gespeichertem PW-hash verglichen. Wenn PW korrekt, dann wird der Benutzer eingeloggt, direkt zur useroverview.html weitergeleitet und Erfolgsmeldung ausgegeben.
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Successfully logged in!', category='success')
                return redirect(url_for('personalize_profile'))
            # Wenn PW inkorrekt eingegeben, dann wird eine Fehlermeldung ausgegeben.
            else:
                flash('Wrong password. Please try again', category='error')
    # Das Login-Formular wird gerendert
    return render_template('login.html', user=current_user)

# Route für das Ausloggen von Benutzern
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    # Logge den aktuellen Benutzer aus
    logout_user()

    # Gib eine Erfolgsmeldung aus und leite Benutzer zur Login Seite weiter.
    flash('Successfully logged out!', category='success')
    return redirect(url_for('auth.login'))

# Route für das Personalisieren des Profils
@auth.route('/personalize', methods=['GET', 'POST'])
@login_required
def personalize_profile():
    form = PersonalizeProfileForm()
    
    # Wenn das Formular abgeschickt wird (POST)
    if form.validate_on_submit():
        # Profilbild hochladen und speichern
        if form.profile_photo.data:
            profile_photo = form.profile_photo.data
            photo_filename = secure_filename(profile_photo.filename)
            photo_path = os.path.join('static/images', photo_filename)
            profile_photo.save(photo_path)
        else:
            photo_path = None
        
        # Benutzerinformationen aktualisieren
        current_user.profile_photo = photo_path
        current_user.favorite_activities = form.favorite_activity.data
        current_user.gym_membership = form.gym_membership.data
        current_user.availability = form.availability.data
        current_user.fitness_level = form.fitness_level.data
        current_user.age = form.age.data
        current_user.gender = form.gender.data
        current_user.motivation_text = form.motivation_text.data
        
        # Änderungen in der Datenbank speichern
        db.session.commit()

        flash('Your profile has been updated successfully!', 'success')
        return redirect(url_for('auth.personalize_profile'))
    
    return render_template('personalizeProfile.html', form=form)