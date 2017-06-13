from flask import Flask, render_template, session, redirect, request
import random, time

app = Flask(__name__)
app.secret_key ='slslslls'

@app.route('/')
def index():
	# farm, cave, house, casino
	
	if "total" in session and 'log' in session:
		pass
	else:
		session['total'] = 0
		session['log'] = []

	return render_template ('index.html')

@app.route('/process_money', methods=["POST"])
def process():
	def earn(a,b):
		number = random.randrange(a,b)
		return number

	if request.form['building'] == "reset":
		session['total'] = 0
		session['log'] = []
	elif request.form['building'] == "farm":
		earned = earn(9,21)
		session['total'] += earned

		message = "Earned " + str(earned) + " golds from the farm! (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
		session['log'].insert(0, message)

	elif request.form['building'] == "cave":
		earned = earn(4,11)
		session['total'] += earned 

		message = "Earned " + str(earned) + " golds from the cave! (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
		session['log'].insert(0, message)

	elif request.form['building'] == "house":
		earned = earn(4,11)
		session['total'] += earned

		message = "Earned " + str(earned) + " golds from the house! (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
		session['log'].insert(0, message)

	elif request.form['building'] == "casino":
		earned = earn(-51,51)
		session['total'] += earned
		if earned > 0:
			message = "Earned " + str(earned) + " golds from the CASINO! (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
		else:
			message = "Entered a casino and lost " + str(earned) + " golds... Ouch... (" + time.strftime('%Y/%d/%m %l%:%M%p') + ")"
		session['log'].insert(0, message)

	return redirect('/')


app.run(debug=True)