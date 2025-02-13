# Module und Klassen aus Flask werden importiert
from flask import Blueprint, render_template, redirect, url_for, flash, flash, request
import os

# Funktionen und Klassen aus Flask-Login und Werkzeug werden importiert
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename

# User-Modell, Registrieruns-Forms, PersonalizeProfile-Forms, Login-Forms und DB-Verbindung werden importiert
from .db import db
from .models import User, Event, event_participants, UserLikes
from .forms import RegistrationForm, PersonalizeProfileForm, LoginForm, AccountSettingsForm, CreateEventForm


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
    # Login-Objekt wird erstellt
    form = LoginForm()
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
                return redirect(url_for('user_overview'))
            # Wenn PW inkorrekt eingegeben, dann wird eine Fehlermeldung ausgegeben.
            else:
                flash('Wrong password. Please try again', category='error')
    # Das Login-Formular wird gerendert
    return render_template('login.html', form=form)

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

     # Debugging: Überprüfe, ob der Code erreicht wird
    print("Formular wurde abgeschickt")
    # Wenn das Formular abgeschickt wird (POST)
    if form.validate_on_submit():
         # Debugging: Alle Formulardaten im Terminal ausgeben
        print(f"Profile Photo: {form.profile_photo.data}")
        print(f"Favorite Activities: {form.favorite_activities.data}")
        print(f"Gym Membership: {form.gym_membership.data}")
        print(f"Availability: {form.availability.data}")
        print(f"Fitness Level: {form.fitness_level.data}")
        print(f"Age: {form.age.data}")
        print(f"Gender: {form.gender.data}")
        print(f"Motivation Text: {form.motivation_text.data}")
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
        current_user.favorite_activities = form.favorite_activities.data
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
    
        #Fehlerausgabe fürs Debbugen
    if not form.validate_on_submit():
         print("Formular-Validierung fehlgeschlagen!")
         print(form.errors)  # Ausgabe der Fehler, falls vorhande
        
         return render_template('personalizeProfile.html', form=form)
    
    
    return render_template('personalizeProfile.html', form=form)

