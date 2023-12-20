from ..models import db, IndCupSale
from datetime import date
from sqlalchemy import text

def seed_ind_sales():
  indSale1 = IndCupSale(id=1, cust_id=1, cup_id=2, sale_date=date(2022, 3, 4), price_at_purchase=2.5, quantity=120)
  indSale2 = IndCupSale(id=2, cust_id=3, cup_id=4, sale_date=date(2022, 5, 3), price_at_purchase=3, quantity=666)
  indSale3 = IndCupSale(id=3, cust_id=5, cup_id=3, sale_date=date(2022, 12, 30), price_at_purchase=2.75, quantity=165)
  indSale4 = IndCupSale(id=4, cust_id=5, cup_id=1, sale_date=date(2023, 2, 5), price_at_purchase=2, quantity=198)
  indSale5 = IndCupSale(id=5, cust_id=4, cup_id=5, sale_date=date(2023, 3, 2), price_at_purchase=3, quantity=198)
  indSale6 = IndCupSale(id=6, cust_id=7, cup_id=6, sale_date=date(2023, 4, 1), price_at_purchase=1.75, quantity=210)
  indSale7 = IndCupSale(id=7, cust_id=2, cup_id=5, sale_date=date(2023, 4, 4), price_at_purchase=3, quantity=3)
  indSale8 = IndCupSale(id=8, cust_id=8, cup_id=1, sale_date=date(2023, 5, 10), price_at_purchase=2, quantity=20320)

  db.session.add(indSale1)
  db.session.add(indSale2)
  db.session.add(indSale3)
  db.session.add(indSale4)
  db.session.add(indSale5)
  db.session.add(indSale6)
  db.session.add(indSale7)
  db.session.add(indSale8)
  db.session.commit()
  
def undo_ind_sales():
  db.session.execute(text("TRUNCATE sales RESTART IDENTITY CASCADE;"))
  db.session.commit()
