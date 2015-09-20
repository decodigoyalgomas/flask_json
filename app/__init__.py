# libraries import
from flask import Flask, render_template, redirect, url_for, request 
from flask_zurb_foundation import Foundation
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


# Configuration
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db" #'postgres://localhost/random'

# Initializations
foundation = Foundation(app)
db = SQLAlchemy(app)
db.create_all()

# Models


from sqlalchemy.dialects.postgresql import JSON

class RandomData(db.Model):
	__tablename__ = "random"

	id = db.Column(db.Integer, primary_key=True)
	random_data = db.Column(JSON)

	def __init__(self, json_data):
		self.random_data = json_data
# views

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
	# cogemos la data recibida
	received_data = request.json 
	new_random_data = RandomData(received_data)
	db.session.add(new_random_data)
	db.session.commit()

	return redirect(url_for("index"))



if __name__ == '__main__':
	app.run()