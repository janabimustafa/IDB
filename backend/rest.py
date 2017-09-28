from flask import Flask, request, Blueprint
from flask_restplus import Api, Resource, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix
"""
This is likely not the final form of
this file, so I've skipped on the documentation
for now. If this gets too large, we might want
to separate endpoints out into different files.
"""


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, version='1.0', title='RocketLeague API',
    description='API for getting data about everything RocketLeague',
    default_mediatype='application/json',
    validate=True)
app.register_blueprint(blueprint)
db = {'TODO': 'Replace with DB query'}


### Internal ID lookup for any resource

@api.route('/id/<int:id>')
class ID_Res(Resource):

    def get(self, id):
        return {'message': db.get(id, id)}


### Player lookup by id number

@api.route('/player_id/<int:id>')
class Player_ID(Resource):

    def get(self, id):
        return {'message': db.get(id, id)}


### Player lookup by name

@api.route('/player_name/<string:name>')
class Player_Name(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


### DLC Lookup by name

@api.route('/dlc/<string:name>')
class DLC_Res(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


### Body lookup by name

@api.route('/body/<string:name>')
class Body_Res(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


### Crate lookup by name

@api.route('/crate/<string:name>')
class Crate_Res(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


### Antenna lookup by name

@api.route('/paint/<string:name>')
class Paint_Res(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


### Decal lookup by name

@api.route('/decal/<string:name>')
class Decal_Res(Resource):

    def get(self, name):
        return {'message': db.get(name, name)}


if __name__ == '__main__':
    app.run(host='0.0.0.0')