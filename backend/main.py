from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harry:gerdes@localhost/twelvepnd'
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
  return "Hello, World"
