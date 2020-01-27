from app import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Product: {}".format(self.name)

class Master(db.Model):
    __tablename__ = "master"

    id = db.Column(db.Integer, primary_key = True)
    material_of_construction = db.Column(db.String)
    moulding_process = db.Column(db.String)
    neck_type = db.Column(db.String)
    SKU = db.Column(db.Integer)
    product = db.Column(db.String)
    best_suited_for = db.Column(db.String)
    container_type = db.Column(db.String)
    vendor_name = db.Column(db.String)
    product_name = db.Column(db.String)
    ofc = db.Column(db.String)
    weight = db.Column(db.String)
    price = db.Column(db.Float)
    shape = db.Column(db.String)

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    product = db.relationship("Product", backref = db.backref("master", order_by = id), lazy = True)
