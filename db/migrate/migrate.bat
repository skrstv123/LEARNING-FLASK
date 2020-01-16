set FLASK_APP=mg1.py 
flask db init
flask db migrate -m "optional message"
flask db upgrade