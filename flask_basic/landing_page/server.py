# session - for work with cookies
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():

	return render_template('index.html', phrase="Hello stranger!")

@app.route('/ninjas')
def ninjas():

	return render_template('ninjas.html', phrase="Ninja page!")

@app.route('/dojos/new')
def dojo():
	return redirect('/')


app.run(debug=True)