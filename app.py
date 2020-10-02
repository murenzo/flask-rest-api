from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    pass


@app.route('/store/<string:name>/item')
def get_store_item(name):
    pass