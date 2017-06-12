from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key ='slslslls'

@app.route('/')
def index():
	if 'randomnumber' in session:
		pass
	else:
		session['randomnumber'] = random.randrange(1,101)
	if 'answer' in session:
		pass
	else:
		session['answer'] = ""
	# session.pop('randomnumber')
	return render_template ('index.html')

@app.route('/process', methods=['POST'])
def process():
	print "div " + session['div']
	print session['randomnumber']

	# RESET LOGIC
	if request.form['action'] == "reset":
		session['div'] = ''
		session['randomnumber'] = random.randrange(1,101)
		session['answer'] = ""

	# GUESS LOGIC
	elif request.form['guess'] == '':
		session['answer'] = 'input number pls!'
		session['div'] = 'low'
	elif int(request.form['guess']) == session['randomnumber'] and request.form['action'] == "takeguess":
		session['answer'] = 'How did you know! Awesome it really was ' + str(session['randomnumber'])
		del session['randomnumber']
		session['div'] = 'green'
	elif int(request.form['guess']) < session['randomnumber']  and request.form['action'] == "takeguess":
		session['answer'] = 'too low!'
		session['div'] = 'low'
	elif int(request.form['guess']) > session['randomnumber'] and request.form['action'] == "takeguess":
		session['answer'] = 'too high!'
		session['div'] = 'low'



	return redirect('/')

app.run(debug=True)