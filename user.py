import sqlite3
from flask_restful import Resource, reqparse


class User():
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users where username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        user = cls(*row) if row else None
        # print(user)

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        user = cls(*row) if row else None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Field cannot be empty.')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Field cannot be empty.')

    def post(self):
        data = UserRegister.parser.parse_args()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully"}, 201
