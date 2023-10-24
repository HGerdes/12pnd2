from ..models import db, Customers
from sqlalchemy import text

def seed_customers():
  customer1 = Customers(customer_id=1, first_name="Monica", last_name="Moistpants", email="mm@moistpants.net", credit_card_token="4444333322221111")
  customer1.set_password("password")
  customer2 = Customers(customer_id=2, first_name="Al", last_name="Capone", email="ac@bootleggers.com", credit_card_token="1234567891236456")
  customer2.set_password("password")
  customer3 = Customers(customer_id=3, first_name="Johnny", last_name="Thundercock", email="alexcameupwiththisone@thunder.cok", credit_card_token="7854231854652315")
  customer3.set_password("password")
  customer4 = Customers(customer_id=4, first_name="Manuella", last_name="Consuela", email="mc@hammer.com", credit_card_token="5689547123654754")
  customer4.set_password("password")
  customer5 = Customers(customer_id=5, first_name="Princess", last_name="Diana", email="pd@insidejob.net", credit_card_token="4678453235674234")
  customer5.set_password("password")
  customer6 = Customers(customer_id=6, first_name="John", last_name="Kennedy", email="jk@headache.org", credit_card_token="1029384775610293")
  customer6.set_password("password")
  customer7 = Customers(customer_id=7, first_name="Mr", last_name="Rue", email="rue@bestcatever.rue", credit_card_token="5647382910293847")
  customer7.set_password("password")
  customer8 = Customers(customer_id=8, first_name="Beef", last_name="McSweat", email="bm@gross.net", credit_card_token="4839201948596054")
  customer8.set_password("password")

  db.session.add(customer1)
  db.session.add(customer2)
  db.session.add(customer3)
  db.session.add(customer4)
  db.session.add(customer5)
  db.session.add(customer6)
  db.session.add(customer7)
  db.session.add(customer8)
  db.session.commit()

def undo_customers():
  db.session.execute(text("TRUNCATE customers RESTART IDENTITY CASCADE;"))
  db.session.commit()
