from flask import Blueprint, render_template, request, jsonify

extrato = Blueprint('extrato', __name__, template_folder='templates', static_folder='static')

@extrato.route('/extrato', methods=['GET'])
def index():
	return jsonify({"message": "feature not yet implemented"}), 501

@extrato.route('/extrato/<conta>', methods=['POST'])
def extratoPost(conta):	
	return jsonify({"message": "feature not yet implemented"}), 501

@extrato.route('/extrato/<conta>', methods=['DELETE'])
def extratoDelete(conta):	
	return jsonify({"message": "feature not yet implemented"}), 501
