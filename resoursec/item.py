from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.item import Product


class ItemList(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), Product.query.all()))}


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
        if item:
            item.price = data["price"]
            item.quantity = data["quantity"]
            message = "Item was updated successfully."

        else:
            message = "New item was added successfully."
            item = Product(**data)

        item.save_to_db()

        return {'message': message}

    @jwt_required()
    def delete(self, model):
        item = Product.find_by_name(model)

        if item:
            item.delete_from_db()
            return {'message': 'Deleting was successful'}

        return {'message': 'You are trying to delete product which does not exist'}, 404