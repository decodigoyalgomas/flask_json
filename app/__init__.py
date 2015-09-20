# libraries import
from flask import Flask, render_template, redirect, url_for, request 
from flask_zurb_foundation import Foundation
from sqlalchemy_wrapper import SQLAlchemy



app = Flask(__name__)


# Configuration
app.config["DEBUG"] = True

from models import RandomData, db
# Initializations
foundation = Foundation(app)


# Models



# views

@app.route("/")
def index():



	data = db.query(RandomData).all()
	print(data)

	return render_template(
		"index.html",
		data=data
	)

@app.route("/save", methods=["POST"])
def save():
	# cogemos la data recibida
	received_data = request.json 
	new_random_data = RandomData(received_data)
	db.session.add(new_random_data)
	db.session.commit()
	

	return redirect(url_for("index"))

