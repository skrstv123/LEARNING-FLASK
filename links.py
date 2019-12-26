# url_for func is used to create links
from templates import *

@app.route('/links')
def link():
	return rtm('link.html')

if __name__=='__main__':
	app.run(debug=1) 
