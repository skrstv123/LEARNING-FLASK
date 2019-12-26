from links import *
from flask import request as rq

@app.route('/home')
def home():
	return rtm('home.html')

@app.route('/form')
def form():
	return rtm('form.html')

@app.route('/thanks')
def thanks():
	na = rq.args.get('name')
	ag = rq.args.get('age')

	return rtm('thank.html',name=na,age=int(ag))

@app.errorhandler(404)
def p404(e):
	return rtm('404.html'),404

if __name__=='__main__':
	app.run(debug=1) 
