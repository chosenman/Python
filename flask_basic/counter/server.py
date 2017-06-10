# session - for work with cookies
from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key ='slslslls'

@app.route('/')
def index():

	if 'count' in session:
		session['count'] +=1
	else:
		session['count'] = 0
	return render_template('index.html', phrase="Counter", times=5, count = session['count'])

@app.route('/two')
def two():
	if 'count' in session:
		session['count'] +=1
	else:
		session['count'] = 0

	return redirect('/')

@app.route('/reset')
def reset():
	session['count'] = 0
	return redirect('/')


app.run(debug=True)