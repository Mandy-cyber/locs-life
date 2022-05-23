from flask import Blueprint, jsonify, render_template, request

views = Blueprint('views', __name__)

#--------------------------------------------------------------------------------#
#ROUTES

@views.route('/')
def landing_page():
    return render_template("landing.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/my-story')
def my_story():
    return render_template("story.html")

@views.route('/work-experiences')
def my_experiences():
    return render_template("experiences.html")

@views.route('/skills-and-education')
def skills_and_education():
    return render_template("education.html")