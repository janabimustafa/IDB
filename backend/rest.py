from flask import Flask, request, Blueprint
from flask_restplus import Api, Resource, reqparse, abort
from werkzeug.contrib.fixers import ProxyFix
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_searchable import search as searchable_search
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
        try:
            for Class in CLASS_TO_TYPE: # Works as a functional listing of all 'real' types
                res = s.query(Class).filter(Class.id == id).first()
                if res:
                    return serialize(res)
            abort(404)
        finally:
            s.close()


def get_obj_by_name(Class, name):
    s = Session()
    try:        
        query = s.query(Class).filter(func.lower(Class.name) == name.lower()).first()
        if not query:
            raise NotFound()
        return serialize(query)
    finally:
        s.close()

def get_obj_by_id(Class, id):
    s = Session()
    try:
        query = s.query(Class).filter(Class.id == id).first()
        if not query:
            raise NotFound()
        return serialize(query)
    finally:
        s.close()

def get_obj_list(Class):
    s = Session()
    try:
        return [serialize(e) for e in s.query(Class)]
    finally:
        s.close()


### Get type by name

# This and the other factories dynamically generate resource classes
# for each type of endpoint. c_name must name a type from models.
# Since using the type() constructor doesn't add the type to globals,
# it's fine to have multiple classes with the same name.
def SingularResourceFactory(c_name):
    def get(self, name):
        if name.isdigit():
            return get_obj_by_id(globals()[c_name], int(name))
        return get_obj_by_name(globals()[c_name], name)
    newres = type(c_name, (Resource,), {'get': get})
    return newres


### Get all of a type

def MultipleResourceFactory(c_name):
    def get(self):
        return get_obj_list(globals()[c_name])
    newres = type(c_name, (Resource,), {'get': get})
    return newres

query_pairings = {
    'Paint': 'paints',
    'Body': 'bodies',
    'Decal': 'decals',
    'Boost': 'boosts',
    'Topper': 'toppers',
    'Antenna': 'antennas',
    'Trail': 'trails',
    'Banner': 'banners',
    'Explosion': 'explosions',
    'Crate': 'crates',
    'Wheel': 'wheels',
    'DLC': 'dlcs',
    'Player': 'players'
}

for res, end in query_pairings.items():
    api.add_resource(SingularResourceFactory(res), '/{0}/<string:name>'.format(end))
    api.add_resource(MultipleResourceFactory(res), '/{0}/'.format(end))


### Search

@api.route('/search/<string:term>')
class Search_Res(Resource):

    def get(self, term):
        s = Session()
        try:
            return [serialize(k) for k in search(RLObject, (k for k in term.split()))]
        finally:
            s.close()


@api.route('/searchable_search/<string:term>')
class Searchable_Res(Resource):

    def get(self, term):
        return [serialize(k) for k in searchable_search(Session().query(RLObtainable), term, sort=True)]


### Meta mappings

def get_mapping(Class):
    s = Session()
    try:    
        return {r.id: r.name for r in s.query(Class)}
    finally:
        s.close()

def MetaResourceFactory(name):
    def get(self):
        return get_mapping(globals()[name])
    newres = type(name, (Resource,), {'get': get})
    return newres

meta_pairings = {
    'Rarity': 'rarities',
    'Source': 'sources',
    'Platform': 'platforms',
    'Paint': 'paints',
    'Body': 'bodies',
    'Decal': 'decals',
    'Boost': 'boosts',
    'Topper': 'toppers',
    'Antenna': 'antennas',
    'Trail': 'trails',
    'Banner': 'banners',
    'Explosion': 'explosions',
    'Crate': 'crates',
    'Wheel': 'wheels',
    'DLC': 'dlcs'
}

for res, end in meta_pairings.items():
    api.add_resource(MetaResourceFactory(res), '/meta/{0}'.format(end))


@api.route('/meta/about')
class AboutStats(Resource):

    def get(self):
        return about_stats.get_about_stats()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
