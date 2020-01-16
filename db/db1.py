# setting up
import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is the file name of current script file
# inner part gets the foldername and later returns the actua path according to current os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app) 

# -------------------setup complete----------------- 

# creating tables using orm
class test(db.Model) :
    __tablename__ = 'TEST' #optional, default table name s same as class name

    #rows
    id = db.Column(db.Integer,primary_key=1) 
    name = db.Column(db.Text)
    roll = db.Column(db.Integer)

    def __init__(self,name,roll):
        self.name,self.roll=name,roll 
    def __repr__(self):
        return "id: %d, name: %s , roll: %d"%(self.id,self.name,self.roll)
    