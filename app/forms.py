from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])


class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    available_qty = DecimalField('available_qty', validators=[DataRequired()])

