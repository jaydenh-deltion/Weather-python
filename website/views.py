from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint('views', __name__)  # Create a Blueprint for views

@views.route('/') # Define the home route
def home():
    return "<h1> Test</h1>"
    return render_template("home.html")