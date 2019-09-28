import uuid

from ..models import db

from ..models.usuario import Usuario

def create_usuario(cpf, nome, sobrenome, email, dataNascimento, password, pais, estado, cidade, bairro, rua, numero, complemento):
	id = str(uuid.uuid4())

	#ToDo: Valid fields
	usuario = Usuario(id, cpf, nome, sobrenome, email, dataNascimento, password, pais, estado, cidade, bairro, rua, numero, complemento)
	
	db.session.add(usuario)
	db.session.commit()
	
	return True

def get_usuario(id=None, cpf=None):
	if id != None:
		return Usuario.query.filter_by(id=id).first()
	elif cpf != None:
		return Usuario.query.filter_by(cpf=cpf).first()

	return None

# ToDo
def update_usuario(usuario, cpf=None, nome=None, sobrenome=None, email=None, dataNascimento=None, password=None, pais=None, estado=None, cidade=None, bairro=None, rua=None, numero=None, complemento=None):
	usuario.cpf = cpf

	return db.session.commit()