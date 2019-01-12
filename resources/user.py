from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        """This resource allows users to register by sending a
        POST request with their username and password
        ---
        tags:
          - user
        parameters:
          - name: body
            in: body
            type: string
            required: true
            schema:
              required:
                - username
                - password
              properties:
                username:
                  type: string
                  description: username
                password:
                  type: string
                  description: password
        responses:
          200:
            description: The user logged
        """
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201
