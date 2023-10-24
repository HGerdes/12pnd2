from ..models import db, Sales
from sqlalchemy import text
from datetime import date

def seed_sales():
  sale1 = Sales(sale_id=1, customer_id=1, sale_date=date(2022, 3, 4), sale_amount="300")
  sale2 = Sales(sale_id=2, customer_id=3, sale_date=date(2022, 5, 3), sale_amount="2000")
  sale3 = Sales(sale_id=3, customer_id=5, sale_date=date(2022, 12, 30), sale_amount="454.50")
  sale4 = Sales(sale_id=4, customer_id=5, sale_date=date(2023, 2, 5), sale_amount="390.25")
  sale5 = Sales(sale_id=5, customer_id=4, sale_date=date(2023, 3, 2), sale_amount="594.50")
  sale6 = Sales(sale_id=6, customer_id=7, sale_date=date(2023, 4, 1), sale_amount="420.69")
  sale7 = Sales(sale_id=7, customer_id=2, sale_date=date(2023, 4, 4), sale_amount="10.25")
  sale8 = Sales(sale_id=8, customer_id=8, sale_date=date(2023, 5, 10), sale_amount="40540.25")

  db.session.add(sale1)
  db.session.add(sale2)
  db.session.add(sale3)
  db.session.add(sale4)
  db.session.add(sale5)
  db.session.add(sale6)
  db.session.add(sale7)
  db.session.add(sale8)
  db.session.commit()

def undo_sales():
  db.session.execute(text("TRUNCATE sales RESTART IDENTITY CASCADE;"))
  db.session.commit()
