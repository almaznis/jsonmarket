# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

username = 'almaz'
password = 'jsonmarket2024!'
host = '35.226.29.185'  # Public IP address of your Google Cloud SQL instance
port = '5432'
database = 'postgres'  # Default database name; change if you have a different one

# Forming the database URL
db_url = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'


SQLALCHEMY_DATABASE_URI = db_url


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Configure to use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes
