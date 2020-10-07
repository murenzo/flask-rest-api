from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister, User

app = Flask(__name__)
app.secret_key = 'azbaba'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='Field cannot be empty.')

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda item: item['name'] == name, items), None)

        return item, 200 if item else 404

    def post(self, name):
        if next(filter(lambda item: item['name'] == name, items), None):
            return {"message": f"An Item with name {name} already exist"}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda item: item['name'] != name, items))
        return {"message": "Item deleted successfully"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda item: item['name'] == name, items), None)

        if item is None:
            new_item = {'name': name, 'price': data['price']}
            items.append(new_item)
        else:
            item.update(data)
        return {"message": "Item updated successfully"}


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
