from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from flask import jsonify

from model.models import Channel, Show
from model.database import db_session


class ChannelResource(Resource):

    def get(self, channelId):
        result = Channel.query.filter_by(channelId=channelId).first()
        return {'channelId': result.channelId, 'name': result.name, 'shows': result.shows }


class ChannelListResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)

    def get(self):
        #results = Channel.query.all()
        '''json_results = []
        for r in results:
            j = {'channelId': r.channelId, 'name': r.name, 'shows': r.shows }
            json_results.append(j)
        return json_results'''
        return jsonify(channels=[i.serialize for i in Channel.query.all()])

    def post(self):
        args = self.parser.parse_args()
        c = Channel(args['name'])
        db_session.add(c)
        db_session.commit()
        return { 'channelId': c.channelId, 'name': c.name, 'shows': c.shows }


class ShowResource(Resource):

    def get(self, showId):
        result = Show.query.filter_by(id=showId).first()
        return jsonify(result)
