from flask import Flask, render_template

app = app = Flask(__name__)

@app.route('/login')
def index():
    # login.html template rendern 
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
