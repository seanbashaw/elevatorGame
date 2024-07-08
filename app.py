from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/clearCookies')
def clearCookies():
	resp = make_response("Cookies are clearred")	
	resp.set_cookie('shrimpMood','')
	resp.set_cookie('journalCode','')
	return resp

@app.route('/journal')
def journal():
	code = request.args.get("passCode")
	return render_template("journal.html",passCode=code)
@app.route('/shrimp')
def shrimp():
	resp = make_response("Praising the shrimp")
	words = request.args.get("shrimpTalk")
	if 'rutabaga' in words.lower():
		resp.set_cookie('shrimpMood','praised')
	else:
		resp.set_cookie('shrimpMood','unamused')
	return render_template('floor2.html',praise=request.cookies.get('shrimpMood'))
@app.route('/elevator')
def elevator():
	floor = request.args.get("floor")
	lest = range(1,10)
	if floor:
		if int(floor)==1:
			return index()
		elif int(floor)==2:
			return render_template('floor2.html',praise=request.cookies.get('shrimpMood'))
		elif int(floor)==3:
			code = request.args.get("passCode")
			return render_template('journal.html',passCode=code)
		elif int(floor)==6:
			return 
		elif int(floor)==9:
			return render_template('roof.html',praise=request.cookies.get('shrimpMood'))
		elif int(floor)<=9:
			return render_template('elevator.html',magic=lest,floorName=floor)
	return render_template('elevator.html',magic=lest)

def floor_1():
	return render_template('floor1.html')