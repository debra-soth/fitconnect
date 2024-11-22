from flask import Flask, render_template

app = app = Flask(__name__)

@app.route('/')
def index():
    # Render the login.html template
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
