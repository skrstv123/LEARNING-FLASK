from helloworld import *
@app.route('/dr/<var>') #angular brackets contain the variable we need (?!)
def dynamic(var):
	return boot+"<h1>this page was created dynamically for <i>"+var+"</i> as according to the variable passed through the url</h1>?"

if __name__=='__main__':
	app.run(debug=1) #debugger cli key is in the o/p in command line