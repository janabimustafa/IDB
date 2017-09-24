from flask import Flask, request
from flask_restplus import Api, Resource, reqparse, abort

"""
This is likely not the final form of
this file, so I've skipped on the documentation
for now. If this gets too large, we might want
to separate endpoints out into different files.
"""


app = Flask(__name__)

api = Api(app, version='1.0', title='RocketLeague API',
    description='API for getting data about everything RocketLeague',
    default_mediatype='application/json',
    validate=True)

db = {'TODO': 'Replace with DB query'}


### Internal ID lookup for any resource

id_parser = api.parser()
id_parser.add_argument('id', type=int, required=True)

@api.route('/id')
class ID_Res(Resource):

    @api.expect(id_parser)
    def get(self):
        args = id_parser.parse_args()
        return {'message': db['TODO']}


### Player lookup by name or id number. Name returns first with that name since not unique?

player_parser = api.parser()
player_parser.add_argument('name', type=str)
player_parser.add_argument('id', type=int)

@api.route('/player')
class Player_Res(Resource):

    @api.expect(player_parser)
    def get(self):
        args = player_parser.parse_args()
        if args['name'] is None and args['id'] is None:
            abort(400, 'At least one of player id or name is required. Player id is preferred.')
        return {'message': str(args)}


### DLC Lookup by name

dlc_parser = api.parser()
dlc_parser.add_argument('name', type=str, required=True)

@api.route('/dlc')
class DLC_Res(Resource):

    @api.expect(dlc_parser)
    def get(self):
        args = dlc_parser.parse_args()
        return {'message': db['TODO']}


### Body lookup by name

body_parser = api.parser()
body_parser.add_argument('name', type=str, required=True)

@api.route('/body')
class Body_Res(Resource):

    @api.expect(body_parser)
    def get(self):
        args = body_parser.parse_args()
        return {'message': db['TODO']}


### Crate lookup by name

crate_parser = api.parser()
crate_parser.add_argument('name', type=str, required=True)

@api.route('/crate')
class Crate_Res(Resource):

    @api.expect(crate_parser)
    def get(self):
        args = crate_parser.parse_args()
        return {'message': db['TODO']}


### Antenna lookup by name

antenna_parser = api.parser()
antenna_parser.add_argument('name', type=str, required=True)

@api.route('/antenna')
class Antenna_Res(Resource):

    @api.expect(antenna_parser)
    def get(self):
        args = antenna_parser.parse_args()
        return {'message': db['TODO']}


### Decal lookup by name

decal_parser = api.parser()
decal_parser.add_argument('name', type=str, required=True)

@api.route('/decal')
class Decal_Res(Resource):

    @api.expect(decal_parser)
    def get(self):
        args = decal_parser.parse_args()
        return {'message': db['TODO']}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)