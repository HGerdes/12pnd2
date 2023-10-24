from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sales(db.Model):
  __tablename__ = "sales"

  sale_id = db.Column(db.Integer, primary_key=True)
  customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"), nullable=False)
  sale_date = db.Column(db.Date, nullable=False)
  sale_amount = db.Column(db.Integer, nullable=False)

  def to_dict(self):
    return {
      "sale_id": self.sale_id,
      "customer_id": self.customer_id,
      "sale_date": self.sale_date,
      "sale_amount": self.sale_amount
    }
