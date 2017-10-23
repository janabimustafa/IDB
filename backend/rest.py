from flask import Flask, request, Blueprint
from flask_restplus import Api, Resource, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_definitions import *
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

db = create_engine('{dialect}://{user}:{password}@db/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, db=DB_NAME))
Session = sessionmaker(bind=db)


### Internal ID lookup for any resource

@api.route('/id/<int:id>')
class ID_Res(Resource):

    def get(self, id):
        s = Session()
        for Class in CLASS_TO_TYPE: # Works as a functional listing of all 'real' types
            res = s.query(Class).filter(Class.id == id).first()
            if res:
                return serialize(res)
        abort(404)

def get_obj_by_name(Class, name):
    return serialize(Session().query(Class).filter(Class.name == name).first())

### Player lookup by id number

@api.route('/player_id/<int:id>')
class Player_ID(Resource):

    def get(self, id):
        return serialize(Session().query(Player).filter(Player.id == id).first())


### Player lookup by name

@api.route('/player_name/<string:name>')
class Player_Name(Resource):

    def get(self, name):
        return get_obj_by_name(Player, name)


### DLC Lookup by name

@api.route('/dlc/<string:name>')
class DLC_Res(Resource):

    def get(self, name):
        return get_obj_by_name(DLC, name)


### Body lookup by name

@api.route('/body/<string:name>')
class Body_Res(Resource):

    def get(self, name):
        return get_obj_by_name(Body, name)


### Crate lookup by name

@api.route('/crate/<string:name>')
class Crate_Res(Resource):

    def get(self, name):
        return get_obj_by_name(Crate, name)


### Antenna lookup by name

@api.route('/paint/<string:name>')
class Paint_Res(Resource):

    def get(self, name):
        return get_obj_by_name(Paint, name)


### Decal lookup by name

@api.route('/decal/<string:name>')
class Decal_Res(Resource):

    def get(self, name):
        return get_obj_by_name(Decal, name)


### Meta mappings

def get_mapping(Class):
    s = Session()
    return {r.id: r.name for r in s.query(Class)}

@api.route('/meta/rarities')
class GetRarities(Resource):

    def get(self):
        return get_mapping(Rarity)


@api.route('/meta/sources')
class GetSources(Resource):

    def get(self):
        return get_mapping(Source)


@api.route('/meta/platforms')
class GetSources(Resource):

    def get(self):
        return get_mapping(Platform)


@api.route('/meta/paints')
class GetPaints(Resource):

    def get(self):
        return get_mapping(Paint)


@api.route('/meta/bodies')
class GetBodies(Resource):

    def get(self):
        return get_mapping(Body)


@api.route('/meta/decals')
class GetDecals(Resource):

    def get(self):
        return get_mapping(Decal)


@api.route('/meta/crates')
class GetCrates(Resource):

    def get(self):
        return get_mapping(Crate)


@api.route('/meta/dlcs')
class GetDLCs(Resource):

    def get(self):
        return get_mapping(DLC)

if __name__ == '__main__':
    app.run(host='0.0.0.0')