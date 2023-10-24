from flask_sqlalchemy import SQLAlchemy
from .db import db

class AnalysisCup(db.Model):
  __tablename__ = "inv_analysis_cups"

  id = db.Column(db.Integer, primary_key=True)
  cup_type = db.Column(db.String(50), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  cost = db.Column(db.Float, nullable=False)
  price = db.Column(db.Float, nullable=False)

  def to_dict(self):
    return {
      "id": self.id,
      "cup_type": self.cup_type,
      "quantity": self.quantity,
      "cost": self.cost,
      "price": self.price
    }
