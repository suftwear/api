#!/usr/bin/env python
"""
    ReviewResource.py, for actions on the Review model,
    this file is a module and has no use as stand-alone file

    ReviewResource contains the following classes:
    TODO
"""


from resources import *  # NOQA
from models import User, UserMeta, Zipcode, Offer


review_fields = {
    'rating': fields.Integer,
    'description': fields.String,
    'author.meta.photo_id': fields.String,
    'author.meta.name': fields.String,
    'author.meta.surname': fields.String,
}


class ReviewByUserIdResource(Resource):
    """
    Class for handling the GET "/user/<int:id>/review"

    GET is used to get the reviews for a User model, given an User id

    """

    def __init__(self):
        self.method = request.method
        self.full_path = request.full_path
        self.args = main_parser.parse_args()

    @api_validation
    @marshal_with(review_fields)
    def get(self, id):
        user = session.query(User).filter(User.id == id).first()
        if not user:
            abort(404, message="User with id={} doesn't exist".format(id))

        reviews = []

        for offer in user.offers:
            reviews += offer.review
        if not reviews:
            abort(404, message="No reviews found for User with id={}".format(id))

        return reviews, 200