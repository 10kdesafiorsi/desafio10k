from flask import Blueprint, render_template, request, jsonify

from ..controllers.usuario import create_usuario
from ..controllers.usuario import get_usuario
from ..controllers.usuario import update_usuario

usuario = Blueprint('usuario', __name__, template_folder='templates', static_folder='static')

@usuario.route('/usuario', methods=['POST'])
def index():
	if not request.is_json:
		return jsonify({"message": "not a json"}), 406

	content = request.get_json()
	
	created = create_usuario(
		content['cpf'],
		content['nome'],
		content['sobrenome'],
		content['email'],
		content['dataNascimento'],
		content['password'],
		content['pais'],
		content['estado'],
		content['cidade'],
		content['bairro'],
		content['rua'],
		content['numero'],
		content['complemento']
	)
	
	if created:
		return jsonify({"message": "success"}), 201
	
	return jsonify({"message": "error database"}), 507

@usuario.route('/usuario', methods=['PUT'])
def usuarioPut():
	if not request.is_json:
		return jsonify({"message": "not a json"}), 406
	
	content = request.get_json()
	
	usuario = get_usuario(cpf=content['cpf'])
	
	if usuario == None:
		return jsonify({"message": "usuario not found"}), 404

	updated = update_usuario(usuario,
		cpf=content['cpf'],
		nome=content['nome'],
		sobrenome=content['sobrenome'],
		email=content['email'],
		dataNascimento=content['dataNascimento'],
		password=content['password'],
		pais=content['pais'],
		estado=content['estado'],
		cidade=content['cidade'],
		bairro=content['bairro'],
		rua=content['rua'],
		numero=content['numero'],
		complemento=content['complemento']
	)

	if updated:
		return jsonify({"message": "success"}), 201
	
	return jsonify({"message": "error database"}), 507

@usuario.route('/usuario/<cpf>', methods=['GET'])
def usuarioGet(cpf):	
	usuario = get_usuario(cpf=cpf)

	if usuario == None:
		return jsonify({"message": "user not found"}), 404

	return jsonify(usuario), 200

@usuario.route('/usuario/<cpf>', methods=['DELETE'])
def usuarioDelete(cpf):	
	usuario = get_usuario(cpf=cpf)

	if usuario == None:
		return jsonify({"message": "user not found"}), 404

	deleted = delete_usuario(usuario)

	if updated:
		return jsonify({"message": "success"}), 201
	
	return jsonify({"message": "error database"}), 507


