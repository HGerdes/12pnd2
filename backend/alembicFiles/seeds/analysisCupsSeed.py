from ..models import db, AnalysisCup
from sqlalchemy import text

def seed_analysis_cups():
  cup1 = AnalysisCup(id=1, cup_type="12-panel", quantity="30000", cost=1.25, price=2)
  cup2 = AnalysisCup(id=2, cup_type="13-panel", quantity="20000", cost=1.50, price=2.5)
  cup3 = AnalysisCup(id=3, cup_type="14-panel", quantity="25000", cost=1.75, price=2.75)
  cup4 = AnalysisCup(id=4, cup_type="18-panel", quantity="7000", cost=2.00, price=3)
  cup5 = AnalysisCup(id=5, cup_type="2-panel", quantity="4000", cost=0.25, price=0.25)
  cup6 = AnalysisCup(id=6, cup_type="9-panel", quantity="50000", cost=1.25, price=1)

  db.session.add(cup1)
  db.session.add(cup2)
  db.session.add(cup3)
  db.session.add(cup4)
  db.session.add(cup5)
  db.session.add(cup6)
  db.session.commit()

def undo_cups():
  db.session.execute(text("TRUNCATE inv_analysis_cups RESTART IDENTITY CASCADE;"))
  db.session.commit()
