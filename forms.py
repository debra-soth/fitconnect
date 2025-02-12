# Formulare aus Flask-WTF und Validatoren aus WTForms werden importiert
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FileField, FieldList
from wtforms.validators import InputRequired, Email, EqualTo, Length, Optional
from wtforms.fields import SelectField
from wtforms import SelectMultipleField

# Formular für die Registrierung
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    first_name = StringField('First name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=7), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

# Formular für die Anmeldung
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

# Formular für das Personalisieren des Profils
class PersonalizeProfileForm(FlaskForm):
    profile_photo = FileField('Profile Photo', validators=[Optional()]) # Profilbild (optional, mit FileField für das Hochladen von Bildern)
    favorite_activities = FieldList(StringField('Favorite Fitness Activity', validators=[InputRequired(), Length(min=3)]), min_entries=1)
    gym_membership = StringField('Gym Membership', validators=[Optional(), Length(max=100)])
    availability = SelectMultipleField('Availability on Weekdays',
        choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
             ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), 
             ('sunday', 'Sunday')],
        validators=[InputRequired(message="Please select at least one availability day.")])
    fitness_level = IntegerField('Fitness Level (1-10)', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = gender = SelectField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Diverse', 'Diverse')],validators=[Optional()])
    motivation_text = TextAreaField('Motivation Text', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Save')

# Formular für das Erstellen eines Events
class CreateEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[InputRequired()])
    event_description = TextAreaField('Event Description', validators=[Optional(), Length(max=250)])
    event_date = StringField('Event Date', validators=[InputRequired()])
    event_starttime = StringField('Event Start Time', validators=[InputRequired()])
    event_endtime = StringField('Event End Time', validators=[InputRequired()])
    event_location = StringField('Event Location', validators=[InputRequired()])
    submit = SubmitField('Create Event')

# Formular für das Bearbeiten des Profils
class AccountSettingsForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    first_name = StringField('First name', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[Optional()])
    profile_photo = FileField('Profile Photo', validators=[Optional()]) # Profilbild (optional, mit FileField für das Hochladen von Bildern)
    favorite_activities = FieldList(StringField('Favorite Fitness Activity', validators=[InputRequired(), Length(min=3)]), min_entries=1)
    gym_membership = StringField('Gym Membership', validators=[Optional(), Length(max=100)])
    availability = SelectMultipleField('Availability on Weekdays',
        choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
             ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), 
             ('sunday', 'Sunday')],
        validators=[InputRequired(message="Please select at least one availability day.")])
    fitness_level = IntegerField('Fitness Level (1-10)', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = gender = SelectField('Gender', choices=[('Female', 'Female'), ('Male', 'Male'), ('Diverse', 'Diverse')],validators=[Optional()])
    motivation_text = TextAreaField('Motivation Text', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Save')