from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from .db import db

class IndCupSale(db.Model):
  __tablename__= "ind_cup_sale"

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  cust_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
  sale_id = db.Column(db.Integer, db.ForeignKey("sales.sale_id"), nullable=False)
  cup_id = db.Column(db.Integer, db.ForeignKey("inv_analysis_cups.id"), nullable=False)
  sale_date = db.Column(db.Date, nullable=False)
  price_at_purchase = db.Column(db.Float, nullable=False)
  quantity = db.Column(db.Integer, nullable=False)

  customers = db.relationship("Customers", back_populates="ind_cup_sale")
  sales = db.relationship("Sales", back_populates="ind_cup_sale")
  inv_analysis_cups = db.relationship("AnalysisCup", back_populates="ind_cup_sale")

  def to_dict(self):
    return {
      "id": self.id,
      "cust_id": self.cust_id,
      "sale_id": self.sale_id,
      "cup_id": self.cup_id,
      "sale_date": self.sale_date,
      "price_at_purchase": self.price_at_purchase,
      "quantity":self.quantity
    }
