

from.db import Product, Item, Cart

SUPPORTED_ENTITIES = ['products', 'carts', 'users',
                      'items', 'cart_items', 'product_items']


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username


# # class CrudEntity:
# #     ID_FIELD = 'id'
# #     EDITABLE_FIELDS = []
# #     TABLE_NAME = ''
# #     POSSIBLE_ACTIONS = ['CREATE', 'DELETE', 'EDIT', 'READ']

# #     def get(self):
# #         if self.TABLE_NAME not in SUPPORTED_ENTITIES:
# #             return (False, [])
# #         entities = db.get_all(self.TABLE_NAME)
# #         return (True, entities)

# #     def get_single(self, id):
# #         if self.TABLE_NAME not in SUPPORTED_ENTITIES:
# #             return (False, [])
# #         entity = db.get_single(self.TABLE_NAME, id)
# #         return (True, entity)

# #     def remove(self, id):
# #         if self.TABLE_NAME not in SUPPORTED_ENTITIES:
# #             return (False, [])
# #         db.remove(self.TABLE_NAME, id)
# #         return True


# # class Product(CrudEntity):
# #     EDITABLE_FIELDS = ['name', 'price']
# #     TABLE_NAME = 'products'


# # class Item(CrudEntity):
# #     EDITABLE_FIELDS = ['name', 'available_qty']
# #     TABLE_NAME = 'items'


# # class Cart(CrudEntity):
# #     EDITABLE_FIELDS = ['password']
# #     TABLE_NAME = 'users'


entities = { 'products': Product, 'items': Item, 'carts': Cart }
def resolve_entity(name):
    if name not in entities:
        return (False, None)
    return (True, entities[name])
