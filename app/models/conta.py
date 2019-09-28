from . import db

class Conta(db.Model):
	__tablename__ = "conta"
	
	id = db.Column(db.Integer, primary_key=True)
	cpf = db.Column(db.String, unique=True, nullable=False)
	valor = db.Column(db.Float, nullable=False)

	def __init__(self, id, cpf):
		self.id = id
		self.cpf = cpf

	def __repr__(self):
		return "<Conta %r>" % self.cpf