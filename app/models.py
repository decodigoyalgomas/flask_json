from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy_wrapper import SQLAlchemy


db = SQLAlchemy('postgresql://127.0.0.1/random', echo=True)

class RandomData(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	random_data = db.Column(JSON)

	def pprint(self):
		"""
		Desempaca el key y el value para poder imprimirlos bien
		"""
		full_data = {}
		print(self.random_data.items())
		for item in self.random_data.items():

			key, value = item
			full_data[key] = value
		return full_data

	def __init__(self, json_data):
		self.random_data = json_data

	def __repr__(self):
		return "{}".format(self.random_data)


db.create_all()