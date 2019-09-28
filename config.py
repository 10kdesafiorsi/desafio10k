# Statement for enabling the development environment
# Gives you some handy tools for debugging errors.
## This includes a web-based stack trace and interactive Python console for errors.
## Should be set to True in development and False in production.
DEBUG = False

# For use in application emails
MAIL_FROM_EMAIL = "default@app.com" 

SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Configuration for the Flask-Bcrypt extension
## If you’re using Flask-Bcrypt to hash user passwords.
## you’ll need to specify the number of “rounds” that the algorithm executes in hashing a password.
## If you aren’t using Flask-Bcrypt, you should probably start.
## The more rounds used to hash a password, the longer it’ll take for an attacker to guess a password given the hash.
## The number of rounds should increase over time as computing power increases.
## Later in this book we’ll cover some of the best practices for using Bcrypt in your Flask application.
BCRYPT_LOG_ROUNDS = 12

FLASKY_ADMIN = 'root@gmail.com'