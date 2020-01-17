from assets import app,db 
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user,login_required, logout_user 
from assets.models import user,posts 
from assets.forms import login,reg,delPost 

@app.route('/')
def home(): return render_template('home.html')

if __name__ == "__main__":
    app.run(debug= 1)
