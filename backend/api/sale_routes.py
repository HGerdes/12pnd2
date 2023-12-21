from flask import Blueprint, jsonify
from flask_login import login_required
from alembicFiles.models import Sales

sale_routes = Blueprint("sales", __name__)

@sale_routes.route("/")
def sales():
  sales = Sales.query.all()
  return {"Sales": [sale.to_dict() for sale in sales]}

@sale_routes.route("/<int:id>", methods=["GET"])
def get_one_sale(id):
  sale = Sales.query.get(id)
  return {"sale": sale.to_dict()}

@sale_routes.route("/new", methods=["POST"])
def create_sale():
  try:
    new_sale=request.json
    sale = Sale(
      sale_id=new_sale["sale_id"],
      customer_id=new_sale["customer_id"],
      sale_date=new_sale["sale_date"],
      sale_amount=new_sale["sale_amount"]
    )
    db.session.add(sale)
    db.session.commit()
    return jsonify({"msg": "sale addition ok"}), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 500

