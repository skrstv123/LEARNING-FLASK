from flask_wtf import FlaskForm 
from wtforms.validators import DataRequired,Email,EqualTo 
from wtforms import StringField,PasswordField,SubmitField 
from wtforms import ValidationError
from assets.models import user, posts 

class reg(FlaskForm):
    name = StringField('Name',validators = [DataRequired()]) 
    mail = StringField('Mail',validators = [DataRequired(),Email()]) 
    uname = StringField('UserName',validators = [DataRequired()]) 
    pwd = PasswordField('Password',validators = [DataRequired(),EqualTo('pwd_2')]) 
    pwd_2 = PasswordField('Password',validators = [DataRequired()]) 

    def checkMail(self,field):
        if user.query.filter_by(mail=  field.data).first():
            raise ValidationError('Email already registered!')

    def checkUser(self,field):
        if user.query.filter_by(username=  field.data).first():
            raise ValidationError('Username already taken!')

class login(FlaskForm):
    mail = StringField('Mail',validators = [DataRequired(),Email()]) 
    uname = StringField('UserName',validators = [DataRequired()]) 
    pwd = PasswordField('Password',validators = [DataRequired()]) 

class delPost(FlaskForm):
    DEL = SubmitField('DELETE')
    def __init__(slef, post):
        slef.id = post.id