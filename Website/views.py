from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user


views = Blueprint('views',__name__)


# This is the route for the home page, where the Kanban Board is present
@views.route('/', methods=['GET', 'POST'])
# This route requires the user to be logged in

def home():
    return render_template("home.html", user=current_user)
    


