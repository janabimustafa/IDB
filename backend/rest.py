from flask import Flask, request, Blueprint
from flask_restplus import Api, Resource, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_searchable import search
from werkzeug.exceptions import BadRequest, NotFound
from models import *
import about_stats
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
    query = Session().query(Class).filter(Class.name == name).first()
    if not query:
        raise NotFound()
    return serialize(query)
def get_obj_by_id(Class, id):
    query = Session().query(Class).filter(Class.id == id).first()
    if not query:
        raise NotFound()
    return serialize(query)
def get_obj_list(Class):
    return [serialize(e) for e in Session().query(Class)]

### Player lookup by id number

@api.route('/players/')
class Players_Res(Resource):
    def get(self):
        return get_obj_list(Player)


@api.route('/players/<string:name>')
class Player_Res(Resource):
    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Player, int(name))
        return get_obj_by_name(Player, name)

### DLC Lookup by name
@api.route('/dlcs/')
class DLCs_Res(Resource):
    def get(self):
        return get_obj_list(DLC)


@api.route('/dlcs/<string:name>')
class DLC_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(DLC, int(name))
        return get_obj_by_name(DLC, name)


### Body lookup by name

@api.route('/bodies/')
class Bodies_Res(Resource):
    def get(self):
        return get_obj_list(Body)


@api.route('/bodies/<string:name>')
class Body_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Body, int(name))
        return get_obj_by_name(Body, name)


### Crate lookup by name

@api.route('/crates/')
class Crates_Res(Resource):
    def get(self):
        return get_obj_list(Crate)

@api.route('/crates/<string:name>')
class Crate_Res(Resource):
    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Crate, int(name))
        return get_obj_by_name(Crate, name)


### Antenna lookup by name

@api.route('/paints/')
class Paints_Res(Resource):
    def get(self):
        return get_obj_list(Paint)

@api.route('/paints/<string:name>')
class Paint_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Paint, int(name))
        return get_obj_by_name(Paint, name)


### Decal lookup by name


@api.route('/decals/')
class Decals_Res(Resource):
    def get(self):
        return get_obj_list(Decal)


@api.route('/decals/<string:name>')
class Decal_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Decal, int(name))
        return get_obj_by_name(Decal, name)


### Search

@api.route('/search/<string:term>')
class Search_Res(Resource):

    def get(self, term):
        return [serialize(k) for k in search(Session().query(RLObtainable), term, sort=True)]


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


@api.route('/meta/about')
class AboutStats(Resource):

    def get(self):
        return about_stats.get_about_stats()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
