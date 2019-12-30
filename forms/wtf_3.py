#using flash
from flask import Flask,redirect,url_for, render_template ,flash
from flask_wtf import FlaskForm 
from wtforms import SubmitField
                    
app = Flask(__name__) 

app.config['SECRET_KEY'] = 'somekey'

class flashh(FlaskForm):
    submit = SubmitField('Click ME!')

@app.route('/', methods=['GET', 'POST'])
def flsh():
    form= flashh()
    if form.validate_on_submit():
        flash('button was clicked!')
        # flash('kill me too!')
        return redirect(url_for('flsh'))
    return render_template('flash.html',form=form)

if __name__ == "__main__":
    app.run(debug= True)