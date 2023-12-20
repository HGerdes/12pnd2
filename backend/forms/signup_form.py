from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from alembicFiles.models import Customers

def customer_exists(form, field):
    # Checking if email exists
    email = field.data
    customer = Customers.query.filter(Customers.email == email).first()
    if customer:
        raise ValidationError('Email address is already in use.')

class SignUpForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), customer_exists, Email()])
    password = PasswordField('password', validators=[DataRequired()])
