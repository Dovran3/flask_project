from main import db


class Info(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(50), nullable=False)
	comment = db.Column(db.String(120), nullable=False)

	def __repr__(self):
		return f"The id number is: {self.id}"