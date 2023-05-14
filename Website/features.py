
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask import render_template


features = Blueprint('features',__name__)

# This is the route for the home page, where the Robot would be present
@features.route('/robot', methods=['GET', 'POST'])
def robot():
    return render_template("robot.html")
