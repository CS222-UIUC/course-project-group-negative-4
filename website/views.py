from flask import Blueprint, redirect, render_template, request, send_file, make_response, url_for, Response
from io import BytesIO
from flask import send_from_directory
#Pandas and Matplotlib
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#other requirements
import io

#Data imports
# df = pd.read_csv('/Users/dheryajalan/Documents/UIUC/Fall_22/cs222/course-project-group-negative-4/website/sp2021.csv').reset_index()
# group = df.groupby("Subject")
# df_mean = group.agg("mean").reset_index()

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


#Matplotlib page
@views.route('/matplot', methods=("POST", "GET"))
def mpl():
    return render_template('matplot.html',
                           PageTitle = "Matplotlib")

@views.route('/course_visualization', methods=("POST", "GET"))
def course_visualization():
    df = pd.read_csv('/Users/jaywoojo/course-project-group-negative-4/website/sp2021.csv').reset_index()
    #group = df.groupby("Subject")
    course = request.form['searched']
    lst = course.split()
    sub = lst[0]
    course_num = int(lst[1])
    int(course_num)
    df = df[ (df["Subject"] == sub) & (df['Course'] == course_num)]
    group = df.groupby("Primary Instructor")
    #df = pd.read_csv('/Users/dheryajalan/Documents/UIUC/Fall_22/cs222/course-project-group-negative-4/website/sp2021.csv').reset_index()
    #group = df.groupby("Subject")
    df_mean = group.agg("mean").reset_index() 
    fig, ax = plt.subplots(figsize = (8,8))
    fig.patch.set_facecolor('#E8E5DA')
    x = df_mean["Primary Instructor"]
    y = df_mean.A

    ax.bar(x, y, color = "#304C89")

    plt.xticks(rotation = 30, size = 7)
    plt.xlabel("Professor", size = 5)
    plt.ylabel("Expected A's", size = 5)
    plt.savefig("course-project-group-negative-4/website/static/images/picture")
    #fig = create_figure()
    #canvas = FigureCanvas(fig)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return redirect(url_for('views.mpl'))
   #Response(output.getvalue(), mimetype='image/png')
    #img = BytesIO()
    #fig.savefig(img)
    #canvas.print_png(img)
    #img.seek(0)
    #return send_from_directory("course-project-group-negative-4/website/static", "macs100.png")
    #return send_file(img, mimetype='image/png')
    #return send_file(img, mimetype='image/png')
    #output = io.BytesIO()
    #FigureCanvas(fig).print_png(output)
    #return Response(img.getvalue(), mimetype='image/png')

# def create_figure():
#     df = pd.read_csv('/Users/dheryajalan/Documents/UIUC/Fall_22/cs222/course-project-group-negative-4/website/sp2021.csv').reset_index()
#     #group = df.groupby("Subject")
#     course = request.form['searched']
#     lst = course.split()
#     sub = lst[0]
#     course_num = int(lst[1])
#     int(course_num)
#     df = df[ (df["Subject"] == sub) & (df['Course'] == course_num)]
#     group = df.groupby("Primary Instructor")
#     #df = pd.read_csv('/Users/dheryajalan/Documents/UIUC/Fall_22/cs222/course-project-group-negative-4/website/sp2021.csv').reset_index()
#     #group = df.groupby("Subject")
#     df_mean = group.agg("mean").reset_index() 
#     fig, ax = plt.subplots(figsize = (8,8))
#     fig.patch.set_facecolor('#E8E5DA')
#     x = df_mean["Primary Instructor"]
#     y = df_mean.A

#     ax.bar(x, y, color = "#304C89")

#     plt.xticks(rotation = 30, size = 7)
#     plt.xlabel("Professor", size = 5)
#     plt.ylabel("Expected A's", size = 5)


#     return fig

