from flask_restful import Resource, reqparse
from models.user import UserModel


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        required=True,
                        help="Please, fill username section as well.")
    parser.add_argument("password",
                        required=True,
                        help="Please, fill in password sections as well.")

    def post(self):
        user_data = RegisterUser.parser.parse_args()

        if UserModel.find_by_username(user_data['username']):
            return {'message': "User already exists"}

        user = UserModel(user_data['username'], user_data['password'])
        user.add_user()

        return {'message': 'User created successfully'}
