from security import *
from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from resoursec.user import RegisterUser
from resoursec.item import Item, ItemList


app = Flask(__name__)

app.secret_key = "I can not tell"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my-data.db"
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def home():
    return redirect('https://github.com/sun-dro/unilab-rest-api/tree/main'), 302


api.add_resource(ItemList, "/items")
api.add_resource(Item, "/items/<string:model>")
api.add_resource(RegisterUser, "/registration")


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

