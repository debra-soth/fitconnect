# Flask und SQLAlchemy werden importiert
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate

# Eine Datenbankinstanz wird erstellt und der Name der Datenbankdatei wird definiert
db = SQLAlchemy()
migrate = Migrate()
DB_NAME = 'database.db'

# Funktion zur Erstellung der Flask-Anwendung
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'FitConnect'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://neondb_owner:npg_emF8Pudwct1E@ep-super-queen-a2fxr5l1-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'
    app.config['WTF_CSRF_ENABLED'] = True 

    # Hier wird die db-Instanz mit der App verbunden
    db.init_app(app)
    migrate.init_app(app, db)  # <--- Migrate hinzufügen
    csrf = CSRFProtect(app)  # CSRF Protection aktivieren
    # Blueprints werden importiert
    from .auth import auth

    # Blueprints für die entsprechenden URLs werden registriert
    app.register_blueprint(auth, url_prefix='/auth')

    # Bevor DB initialisiert wird, müssen die DB-Modelle definiert werden
    from .models import User, Event

    # SQLAlchemy testet, ob Datenbank bereits vorhanden ist oder nicht
    with app.app_context():
        db.create_all()

    # Login Manager wird initialisiert
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # Authentifizierungs-Login-Route
    login_manager.init_app(app)

    # Funktion zum Laden eines Benutzers
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app