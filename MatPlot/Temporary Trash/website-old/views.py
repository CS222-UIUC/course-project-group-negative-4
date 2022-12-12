from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# URL to get to this endpoint
@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about_us')
def about_us():
    return render_template("about_us.html")

@views.route('/course_details')
def course_details():
    return render_template("course_details.html")

@views.route('/course_list')
def course_list():
    return render_template("course_list.html")
