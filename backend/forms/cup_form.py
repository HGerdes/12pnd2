from flask_wtf import FlaskForm
from wtforms.fields import (DecimalField, IntegerField)
from wtforms.validators import DataRequired, Length
from alembicFiles.models import AnalysisCup

class EditAnalysisCupForm(FlaskForm):
  quantity = IntegerField("quantity", validators=[DataRequired()])
  cost = DecimalField("cost", validators=[DataRequired()])
  price = DecimalField("price", validators=[DataRequired()])
