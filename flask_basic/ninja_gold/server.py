from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key ='slslslls'

@app.route('/')
def index():
	# farm, cave, house, casino
	
	if "total" in session:
		pass
	else:
		session['total'] = 0

	return render_template ('index.html')

@app.route('/process_money', methods=["POST"])
def process():
	if request.form['building'] == "farm":
		session['total'] += random.randrange(9,21) 
	if request.form['building'] == "cave":
		session['total'] += random.randrange(4,11) 
	if request.form['building'] == "house":
		session['total'] += random.randrange(1,6) 
	if request.form['building'] == "casino":
		session['total'] += random.randrange(-51,51)

	return redirect('/')

app.run(debug=True)