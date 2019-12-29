from flask import Flask, render_template 
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 

app = Flask(__name__) 

app.config['SECRET_KEY'] = 'somekey'

class info(FlaskForm):

    clas = StringField("enter class")
    submit = SubmitField('Submit')

@app.route('/',methods=['POST','GET'])
def index():
    clas = ''
    form = info()
    if form.validate_on_submit():
        clas = form.clas.data 
        form.clas.data = ''

    return render_template('index.html',form=form,clas=clas) 

if __name__ == "__main__":
      app.run(debug=1) 