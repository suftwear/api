"""
SubjectResource.py

For returning list of levels, requires no API authorization

"""


from resources import *  # NOQA
from models import Level


level_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


class SubjectResource(Resource):
    """
    Class for handling the GET requests to "/level/all"

    """

    @api_validation
    @marshal_with(level_fields)
    def get(self):
        levels = session.query(Level).all()

        if not levels:
            abort(404, message="No levels found")

        # TODO remove extra header in final, temporarily allows cross-site ajax
        return levels, 200, {"Access-Control-Allow-Origin": "*"}
