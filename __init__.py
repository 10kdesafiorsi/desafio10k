import os

from flask import Flask

def define_config(app, config=None):
	# config/default.py      - Default values, to be used for all environments or overridden by individual environments. An example might be setting DEBUG = False in config/default.py and DEBUG = True in config/development.py.
	# config/development.py  - Values to be used during development. Here you might specify the URI of a database sitting on localhost.
	# config/production.py   - Values to be used in production. Here you might specify the URI for your database server, as opposed to the localhost database URI used for development.
	# config/staging.py      - Depending on your deployment process, you may have a staging step where you test changes to your application on a server that simulates a production environment. You’ll probably use a different database, and you may want to alter other configuration values for staging applications.

	# Load the default configuration
	app.config.from_object('config')

	# Load the configuration from the instance folder
	app.config.from_pyfile('config.py')

	# Load environment configuration
	# Load the file specified by the (FLASK_CONFIG|APP_CONFIG_FILE) environment variable
	# Variables defined here will override those in the default configuration
	if 'FLASK_CONFIG' in os.environ:
		app.config.from_envvar('FLASK_CONFIG')

	# Load app sepcified configuration
	if config is not None:
		if isinstance(config, dict):
			app.config.update(config)
		elif config.endswith('.py'):
			app.config.from_pyfile(config)
	
	return app

# Create the app and configuration
# Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

# Read the configuration file
app = define_config(app)
