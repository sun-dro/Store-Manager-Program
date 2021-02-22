from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from models.item import Product


class ItemList(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), Product.query.all()))}
        # all_items = Product.query.all()
        # item_list = []

        # for item, item1, item2, item3 in all_items:
        #     return item.json()
        # for item in all_products:
        #     return {"model": self.model, "price": self.price, "quantity": self.quantity}
        # all_items = Product.find_all()
        # data = []
        # for item in all_items:
        #     data.append(item)
        #     data = json.dumps(data)
        #     return data
        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # curs.execute("SELECT * from items")
        # row = curs.fetchall()
        # connec.close()
        # return row

    # @jwt_required()
    # def delete(self):
    #     # db.session.delete()
    #     # db.session.commit()
    #     # connec = sqlite3.connect('my-data.db')
    #     # curs = connec.cursor()
    #     # curs.execute("DELETE from items")
    #     # connec.commit()
    #     # connec.close()
    #     return {"message": "Deleting was successful"}


class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("model",
                        type=str,
                        required=True,
                        help="Use just strings for the 'model' value in your request")
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="Use just integers or floats for the 'price' value in your request")
    parser.add_argument("quantity",
                        type=int,
                        required=True,
                        help="Use just integers for the 'quantity' value in your request")

    def get(self, model):
        item = Product.find_by_name(model)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @jwt_required()
    def post(self, model):

        item = Product.find_by_name(model)
        if not item:
            data = Item.parser.parse_args()
            item = Product(data['model'], data['price'], data['quantity'])
            Product.save_to_db(item)
            return {'message': "New item was added successfully."}
        else:
            return {'message': 'Item with this name already exists.'}

    @jwt_required()
    def put(self, model):
        item = Product.find_by_name(model)
        data = Item.parser.parse_args()
        #item = Product.find_by_id(item_id)
        if item:
            #ver anaxlebs aq
            item.price = data["price"]
            item.quantity = data["quantity"]
            message = "Item was updated successfully."

        else:
            message = "New item was added successfully."
            item = Product(**data)

        item.save_to_db()
        #return item.json()
        return {'message': message}

        # if not item:
        #     Product.insert(data)
        #     return {'message': "New item was added successfully."}
        # else:
        #     Product.update(data, item_id)
        #     return {'message': "Item was updated successfully."}

    @jwt_required()
    def delete(self, model):
        item = Product.find_by_name(model)

        if item:
            item.delete_from_db()
            return {'message': 'Deleting was successful'}

        return {'message': 'You are trying to delete product which does not exist'}, 404

        # connec = sqlite3.connect('my-data.db')
        # curs = connec.cursor()
        # curs.execute("SELECT * from items WHERE id=?", (item_id,))
        # row = curs.fetchone()
        # if row:
        #     curs.execute("DELETE from items WHERE id =?", (item_id, ))
        #     connec.commit()
        #     connec.close()
        #     return {'message': 'Deleting was successful'}
        # else:
        #     return {'message': 'You are trying to delete product which does not exist'}
