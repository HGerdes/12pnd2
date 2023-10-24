from flask.cli import AppGroup
from .analysisCupsSeed import seed_analysis_cups, undo_cups
from .customersSeed import seed_customers, undo_customers
from .salesSeed import seed_sales, undo_sales

seed_commands = AppGroup("seed")

@seed_commands.command("all")
def seed():
  seed_analysis_cups()
  seed_customers()
  seed_sales()

@seed_commands.command("undo")
def undo():
  undo_cups()
  undo_customers()
  undo_sales()
