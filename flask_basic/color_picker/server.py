from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key ='slslslls'

@app.route('/')
def homeScreen():
	if 'red' in session and 'green' in session and 'blue' in session:
		pass
	else:
		session['red'] = 255
		session['green'] = 255
		session['blue'] = 255

	return render_template('index.html', message="Enter your color values below:", red=session['red'], green=session['green'], blue=session['blue'])

@app.route('/process', methods=['POST'])
def result():

	session['red'] = request.form['red']
	session['green'] = request.form['green']
	session['blue'] = request.form['blue']


	return redirect('/')




app.run(debug=True)