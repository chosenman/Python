from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/users_form', methods=['POST'])
def create_user():
	print "Got Post Info"
	print request.form

	name = request.form['name']
	email = request.form['email']

	return render_template('success.html')

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
	print username
	print id
	return render_template("user.html")


app.run(debug=True) # run our server
