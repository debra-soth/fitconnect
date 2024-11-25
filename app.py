import os
from flask import Flask, render_template
import db

app = app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

@app.route('/')
def index():
    # Render the login.html template
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
