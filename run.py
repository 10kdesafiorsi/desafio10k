import os

# Import application
from app import app
# Import module routes/viwes
from app import routes
# Import module database
from app.models import db

# Define routes/viwes
app = routes.init_app(app)

# Define database
db.init_app(app)

# Run a server.
if __name__ == "__main__":
	app.run(
		host=os.environ.get('FLASK_CONFIG_HTTP_HOST', '0.0.0.0'),
		port=int(os.environ.get('FLASK_CONFIG_HTTP_PORT', '8080')),
		threaded=False,
		debug=True
	)