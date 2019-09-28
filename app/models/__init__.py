from flask_sqlalchemy import SQLAlchemy

# Connect to database with sqlalchemy.
db = SQLAlchemy()

# Define models
from .usuario import Usuario