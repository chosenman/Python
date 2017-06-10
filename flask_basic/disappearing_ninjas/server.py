from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def homeScreen():
	return render_template('index.html', message="NO ninjas here")

@app.route('/ninja')
def ninja():
	defaultimage = 'img/tmnt.png'
	return render_template('ninja.html', message="Ninjas are here", defimage = defaultimage)

@app.route('/ninja/<ninja_color>')
def ninjacolor(ninja_color):

	# /ninja/orange - Michelangelo. michelangelo.jpeg
	# /ninja/red - Raphael	raphael-tmnt_3.png

	# granny.jpeg
	image = 'img/granny.jpeg'
	# /ninja/blue - Leonardo.  profile_leonardo.gif
	if ninja_color == 'blue':
		image = "img/profile_leonardo.gif"
	elif ninja_color == "orange":
		image = "img/michelangelo.jpeg"
	elif ninja_color == "red":
		image = "img/raphael-tmnt_3.png"
	# /ninja/purple - Donatello. donatello.jpeg
	elif ninja_color == "purple":
		image = "img/donatello.jpeg"

	print ninja_color
	return render_template("ninja.html",  defimage=image)

app.run(debug=True)