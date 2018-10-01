from flask import Flask, request, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#Create the route to display form

app.route("/")
def index():
    return render_template("base.html")

def empty_val(x):
    if x:
        return True
    else:
        return False

def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def email_at_symbol_more_than_one(x):
    if x.count('@')<=1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.')>=1:
        return True
    else:
        return False

def email_period_more_than_one(x):
    if x.count('.')<=1:
        return True
    else:
        return False

@app.route("/signup", methods=['POST'])
def user_signup_complete():
    username = request.form['username']
    password = request.form ['password']
    password_validate = request.form ['password_validate']
    email = request.form ['email']

    username_error=""
    password_error=""
    password_validate_error=""
    email_error=""

    entry_error = "Error: Entry not valid. (0-24 characters with no spaces)"
    pass_error = "Error: Passwords do not match."
    email_error = "Error: Not a Valid Email Address"

    if not valid_entry(username):
        username_error = entry_error
    if not valid_entry(password):
        password_error = entry_error
    if not valid_entry(password_validate):
        password_validate_error = entry_error
    if not password == password_validate:
        password_error = pass_error
        password_validate = pass_error
    if email:
        if not email_check(email):
            email_error = email_entry_error
        if not valid_entry(email):
            email_error = entry_error

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('body.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)

@app.route('/success')
def valid_signup():
    return render_template('success.html', username=username)

app.run()