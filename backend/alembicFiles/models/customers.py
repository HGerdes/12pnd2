from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from .db import db


class Customers(db.Model, UserMixin):
  __tablename__="customers"
  customer_id=db.Column(db.Integer, primary_key=True)
  first_name=db.Column(db.String(50), nullable=False)
  last_name=db.Column(db.String(50), nullable=False)
  email=db.Column(db.String(100), nullable=False)
  credit_card_token=db.Column(db.String(16), nullable=False)
  hashed_password=db.Column(db.String(255), nullable=False)

  sales = db.relationship("Sales", back_populates="customers")

  def set_password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def to_dict(self):
    return {
      "customer_id": self.customer_id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "email": self.email,
    }
