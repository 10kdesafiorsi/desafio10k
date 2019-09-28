from . import db

class Usuario(db.Model):
	__tablename__ = "usuario"
	
	id = db.Column(db.Integer, primary_key=True)

	# User datas
	cpf = db.Column(db.Integer, unique=True, nullable=False)
	nome = db.Column(db.String, nullable=False)
	sobrenome = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	# ToDo: DateTime
	dataNascimento = db.Column(db.String, nullable=False)

	# ToDo: Create other tables (Auth)
	password = db.Column(db.String, nullable=False)

	# ToDo: Create other tables (Address)
	pais = db.Column(db.String, nullable=False)
	estado = db.Column(db.String, nullable=False)
	cidade = db.Column(db.String, nullable=False)
	bairro = db.Column(db.String, nullable=False)
	rua = db.Column(db.String,  nullable=False)
	numero = db.Column(db.Integer, nullable=False)
	complemento = db.Column(db.String)

	# ToDo
	def __init__(self, id, cpf, nome, sobrenome, email, dataNascimento, password, pais, estado, cidade, bairro, rua, numero, complemento):
		self.id = id
		self.cpf = cpf
		self.nome = nome
		self.sobrenome = sobrenome
		self.email = email
		self.dataNascimento = dataNascimento
		self.password = password
		self.pais = pais
		self.estado = estado
		self.cidade = cidade
		self.bairro = bairro
		self.rua = rua
		self.numero = numero
		self.complemento = complemento

	def __repr__(self):
		return "<Usuario %r>" % self.cpf