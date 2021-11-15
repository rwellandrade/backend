

from .models import Product, Item, Cart
from .forms import ProductForm, ItemForm

SUPPORTED_ENTITIES = ['products', 'carts', 'users',
                      'items', 'cart_items', 'product_items']


entities = { 'products': Product, 'items': Item, 'carts': Cart }
def resolve_entity(name):
    if name not in entities:
        return (False, None)
    return (True, entities[name])


forms = { 'products': ProductForm, 'items': ItemForm, 'carts': Cart }
def resolve_forms(name):
    if name not in forms:
        return (False, None)
    return (True, forms[name])
