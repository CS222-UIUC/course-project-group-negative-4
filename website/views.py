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

#from jaymatplotlibfinal import *
import numpy as np

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
    """ Dherya's Stuff here copied """
    course = request.form['searched']
    lst = course.split()
    sub = lst[0]
    course_num = int(lst[1])
    int(course_num)
    
    """ Assigning my variable names below equal to the user input ones from above code """
    course = sub
    tag = course_num
    
    """ Read in CSV """
    #df = pd.read_csv('MatPlot-Jay/fa-2021-only.csv')
    df = pd.read_csv('website/CSVs/uiuc-gpa-dataset-fa19-onwards.csv')

    """ Find DF in CSV"""
    df2 = df.loc[(df['Subject'] == course) & (df['Number'] == tag)] #print(df2)
    print("what is thi 1??")
    print(df2)
    df3 = df2.iloc[:,[21,7,8,9,10,11,12,13,14,15,16,17,18,19,20]] 
    print("what is thi??")
    print(df3)

    """ Sum the rows with the same Primary Instructor """
    df3 = df3.groupby('Primary Instructor', as_index=False).sum() #as_index or else the Primary Instructor column name gets weird #print(df3)
    df3 = df3.sort_values(by = ['A+', 'A', 'A-', 'B+', 'B', 'B-']) #print(df3)

    print(df3)
    """ Adjust the DF to Sort by Weighted GPA. Remember it's sorted in Lowest to Highest because later the visualization graph plot will reverse it """
    weight_map = {"A+": 4.00, "A": 4.00, "A-": 3.67,
                "B+": 3.33, "B": 3.00, "B-": 2.67,
                "C+": 2.33, "C": 2.00, "C-": 1.67,
                "D+": 1.33, "D": 1.00, "D-": 0.67,
                "F": 0}
                
    df3['Weighted Sum'] = df3['A+']*(weight_map['A+']) + df3['A']*(weight_map['A']) + df3['A-']*(weight_map['A-']) + df3['B+']*(weight_map['B+']) + df3['B']*(weight_map['B']) + df3['B-']*(weight_map['B-']) + df3['C+']*(weight_map['C+']) + df3['C']*(weight_map['C']) + df3['C-']*(weight_map['C-']) + df3['D+']*(weight_map['D+']) + df3['D']*(weight_map['D']) + df3['D-']*(weight_map['D-']) + df3['F']*(weight_map['F'])
    #df3['Row Sum'] = df3.sum(axis=1) 
    df3['Row Sum'] = df3['A+'] + df3['A'] + df3['A-'] + df3['B+'] + df3['B'] + df3['B-'] + df3['C+'] + df3['C'] + df3['C-'] + df3['D+'] + df3['D'] + df3['D-'] + df3['F']
    df3['Avg'] = df3['Weighted Sum'] / df3['Row Sum']
    df3['Avg Rounded'] = df3['Avg'].round(2)
    df3['Primary Instructor'] = df3['Primary Instructor'] + '\n' + '(' + df3['Avg Rounded'].astype(str) + ')'

    df3 = df3.sort_values(by=['Avg']) #, ascending=False
    print(df3)
    df3 = df3.drop(columns=['Weighted Sum', 'Row Sum', 'Avg', 'Avg Rounded'])
    print(df3)

    """ Now Build Visualization  """
    # load dataset
    #df = pd.read_csv('Matplot/stat400normal.csv')
    df = df3.copy()
    #print(df)

    """ my_colors = ['green', 'forestgreen', 'mediumseagreen', 
                'skyblue', 'lightskyblue', 'lightblue',
                'indianred', 'salmon', 'lightcoral',
                'wheat', 'moccasin', 'papayawhip',
                'dimgray', 'lightgray']
    """
    
    my_colors = ['lightgreen', 'mediumseagreen', 'forestgreen', 
                'lightblue', 'lightskyblue', 'skyblue',
                'lightcoral', 'salmon', 'indianred',
                'papayawhip', 'moccasin', 'wheat',
                'dimgray', 'lightgray']


    """ Converting it to 100% based percentages in order to get it to graph on a 0-100 graph """
    df_total = df["A+"] + df["A"] + df["A-"] + df["B+"] + df["B"] + df["B-"] + df["C+"] + df["C"] + df["C-"] + df["D+"] + df["D"] + df["D-"] + df["F"] + df["W"]
    df_rel = df[df.columns[1:]].div(df_total, 0)*100 #again, df[df.columns[1:]] is same as above, its basically the table. Then df_total is the column of the totals. I don't get the 0.
    df_rel_copy = df_rel.copy() #for some reason if you try def_rel_copy = def_rel_copy it messes up below. I think it does a deep copy for some reason
    df_rel_copy.insert(0, "Primary Instructor", df["Primary Instructor"])
    df_rel_copy = df_rel_copy.round(2) #round to 2 decimals
    print(df_rel_copy)

    df_rel_copy.plot(
        x = ('Primary Instructor'),
        kind = 'barh',
        stacked = True,
        title = course + str(tag),
        mark_right = True,
        color=my_colors,
        figsize=(30, 8),
        xlim=(-2,102))

    print(df_rel_copy)

    for n in df_rel:
        for i, (cs, ab, pc) in enumerate(zip(df_rel_copy.iloc[:, 1:].cumsum(1)[n], 
                                            df_rel_copy[n], df_rel[n])):
            #if A/B... 
            if ((n[0] == 'A' or n[0] == 'B')):
                if ((np.round(pc, 1)) > 4): #if the percent is greater than 4%, then list the letter+%         
                    plt.text(cs - ab / 2, i, n + ' ' + '(' + str(np.round(pc, 1)) + '%)', va = 'center', ha = 'center', fontsize = 7) 
                elif (((np.round(pc, 1)) > 1)): #if greater than 1%, i'll just list the letter.
                    plt.text(cs - ab / 2, i, n, va = 'center', ha = 'center', fontsize = 4.5)
            
            #if C/D/F/W , I figured noone really cares about the percent here. 
            elif (n[0] == 'C' or n[0] == 'D' or n[0] == 'F' or n[0] == 'W'):
                if ((np.round(pc, 1)) > 1.5): #Only if we have space of 1.5, then we'll just add the letter.
                    plt.text(cs - ab / 2, i, n, va = 'center', ha = 'center', fontsize = 4.5) 
            
    #plt.figure(figsize=(20,8)) WHY DOESN'T THIS WORK?
    plt.legend(loc='best', bbox_to_anchor=(0.94, -0.06), ncol=len(df.columns)) #loc='upper left'
    plt.title(course + " " + str(tag) + " GPA Spread (FA19~FA21)", fontsize=14, pad=15)
    plt.ylabel("Instructors", fontsize=10, labelpad=15)
    
    plt.subplots_adjust(bottom=0.044, left=0.136, top=0.9, right=0.6)
    plt.savefig("website/static/images/MATPLOTIMAGE", bbox_inches='tight')
    
    #plt.show()
    
    output = io.BytesIO()
    #FigureCanvas(fig).print_png(output)
    return redirect(url_for('views.mpl'))

















""" DERYAS CODE BELOW 
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
    plt.savefig("website/static/images/MATPLOTIMAGE")
    #fig = create_figure()
    #canvas = FigureCanvas(fig)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return redirect(url_for('views.mpl'))

"""

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



