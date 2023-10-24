import os
from alembicFiles.models import db
from alembicFiles.seeds import seed_commands
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harry:gerdes@localhost/twelvepnd'
# Register the custom CLI commands
app.cli.add_command(seed_commands)
db.init_app(app)

@app.route("/")
def hello_world():
  return "Hello, World"
