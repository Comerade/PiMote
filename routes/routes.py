from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask import jsonify
from model.models import Channel
from model.database import db_session


class ChannelResource(Resource):

    def get(self, channelId):
        result = Channel.query.filter_by(id=channelId).first()
        return {'id': result.id, 'name': result.name }


class ChannelListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    def get(self):
        results = Channel.query.all()
        json_results = []
        for r in results:
            j = {'id': r.id, 'name': r.name }
            json_results.append(j)
        return json_results

    def post(self):
        args = self.parser.parse_args()
        c = Channel(args['name'])
        db_session.add(c)
        db_session.commit()
        return { 'id': c.id, 'name': c.name }
