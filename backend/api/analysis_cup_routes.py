from flask import Blueprint, jsonify
from flask_login import login_required
from alembicFiles.models import AnalysisCup

analysis_cup_routes = Blueprint("inv_analysis_cups", __name__)

@analysis_cup_routes.route("/")
def cups():
  cups = AnalysisCup.query.all()
  return {"AnalysisCup": [cup.to_dict() for cup in cups]}

@analysis_cup_routes.route("/<int:id>", methods=["GET"])
def get_one_cup(id):
  cup = AnalysisCup.query.get(id)
  return {"cup": cup.to_dict()}

@analysis_cup_routes.route("/new", methods=["POST"])
def create_cup():
  try:
    new_cup = request.json
    cup = AnalysisCup(
      cup_type = new_cup["cup_type"].
      quantity = new_cup["quantity"],
      cost = new_cup["cost"],
      price = new_cup["price"]
    )
    db.session.add(cup)
    db.session.commit()
    return jsonify({"msg": "cup addition ok"}), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@analysis_cup_routes.route("/<int:id>", methods=["PATCH"])
def update_cup(id):
  cup = AnalysisCup.query.get(id)
  form = EditCupForm()
  form["csrf_token"].data = request.cookies["csrf_token"]
  if form.validate_on_submit():
    cup.cup_type = form.data["cup"]
    db.session.commit()
    return cup.to_dict()
  return jsonify(form.errors), 400
