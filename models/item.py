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

    # def _rept__(self):
    #     return {"model": self.model, "price": self.price, "quantity": self.quantity}

    def json(self):
        return {"model": self.model, "price": self.price, "quantity": self.quantity}

    @classmethod
    def show_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, model):
        #item = Product.query.filter_by(name=name).first()
        return cls.query.filter_by(model=model).first()
        # query.all - yvela monacems wamoigebs
        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # curs.execute("SELECT * from items WHERE id=?", (item_id,))
        # row = curs.fetchone()
        # connec.commit()
        # connec.close()
        # if row:
        #     return {'item': {'id': row[0], 'model': row[1], 'price': row[2], 'quantity': row[3]}}

    #@classmethod
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # new_item = "INSERT INTO items (id, model, price, quantity) VALUES (?, ?, ?, ?)"
        # curs.execute(new_item, (*item_id.values(), ))
        # connec.commit()
        # connec.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    # @classmethod
    # def update(cls, item_info, item_id):
    #     connec = sqlite3.connect('my-data.db')
    #     curs = connec.cursor()
    #     upd_item = "UPDATE items SET id=?, model=?, price=?, quantity=? WHERE id =?"
    #     curs.execute(upd_item, (*item_info.values(), item_id))
    #     connec.commit()
    #     connec.close()