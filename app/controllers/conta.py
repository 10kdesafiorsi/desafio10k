from ..models import db

from ..models.conta import Conta

def create_conta(id, cpf):
	conta = Conta(id, cpf)
	
	db.session.add(conta)
	db.session.commit()
	
	return True

def get_conta(id=None):
	return Conta.query.filter_by(id=id).first()

def add_valor(conta, valor):
	if conta.valor == None or conta.valor <= 0:
		conta.valor = valor
	else:
		conta.valor = conta.valor + valor

	return db.session.commit()

def delete_conta(conta):
	db.session.delete(conta)

	return db.session.commit()