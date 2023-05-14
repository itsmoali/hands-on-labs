from flask import Blueprint, render_template, request, flash, redirect, url_for
from Website import db
from .models import  User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# This is the route for the login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Uses the post request to get the email and password from the form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        # Checks if the user exists and if the password is correct
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)

                # Redirects the user to the home page when they login
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    
    return render_template('login.html', user=current_user)



# This is the route for the signup page
@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    # Uses the post request to get the email, first name, password1, and password2 from the form
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        # Checks if the email already exists, if the email is greater than 3 characters, if the first name is greater than 1 character, if the passwords match, and if the password is greater than 7 characters
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Adds the new user to the database and logs them in
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account created!', category='success')

            # Redirects the user to the home page when they sign up
            return redirect(url_for('views.home'))
    return render_template('signup.html' , user= current_user)



# This is the route for the logout page
@auth.route('/logout')
# This decorator makes sure that the user is logged in before they can logout
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



