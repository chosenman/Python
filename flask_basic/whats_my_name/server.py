from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def firstpage():
	return render_template('index.html', greeting="Hello man!")

@app.route("/process", methods=['POST'])
def process():
	print "Got Post info"

	name = request.form['name']
	print name
	
	return redirect('/')

app.run(debug=True)