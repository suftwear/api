# User Resource, for actions on the User model (table)

from resources import *
from models import User, UserMeta

from common.authentication import api_validation

user_fields = {
    'id': fields.Integer,
    'meta.name': fields.String,
    'meta.surname': fields.String,
    'meta.photo_id': fields.String,
    'meta.facebook_token': fields.String,
    'meta.description': fields.String,
}

meta_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'subject_id': fields.Integer,
    'level_id': fields.Integer,
}


# User Data field parser
# Used for parsing the user and user meta fields inside the data field
user_data_parser = reqparse.RequestParser()
user_data_parser.add_argument('user', type=dict, required=True, location=('data'))
user_data_parser.add_argument('meta', type=dict, required=True, location=('data'))

# User parser
# Used for parsing the fields inside the user field
user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True, help="email", location=('user'))
user_parser.add_argument('password', type=str, required=True, help="password", location=('user'))

# Usermeta parser
# Used for parsing the fields inside the user meta field
usermeta_parser = reqparse.RequestParser()
usermeta_parser.add_argument('name', type=str, help="email", location=('usermeta'))
usermeta_parser.add_argument('surname', type=str, help="surname", location=('usermeta'))
usermeta_parser.add_argument('postal_code', type=str, help="postal_code", location=('usermeta'))
usermeta_parser.add_argument('phone', type=str, help="phone", location=('usermeta'))
usermeta_parser.add_argument('photo_id', type=str, help="photo_id", location=('usermeta'))
usermeta_parser.add_argument('facebook_token', type=str, help="facebook_token", location=('usermeta'))
usermeta_parser.add_argument('description', type=str, help="description", location=('usermeta'))


class UserByIdResource(Resource):
    """
    Class for handling the GET, PUT and DELETE requests for "/user/<int:id>"

    GET is used for giving info about an User model, given an User id
    PUT is used for changing info about an User model, given an User id,
        you cannot create a user using this method.
    DELETE is used deleting an User model, given an User id

    """

    def __init__(self):
        self.method = request.method
        self.path = request.path
        self.args = main_parser.parse_args()

    @marshal_with(user_fields)
    @api_validation
    def get(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User with id={} doesn't exist".format(id))

        return user, 200

    @marshal_with(user_fields)
    @api_validation
    def put(self, id):
        user_data_args = user_data_parser.parse_args(self.args)

        user_data = user_parser.parse_args(user_data_args)
        usermeta_data = usermeta_parser.parse_args(user_data_args)

        # Check if user with id exists
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User with id={} doesn't exist".format(id))

        if user_data['email']:
            user.email = user_data['email']
        if user_data['password']:
            user.password = user_data['password']
        session.add(user)
        session.commit()

        return usermeta_data, 201

    @api_validation
    def delete(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User with id={} doesn't exist".format(id))
        session.delete(user)
        session.commit()
        return {}, 204


class UserResource(Resource):
    """
    Class for handling the GET, POST requests for "/user"

    GET TODO: not yet implemented, is used for managing your own User model
    POST is used for creating an new User model
    DELETE TODO: not yet implemented

    """

    def __init__(self):
        self.method = request.method
        self.path = request.path
        self.args = main_parser.parse_args()

    @marshal_with(user_fields)
    @api_validation
    def get(self):
        pass

    @marshal_with(user_fields)
    @api_validation
    def post(self):
        user_data = self.args['data']['user']
        usermeta_data = self.args['data']['usermeta']

        user = User(email=user_data['email'], password=user_data['password'])
        user.meta = UserMeta(name=usermeta_data['name'],
                             surname=usermeta_data['surname'],
                             postal_code=usermeta_data['postal_code'],
                             phone=usermeta_data['phone'],
                             photo_id='photo',
                             facebook_token='fb_token',
                             description=usermeta_data['desc'])
        session.add(user)
        session.commit()
        return user, 201
