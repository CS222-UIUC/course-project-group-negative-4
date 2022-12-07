from . import db
from sqlalchemy.sql import func
from sqlalchemy.dialects.mysql import FLOAT


class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True) # , autoincrement=True
    tDept = db.Column(db.String(255))
    tSid = db.Column(db.Integer) 
    institution_name = db.Column(db.String(255))
    tFname = db.Column(db.String(255)) 
    tMiddlename = db.Column(db.String(255)) 
    tLname = db.Column(db.String(255))  
    tid = db.Column(db.Integer)  
    tNumRatings = db.Column(db.Integer) 
    rating_class = db.Column(db.String(255)) 
    contentType = db.Column(db.String(255)) 
    categoryType = db.Column(db.String(255)) 
    overall_rating = db.Column(db.FLOAT())