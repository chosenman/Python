from flask import Flask, request, render_template, redirect, flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def homeScreen():
	return render_template('index.html', message="Dojo Survey")

@app.route('/result', methods=['POST'])
def result():


	name = request.form['name']
	city = request.form['city']
	flanguage = request.form['flanguage']
	text = request.form['text']

	if len(flanguage) < 1 or len(name) < 1 or len(city) < 1 or len(text) < 1:
		flash("Don't leave field(s) cannot be empty!")
		return redirect('/')
	elif len(text) > 120:
		flash("Comment should not be longer than 120 characters!")
		return redirect('/')

	return render_template('result.html',name=name, city=city, text=text, flanguage=flanguage)

app.run(debug=True)