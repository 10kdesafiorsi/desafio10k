from flask import Blueprint, render_template

transferencia = Blueprint('transferencia', __name__, template_folder='templates', static_folder='static') 

@transferencia.route('/transferir', methods=['POST'])
def index():
	return 'GET tranferir'
