#using sessions
from flask import Flask, render_template ,session, redirect, url_for
from flask_wtf import FlaskForm 
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextAreaField ,TextField)
from wtforms.validators import DataRequired

app = Flask(__name__) 

app.config['SECRET_KEY'] = 'somekey'

class Form(FlaskForm):
    name = StringField('SOme label that can be accessed using fiels.label syntax', validators=[DataRequired()])
    Age = BooleanField('18 or above?')
    major=SelectField('CHoices', choices=[('ph','PHYSICS'),
    ('cse','CSE'), ('mt','maths')]) 
    #value , label

    gen = RadioField('enter gender', choices= [('m','male'),('f','female')])
    #value , label
    feedback=TextAreaField()
    submit= SubmitField()


@app.route('/',methods=['GET','POST'])
def index():
    form = Form() 
    if form.validate_on_submit():
        session['name']=form.name.data
        session['age']=form.Age.data 
        session['major']=form.major.data 
        session['gen']=form.gen.data 
        session['fb']=form.feedback.data

        return redirect(url_for('confirm')) #no need to send the session variable
    return render_template('index1.html',form= form)

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

if __name__ == "__main__":
    app.run(debug=1)