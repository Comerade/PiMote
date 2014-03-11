from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask import jsonify

from model.models import Channel, Show
from model.database import db_session


class ChannelResource(Resource):

    def get(self, channelId):
        result = Channel.query.filter_by(channelId=channelId).first()
        return jsonify(result.serialize)


class ChannelListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    def get(self):
        result = Channel.query.all()
        return jsonify(channels=[i.serialize for i in result])

    def post(self):
        args = self.parser.parse_args()
        c = Channel(args['name'])
        db_session.add(c)
        db_session.commit()
        return jsonify(c.serialize)


class ShowResource(Resource):

    def get(self, showId):
        result = Show.query.filter_by(id=showId).first()
        return jsonify(result.serialize)