# Route für Account Settings
@auth.route('/settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    form = AccountSettingsForm(obj=current_user)  # Füllt das Formular mit aktuellen User-Daten

    print("Formular wurde geladen")  # Debugging: Wird die Route aufgerufen?

    if request.method == 'POST':
        print("POST-Request wurde empfangen")  # Debugging: Prüfen, ob das Formular abgeschickt wurde
        print("Formulardaten:", request.form)  # Debugging: Alle empfangenen Formulardaten anzeigen

        if form.validate_on_submit():
            print("Formular wurde validiert")  # Debugging: Ist die Validierung erfolgreich?

            # Aktualisiere die User-Daten mit den neuen Formulardaten
            current_user.username = form.username.data
            current_user.first_name = form.first_name.data
            current_user.email = form.email.data

            # Falls ein neues Passwort eingegeben wird, speichere es gehasht
            if form.password.data:
                print("Neues Passwort erkannt")  # Debugging
                current_user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

            # Profilbild hochladen und speichern
            if form.profile_photo.data:
                print("Profilbild wird verarbeitet")  # Debugging
                profile_photo = form.profile_photo.data
                photo_filename = secure_filename(profile_photo.filename)
                photo_path = os.path.join('static/images', photo_filename)
                profile_photo.save(photo_path)
                current_user.profile_photo = photo_path  # Speichere den Bildpfad

            # Speichern der restlichen Formulardaten
            current_user.favorite_activities = form.favorite_activities.data
            current_user.gym_membership = form.gym_membership.data
            current_user.availability = form.availability.data
            current_user.fitness_level = form.fitness_level.data
            current_user.age = form.age.data
            current_user.gender = form.gender.data
            current_user.motivation_text = form.motivation_text.data

            # Speichern der Änderungen in der Datenbank
            try:
                db.session.commit()
                print("Änderungen erfolgreich gespeichert")  # Debugging
                flash("Profile successfully updated!", "success")

                # Weiterleitung zur User-Übersicht
                return redirect(url_for('user_overview'))
            except Exception as e:
                print("Fehler beim Speichern in der Datenbank:", str(e))  # Debugging
                db.session.rollback()  # Falls etwas schiefgeht, rollback machen

        else:
            print("Formularvalidierung fehlgeschlagen")  # Debugging
            print(form.errors)  # Debugging: Zeigt an, warum das Formular fehlschlägt

    return render_template('accountSettings.html', form=form)

# Route zum Erstellen eines Events
@auth.route('/create-event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = CreateEventForm()
    if request.method == "POST":
        print("POST-Request erhalten!")  # Debugging: Wird ein POST-Request empfangen?

    if form.validate_on_submit():
        print("Formular wurde validiert!")  # Debugging: Wird das Formular korrekt validiert?
        print(f"Eingegebene Daten: {form.data}")  # Debuggibng: Alle Formulardaten anzeigen

        new_event = Event(
            event_name=form.event_name.data,
            event_description=form.event_description.data,
            event_date=form.event_date.data,
            event_starttime=form.event_starttime.data,
            event_endtime=form.event_endtime.data,
            event_location=form.event_location.data,
            max_participants=form.max_participants.data,
            host_id=current_user.id  # Host wird automatisch gesetzt!
        )
        db.session.add(new_event)
        try:
            db.session.commit()
            print("Event wurde erfolgreich gespeichert!")  # DEBUG: Erfolgreiches Speichern
            flash("Event successfully created!", "success")
            return redirect(url_for('event_overview'))
        except Exception as e:
            db.session.rollback()
            print("Fehler beim Speichern des Events:", str(e))  # DEBUG: Fehler anzeigen
            flash("An error occurred while creating the event.", "danger")

    else:
        print("Formular ist ungültig!")  # Falls Validierung fehlschlägt
        print(form.errors)  # Fehler ausgeben

    return render_template('createEvent.html', form=form)

#Route fürs Joinen eines Events
@auth.route('/join-event/<int:event_id>', methods=['POST'])
@login_required
def join_event(event_id):
    event = Event.query.get_or_404(event_id)

    # Überprüfen, ob der Benutzer bereits Teilnehmer ist
    already_joined = db.session.query(event_participants).filter_by(user_id=current_user.id, event_id=event.id).first()
    if already_joined:
        flash('You are already part of this event.', 'warning')
        return redirect(url_for('event_overview')) 

    # Überprüfen, ob die maximale Teilnehmerzahl erreicht wurde
    current_participants_count = db.session.query(event_participants).filter_by(event_id=event.id).count()
    if current_participants_count >= event.max_participants:
        flash('This event is already full.', 'danger')
        return redirect(url_for('event_overview')) 

    # User zum Event hinzufügen
    db.session.execute(event_participants.insert().values(user_id=current_user.id, event_id=event.id))
    db.session.commit()

    flash('Successfully joined the event!', 'success')
    return redirect(url_for('event_overview')) 

# Route für das Liken eines Users
@auth.route('/like/<int:user_id>', methods=['POST'])
@login_required
def like_user(user_id):
    # Überprüfen, ob der gelikte User existiert
    liked_user = User.query.get_or_404(user_id)

    # Prüfen, ob das Like bereits existiert
    existing_like = UserLikes.query.filter_by(liker_id=current_user.id, liked_id=user_id).first()
    if existing_like:
        flash("You have already liked this user!", "warning")
        return redirect(url_for('your_matches'))

    # Neues Like in die Datenbank einfügen
    new_like = UserLikes(liker_id=current_user.id, liked_id=user_id)
    db.session.add(new_like)
    db.session.commit()

    # Prüfen, ob ein gegenseitiges Like existiert → Falls ja, sind beide Matches!
    mutual_like = UserLikes.query.filter_by(liker_id=user_id, liked_id=current_user.id).first()
    if mutual_like:
        flash("It's a Match! 🎉 You can now see their contact details.", "success")
    else:
        flash("You liked this user! If they like you back, you'll be matched.", "info")

    return redirect(url_for('your_matches'))