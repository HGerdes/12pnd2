from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customers(db.Model):
  __tablename__="customers"
  customer_id=db.Column(db.Integer, primary_key=True)
  first_name=db.Column(db.String(50), nullable=False)
  last_name=db.Column(db.String(50), nullable=False)
  email=db.Column(db.String(100), nullable=False)
  credit_card_token=db.Column(db.String(16), nullable=False)

  def to_dict(self):
    return {
      "customer_id": self.customer_id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "email": self.email,
      "credit_card_token": self.credit_card_token
    }
