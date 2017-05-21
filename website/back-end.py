from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/ordernow')
def ordernow():
	return render_template('ordernow.html')

if __name__ == '__main__':
	app.run(debug=True)
