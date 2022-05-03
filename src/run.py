import os
from app import *
from errorHandler import errorHandler, Error404
from functions import *
from config import PORT

@app.route('/')
def index():
    render_template("login.html")

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("signup.html")

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug = True)