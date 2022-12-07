# from flask import Blueprint, render_template, request
# from .models import Professor
# from . import db

# # https://stackoverflow.com/questions/71541864/how-to-receive-a-row-information-from-a-html-table-to-python-flask
# # There are 2 possible solutions here

# # 1. You change your code so that you have a form in each row. 
# # This way, when you submit, you are submitting the form for 
# # just that row.

# # 2. You keep your code as is, but add Javascript code to 'intercept' 
# # your submit action. Your JS code will then determine which row 
# # you clicked, pick the value of the title in that row and manually 
# # submit the form with that value.


# # How to Turn Dictionaries into SQL Statements | Python | SQL 
# # https://www.youtube.com/watch?v=GEh6QbZjRoI


# tDept
# tSid
# institution_name
# tFname
# tMiddlename
# tLname
# tid
# tNumRatings
# rating_class
# contentType
# categoryType
# overall_rating

# new_prof = Professor(tDept=, tSid=a, institution_name=a, tFname=a, tMiddlename=a, tLname=a, tid=a, tNumRating=a, rating_class=a,
# contentType=a, categoryType=a, overall_rating=a)
#             db.session.add(new_prof)
#             db.session.commit()

#     # id = db.Column(db.Integer, primary_key=True)
#     # tDept = db.Column(db.String(255))
#     # tSid = db.Column(db.Integer) 
#     # institution_name = db.Column(db.String(255))
#     # tFname = db.Column(db.String(255)) 
#     # tMiddlename = db.Column(db.String(255)) 
#     # tLname = db.Column(db.String(255))  
#     # tid = db.Column(db.Integer)  
#     # tNumRatings = db.Column(db.Integer) 
#     # rating_class = db.Column(db.String(255)) 
#     # contentType = db.Column(db.String(255)) 
#     # categoryType = db.Column(db.String(255)) 
#     # overall_rating = db.Column(db.FLOAT())