from flask import Blueprint, render_template

conta = Blueprint('conta', __name__, template_folder='templates', static_folder='static')

@conta.route('/conta', methods=['POST'])
def index():	
	return 'POST conta'

@conta.route('/conta/adicionarSaldo', methods=['POST'])
def adicionarSaldo():	
	return 'POST adicionarSaldo'

@conta.route('/conta/<id>/', methods=['GET'])
def contaGet(id):
	return 'GET conta/{}'.format(id)

@conta.route('/conta/<id>/', methods=['DELETE'])
def contaDelete(id):
	return 'DELETE conta/{}'.format(id)
