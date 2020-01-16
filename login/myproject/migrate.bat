set FLASK_APP=app.py 
flask db init
flask db migrate -m "optional message"
flask db upgrade