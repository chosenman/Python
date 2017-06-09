from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/')
def homeScreen():
	return render_template('index.html', message="Dojo Survey")

@app.route('/result', methods=['POST'])
def result():

	name = request.form['name']
	city = request.form['city']
	text = request.form['text']

	return render_template('result.html',name=name, city=city, text=text)

app.run(debug=True)