import uuid

from ..models import db

from ..models.conta import Conta

def transferir(valor, origem, destino):
	if origem.valor < valor:
		return False
	
	origem.valor = origem.valor - valor
	destino.valor = destino.valor + valor
	
	return db.session.commit()