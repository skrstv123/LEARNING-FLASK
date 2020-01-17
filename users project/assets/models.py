from assets import db,login_manager 
from werkzeug.security import generate_password_hash,check_password_hash 
from flask_login import UserMixin 
 
@login_manager.user_loader
def load_user(user_id): return user.query.get(user_id)

class user(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=1)
    name  = db.Column(db.String(64))
    mail = db.Column(db.String(64),unique=1,index=1)
    username = db.Column(db.String(64),unique=1,index=1)
    pass_hash = db.Column(db.String(128))

    def __init__(self, name, mail, username,pwd):
        self.name = name
        self.mail = mail
        self.username = username 
        self.pass_hash = generate_password_hash(pwd) 
    def check_pass(self,pwd):
        return check_password_hash(self.pass_hash,pwd) 

    
class posts(db.Model):
    __tablename__ = 'posts' 
    id = db.Column(db.Integer,primary_key=1)
    text = db.Column(db.String(64))
    
    