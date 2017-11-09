from flask import Flask, request, Blueprint
from flask_restplus import Api, Resource, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix
from sqlalchemy import create_engine, func
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
    query = Session().query(Class).filter(func.lower(Class.name) == name.lower()).first()
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

@api.route('/boosts/')
class Boosts_Res(Resource):
    def get(self):
        return get_obj_list(Boost)


@api.route('/boosts/<string:name>')
class Boost_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Boost, int(name))
        return get_obj_by_name(Boost, name)


@api.route('/wheels/')
class Wheels_Res(Resource):
    def get(self):
        return get_obj_list(Wheel)


@api.route('/wheels/<string:name>')
class Wheel_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Wheel, int(name))
        return get_obj_by_name(Wheel, name)


@api.route('/toppers/')
class Boosts_Res(Resource):
    def get(self):
        return get_obj_list(Topper)


@api.route('/toppers/<string:name>')
class Boost_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Topper, int(name))
        return get_obj_by_name(Topper, name)

@api.route('/explosions/')
class Explosions_Res(Resource):
    def get(self):
        return get_obj_list(Explosion)


@api.route('/explosions/<string:name>')
class Explosion_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Explosion, int(name))
        return get_obj_by_name(Explosion, name)

@api.route('/trails/')
class Trails_Res(Resource):
    def get(self):
        return get_obj_list(Trail)


@api.route('/trails/<string:name>')
class Trail_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Trail, int(name))
        return get_obj_by_name(Trail, name)

@api.route('/banners/')
class Banners_Res(Resource):
    def get(self):
        return get_obj_list(Banner)


@api.route('/banners/<string:name>')
class Banner_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Banner, int(name))
        return get_obj_by_name(Banner, name)

@api.route('/antennas/')
class Antennas_Res(Resource):
    def get(self):
        return get_obj_list(Antenna)


@api.route('/antennas/<string:name>')
class Antenna_Res(Resource):

    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(Antenna, int(name))
        return get_obj_by_name(Antenna, name)

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
class GetPlatforms(Resource):

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

@api.route('/meta/boosts')
class GetBoosts(Resource):

    def get(self):
        return get_mapping(Boost)

@api.route('/meta/toppers')
class GetToppers(Resource):

    def get(self):
        return get_mapping(Topper)

@api.route('/meta/antennas')
class GetAntennas(Resource):

    def get(self):
        return get_mapping(Antenna)

@api.route('/meta/trails')
class GetBoosts(Resource):

    def get(self):
        return get_mapping(Trail)

@api.route('/meta/banners')
class GetBanners(Resource):

    def get(self):
        return get_mapping(Banner)

@api.route('/meta/explosions')
class GetExplosions(Resource):

    def get(self):
        return get_mapping(Explosion)


@api.route('/meta/crates')
class GetCrates(Resource):

    def get(self):
        return get_mapping(Crate)
    
@api.route('/meta/wheels')
class GetWheels(Resource):

    def get(self):
        return get_mapping(Wheel)

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
