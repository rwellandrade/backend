from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])


class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    available_qty = IntegerField('available_qty', validators=[DataRequired()])

