# Formulare aus Flask-WTF und Validatoren aus WTForms werden importiert
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FileField
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
    
# Formular für das Personalisieren des Profil
class PersonalizeProfileForm(FlaskForm):
    profile_photo = FileField('Profile Photo', validators=[Optional()]) # Profilbild (optional, mit FileField für das Hochladen von Bildern)
    favorite_activity = StringField('Favorite Fitness Activity', validators=[InputRequired(), Length(min=3)])
    gym_membership = StringField('Gym Membership', validators=[Optional(), Length(max=100)])
    availability = SelectMultipleField('Availability on Weekdays',
        choices=[('Monday'), ('Tuesday'), ('Wednesday'),('Thursday'), ('Friday'), ('Saturday'),('Sunday')],
        validators=[InputRequired()])
    fitness_level = IntegerField('Fitness Level (1-10)', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('Female'), ('Male'), ('Diverse')],
                         validators=[Optional()])
    motivation_text = TextAreaField('Motivation Text', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Save')