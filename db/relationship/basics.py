# setting up
import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is the file name of current script file
# inner part gets the foldername and later returns the actua path according to current os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

Migrate(app,db)

# -------------------setup complete----------------- 


class Student(db.Model):

    __tablename__ = 'Student'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # This is a one-to-many relationship
    # A Student can have many subjects
    subjects = db.relationship('Subjects',backref='Student',lazy='dynamic')
    # This is a one-to-one relationship
    # A Student only has one mentor, thus uselist is False.
    # Strong assumption of 1 student per 1 mentor and vice versa.
    mentor = db.relationship('mentor',backref='Student',uselist=False)

    def __init__(self,name):
        # Note how a Student only needs to be initalized with a name!
        self.name = name


    def __repr__(self):
        if self.mentor:
            return f"Student name is {self.name} and mentor is {self.mentor.name}"
        else:
            return f"Student name is {self.name} and has no mentor assigned yet."

    def report_subjects(self):
        print("Here are my subjects!")
        for sub in self.subjects:
            print(sub.sub_name)
        

class Subjects(db.Model):

    __tablename__ = 'Subjects'

    id = db.Column(db.Integer,primary_key = True)
    sub_name = db.Column(db.Text)
    # Connect the sub to the Student that reads it.
    #  use Student.id because __tablename__='Student'
    Student_id = db.Column(db.Integer,db.ForeignKey('Student.id'))

    def __init__(self,sub_name,Student_id):
        self.sub_name = sub_name
        self.Student_id = Student_id


class mentor(db.Model):

    # __tablename__ = 'mentors'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    #  use Student.id because __tablename__='Student'
    Student_id = db.Column(db.Integer,db.ForeignKey('Student.id'))

    def __init__(self,name,Student_id):
        self.name = name
        self.Student_id = Student_id
