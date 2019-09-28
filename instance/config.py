# Define the application directory
import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 

UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'upload/')
DATABASE = os.path.join(BASE_DIR, 'storage.db')

MAX_CONTENT_LENGTH = 1024 * 1024
# Secret key for signing cookies
# This is a secret key that is used by Flask to sign cookies.
## It’s also used by extensions like Flask-Bcrypt.
## You should define this in your instance folder to keep it out of version control.
## This should be a complex random value.
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'

STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgresql://user:TWljaGHFgiBCYXJ0b3N6a2lld2ljeiEh@localhost/databasename'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"