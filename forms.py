from wtforms import Form, StringField, SelectField

class ProductSearchForm(Form):
    choices = [('Shampoo', 'Shampoo'),
               ('Lotion', 'Lotion'),
               ('Cream', 'Cream'),
               ('Balm', 'Balm'),
               ('Oil', 'Oil'),
               ('Conditioner', 'Conditioner')]
    select = SelectField('Search for Product:', choices = choices)
    search = StringField('')
"""
class ShapeSearchForm(Form):
    choices = [('Cylinder', 'Cylinder'),
               ('Flat', 'Flat'),
               ('Oval', 'Oval'),
               ('Curvy', 'Curvy'),
               ('Square', 'Square'),
               ('Rectangle', 'Rectangle')]
    select = SelectField('Search for Shape:', choices = choices)

class TypeSearchForm(Form):
    choices = [('Opaque', 'Opaque'),
               ('Transparent', 'Transparent')]
    select = SelectField('Search for Type:', choices = choices)"""

class ProductForm(Form):
    product_choices = [('Shampoo', 'Shampoo'),
                       ('Lotion', 'Lotion'),
                       ('Cream', 'Cream'),
                       ('Balm', 'Balm'),
                       ('Oil', 'Oil'),
                       ('Conditioner', 'Conditioner')]
    container_type_choices = [('Opaque', 'Opaque'),
                              ('Transparent', 'Transparent')]
    shape_choices=[('Cylinder', 'Cylinder'),
                   ('Flat', 'Flat'),
                   ('Oval', 'Oval'),
                   ('Curvy', 'Curvy'),
                   ('Square', 'Square'),
                   ('Rectangle', 'Rectangle')]

    material_of_construction = StringField('Material of construction')
    moulding_process = StringField('Moulding process')
    neck_type = StringField('Neck type')
    SKU = StringField('SKU')
    product = SelectField('Product', choices=product_choices)
    best_suited_for = StringField('Best suited for')
    container_type = SelectField('Container type', choices=container_type_choices)
    vendor_name = StringField('Vendor name')
    product_name = StringField('Product name')
    ofc = StringField('OFC')
    weight = StringField('Weight')
    price = StringField('Price')
    shape = SelectField('Shape', choices=shape_choices)
