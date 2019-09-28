from .auth import auth
from .conta import conta
from .extrato import extrato
from .transferencia import transferencia
from .usuario import usuario

from .home import home
#from .profile import profile

def init_app(app):
	app.register_blueprint(auth)
	app.register_blueprint(conta)
	app.register_blueprint(extrato)
	app.register_blueprint(transferencia)
	app.register_blueprint(usuario)

	app.register_blueprint(home)
	#app.register_blueprint(profile)
	
	return app