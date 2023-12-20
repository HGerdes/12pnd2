from flask import Blueprint, jsonify
from flask_login import login_required
from alembicFiles.models import Customers

customer_routes = Blueprint('customers', __name__)

@customer_routes.route('/')
#@login_required
def customers():
    customers = Customers.query.all()
    return {'Customers': [customer.to_dict() for customer in customers]}

@customer_routes.route('/<int:id>')
#@login_required
def customer(id):
    customer = Customers.query.get(id)
    return customer.to_dict()
