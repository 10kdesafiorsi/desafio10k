from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static') 

@auth.route('/usuario/login', methods=['POST'])
def index():
	return jsonify({"message": "feature not yet implemented"}), 501

@auth.route('/usuario/logout', methods=['GET'])
def authLogout():
	return jsonify({"message": "feature not yet implemented"}), 501
