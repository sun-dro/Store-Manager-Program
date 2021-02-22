from db import db


class Product(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String(80), unique=True)
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Float)

    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity

    def json(self):
        return {"model": self.model, "price": self.price, "quantity": self.quantity}

    @classmethod
    def find_by_name(cls, model):
        return cls.query.filter_by(model=model).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()