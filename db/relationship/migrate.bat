set FLASK_APP=basics.py 
flask db init
flask db migrate -m "optional message"
flask db upgrade