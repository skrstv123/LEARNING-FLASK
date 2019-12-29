from dynamicRoutes import * 
from flask import render_template as rtm 

@app.route('/templates/basic')
def tmp0():
	return rtm('tmp.html')
	
@app.route('/templates/jinja')
def printvar():
	var = list('jinjavariables')
	return rtm('tmp1.html',jvar=var) #name of jinja template variables are used as a named argument 

@app.route('/templates/jinja1')
def jinjaControl():
	#<!-- a jinja flow control is kept in {% %} and it must have a {% endFLOW %} -->
	var = list(range(1,21,3))
	return rtm('tmp2.html',numList = var) 

# --------------------template inheritance----------------------
@app.route('/base')
def base():
	return rtm('base.html')
@app.route('/child/<text>')
def child(text):
	return rtm('inherited.html',text = text)

	
if __name__=='__main__':
	app.run(debug=1) 
