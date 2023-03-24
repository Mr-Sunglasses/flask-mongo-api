from flask import Flask
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

db = PyMongo(app)

bcrypt = Bcrypt(app)

from users import routes