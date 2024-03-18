# API CREATION 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# initialize flask application
app = Flask(__name__)
CORS(app)   # addresses the cors error

app.config["SQLALCHEMY_DATBASE_URI"] = "sqlite:///mydatabase.db"    # a file, sql database object
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False    # not tracking our changes for development purposes

db = SQLAlchemy(app)    # creates db instance