from flask import Blueprint, render_template

extrato = Blueprint('extrato', __name__, template_folder='templates', static_folder='static')

@extrato.route('/extrato', methods=['GET'])
def index():	
	return 'GET extrato'

@extrato.route('/extrato/<conta>', methods=['POST'])
def extratoPost(conta):	
	return 'POST extrato'

@extrato.route('/extrato/<conta>', methods=['DELETE'])
def extratoDelete(conta):	
	return 'DELETE extrato'
