from flask import Blueprint, render_template, request, jsonify

from ..controllers.conta import create_conta
from ..controllers.conta import get_conta
from ..controllers.conta import add_valor

conta = Blueprint('conta', __name__, template_folder='templates', static_folder='static')

@conta.route('/conta', methods=['POST'])
def index():
	if not request.is_json:
		return jsonify({"message": "not a json"}), 406
	
	content = request.get_json()

	created = create_conta(
		content['id'],
		content['cpf']
	)

	if created:
		return jsonify({"message": "success"}), 201
	
	return jsonify({"message": "error database"}), 507

@conta.route('/conta/adicionarSaldo', methods=['POST'])
def adicionarSaldo():
	if not request.is_json:
		return jsonify({"message": "not a json"}), 406
	
	content = request.get_json()

	conta = get_conta(id=content['conta'])

	if conta == None:
		return jsonify({"message": "conta not found"}), 404

	add_valor(conta, content['valor'])

	return jsonify({"message": "success"}), 201

@conta.route('/conta/<id>/', methods=['GET'])
def contaGet(id):
	conta = get_conta(id=id)

	if conta == None:
		return jsonify({"message": "conta not found"}), 404

	return jsonify({
		"conta": conta.id,
  		"saldo": conta.valor
	}), 200

@conta.route('/conta/<id>/', methods=['DELETE'])
def contaDelete(id):
	conta = get_conta(id=id)

	if conta == None:
		return jsonify({"message": "conta not found"}), 404

	deleted = delete_conta(conta)
	
	return jsonify({"message": "success"}), 201
