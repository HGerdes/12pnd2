import os
from alembicFiles.models import db
from alembicFiles.seeds import seed_commands
from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

from alembicFiles.models import db, Customers, Sales
from api.auth_routes import auth_routes
from api.customer_routes import customer_routes
from api.sale_routes import sale_routes
from api.analysis_cup_routes import analysis_cup_routes

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_user(customer_id):
    return Customers.query.get(int(customer_id))

#blueprint registers
app.register_blueprint(analysis_cup_routes, url_prefix="/api/cups")
app.register_blueprint(sale_routes, url_prefix="/api/sales")
app.register_blueprint(customer_routes, url_prefix='/api/customers')
app.register_blueprint(auth_routes, url_prefix='/api/auth')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harry:gerdes@localhost/twelvepnd'
# Register the custom CLI commands
app.cli.add_command(seed_commands)
db.init_app(app)

# Application Security
CORS(app)

# Initialize CSRF Protection
csrf = CSRFProtect(app)

# Exempt auth_routes Blueprint from CSRF
csrf.exempt(auth_routes)

#ensures all requests are redirected from http to https
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')
