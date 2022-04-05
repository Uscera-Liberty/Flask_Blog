from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://Users//admin//Downloads//Cats_Blog(flask)//database.db'

from app import views