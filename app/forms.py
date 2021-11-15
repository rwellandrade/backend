from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, FormField, SelectField, FieldList
from wtforms.validators import DataRequired
# from wtforms_sqlalchemy import ModelFieldList
from .models import Item, Product


class ProductItemForm(FlaskForm):
    its = SelectField('Item', coerce=int)
    quantity = IntegerField('quantity')

    def __init__(self, *args, **kwargs):
        super(ProductItemForm, self).__init__(*args, **kwargs)
        self.its.choices = [(item.id, item.name)
                                 for item in Item.query.order_by(Item.name).all()]

def available_items():
    return Item.query.all()

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    its = FieldList(FormField(ProductItemForm), min_entries=3)


class ItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    available_qty = IntegerField('available_qty', validators=[DataRequired()])

