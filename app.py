import os
from flask import Flask, render_template
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'fitconnect.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

# Access database connection
def get_db():
    return db.get_db_con()

@app.route('/')
def index():
    # Render the login.html template
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    # Fetch users from database
    db_con = get_db()
    cursor = db_con.execute("SELECT username, name, gender, fitness_level, activities, profile_photo FROM user")
    users = [
        {
            'username': row['username'],
            'name': row['name'],
            'gender': row['gender'],
            'fitness_level': row['fitness_level'],
            'activities': row['activities'],
            'profile_photo': row['profile_photo']
        }
        for row in cursor.fetchall()
    ]

    # Add placeholder values if no users are found
    if not users:
        users = [
            {
                'username': 'placeholder_user1',
                'name': 'Placeholder User 1',
                'gender': 'N/A',
                'fitness_level': 'N/A',
                'activities': 'Running, Cycling',
                'profile_photo': 'default_user_icon.png'
            },
            {
                'username': 'placeholder_user2',
                'name': 'Placeholder User 2',
                'gender': 'N/A',
                'fitness_level': 'N/A',
                'activities': 'Tennis, Football',
                'profile_photo': 'default_user_icon.png'
            }
        ]

    current_user_name = "Username"  # Replace with a real logged-in user value once authentication is added
    return render_template('homepage.html', users=users, current_user_name=current_user_name)

if __name__ == '__main__':
    app.run(debug=True)