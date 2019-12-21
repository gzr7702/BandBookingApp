import os
from info import credentials

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

usr = credentials['usr']
pwd = credentials['pwd']

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://" + usr + ":" + pwd + "@localhost:5432/banddb"
