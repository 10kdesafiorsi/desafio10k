from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static') 

@auth.route('/usuario/login', methods=['POST'])
def index():
	return 'POST login'

@auth.route('/usuario/logout', methods=['GET'])
def authLogout():
	return 'GET logout'
