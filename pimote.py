from flask import Flask, make_response
from flask.ext.restful import Api
from model.database import  db_session
from routes.routes import ChannelResource, ChannelListResource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return make_response(open('templates/index.html').read())

api.add_resource(ChannelResource, '/api/channel/<channelId>')
api.add_resource(ChannelListResource, '/api/channel/')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug = True)