from flask import Blueprint, render_template, request, jsonify

from ..controllers.conta import get_conta

from ..controllers.transacao import transferir

transferencia = Blueprint('transferencia', __name__, template_folder='templates', static_folder='static') 

@transferencia.route('/transferir', methods=['POST'])
def index():
	if not request.is_json:
		return jsonify({"message": "not a json"}), 406

	content = request.get_json()

	contaOrigem = get_conta(id=content['contaOrigem'])
	contaDestino = get_conta(id=content['contaDestino'])
	
	transferencia = transferir(
		valor=content['valor'],
		origem=contaOrigem,
		destino=contaDestino
	)
	
	return jsonify({"message": "success"}), 201