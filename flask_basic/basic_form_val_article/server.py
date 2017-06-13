from flask import Flask, render_template, redirect, request, session, flash
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!") # just pass a string to the flash function
  # elif request.form['name'].isalpha() != true:
  # 	flash("Enter please alphabetical characters!")
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid Email Address!")
  else:
    flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
  return redirect('/') # either way the application should return to the index and display the message


app.run(debug=True)