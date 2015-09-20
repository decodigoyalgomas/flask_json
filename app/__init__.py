# coding: utf-8
# libraries import
import json
from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
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
	


	return render_template(
		"index.html",
		data=data
	)

@app.route("/save", methods=["POST"])
def save():
	# cogemos la data recibida
	
	returned_data = {}
	received_data = request.json 
	try:
		new_random_data = RandomData(received_data)
		db.session.add(new_random_data)
		db.session.commit()
		returned_data["message"] = "Se Creó una nueva data aleatoria"
		returned_data["data"] = received_data
		returned_data["status"] = "success"
	except Exception as e:
		returned_data["message"] = "Hubo un error"
		returned_data["error"] = e
		returned_data["status"]= "alert"


	return jsonify(returned_data)

