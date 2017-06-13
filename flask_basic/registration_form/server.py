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

	email = request.form['email']
	fname = request.form['fname']
	lname = request.form['lname']
	password = request.form['password']
	repasword = request.form['repassword']

	if len(email) < 1 or len(fname) < 1 or len(lname) < 1 or len(password) < 1 or len(repasword) < 1:
		flash("All fields are required!", "error")
		return redirect('/')
	elif password != repasword:
		flash("Passwords don't match !", "error")
		return redirect('/')
	elif len(password) <8:
		flash("Password can't be lower than 8 characters!", "error")
		return redirect('/')
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!", "error")
		return redirect('/')
	elif lname.isalpha() == False or lname.isalpha() == False:
		flash("Name and Last name should be alphabetical!", "error")
		return redirect('/')
	else:
		flash("Thanks for submitting your information", "success")
		return redirect('/')

	# return render_template('result.html',email=email, fname=fname, lname=lname)

app.run(debug=True)