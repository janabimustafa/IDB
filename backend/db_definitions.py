from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import json
import os

Base = declarative_base()

DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_DIALECT = os.environ['DB_DIALECT']
DB_HOST = os.environ['DB_HOST']
# To create this schema, ensure that the DB_NAME database exists,
# and that DB_USER:DB_PASS is correct. Then using the above Base object
# do: Base.metadata.create_all(engine) to initialize a blank db (or nop
# if it already exists)

db = create_engine('{dialect}://{user}:{password}@{host}/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, host=DB_HOST, db=DB_NAME))
Session = sessionmaker(bind=db)

class DBObject: # Everything
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

class RLObject(DBObject): # Non-meta
    @declared_attr
    def id(cls):
        return Column(Integer, ForeignKey('unique_ids.id'), primary_key=True)

    image = Column(String(300)) # URL of image

    _relations = []

    def __eq__(self, other):
        return serialize_str(self) == serialize_str(other)

    def __repr__(self):
        return "<RLObject(id='{0}', name='{1}', type='{2}')>".format(
                                self.id, self.name, CLASS_TO_TYPE.get(type(self)))

class RLObtainable(RLObject): # Not Players
    release_date = Column(Date)
    image = Column(String(300)) # URL of image
    description = Column(String(800))

class RLItem(RLObtainable): # Not DLC
    @declared_attr
    def source(cls):
        return Column(Integer, ForeignKey('sources.id'))

    @declared_attr
    def rarity(cls):
        return Column(Integer, ForeignKey('rarities.id'))

    description = Column(String)

# Used for ForeignKey
class Source(Base, DBObject):
    __tablename__ = 'sources'

# Used for ForeignKey
class Rarity(Base, DBObject):
    __tablename__ = 'rarities'

# Used for ForeignKey
class Platform(Base, DBObject):
    __tablename__ = 'platforms'

# Used to ensure all items have unique ids
class UniqueIDRelation(Base, DBObject):
    __tablename__ = 'unique_ids'

class Paint(Base, RLItem):
    __tablename__ = 'paints'
    crate = Column(ForeignKey('crates.id')) # ForeignKey
    _relations = [('decals', 'decal_id', 'SELECT * FROM paint_decal_relations WHERE paint_id = {0}')]
    #list of decals stored in PaintDecalsRelation table

# Maps paints to decals
class PaintDecalsRelation(Base):
    __tablename__ = 'paint_decal_relations'
    paint_id = Column(ForeignKey('paints.id'), primary_key=True)
    decal_id = Column(ForeignKey('decals.id'), primary_key=True)

class Body(Base, RLItem):
    __tablename__ = 'bodies'
    _relations = [('decals', 'decal_id', 'SELECT * FROM body_decal_relations WHERE body_id = {0}')]
    #list of decals stored in BodyDecalsRelation table

class BodyDecalsRelation(Base):
    __tablename__ = 'body_decal_relations'
    body_id = Column(ForeignKey('bodies.id'), primary_key=True)
    decal_id = Column(ForeignKey('decals.id'), primary_key=True)

class Decal(Base, RLItem):
    __tablename__ = 'decals'
    crate = Column(Integer, ForeignKey('crates.id')) # ForeignKey
    is_animated = Column(Boolean)
    is_paintable = Column(Boolean)
    _relations = [('bodies', 'item_id', 'SELECT * FROM body_decal_relations WHERE decal_id = {0}')]
    #list of bodies stored in BodyDecalsRelation table

class Wheel(Base, RLItem):
    __tablename__ = 'wheels'

class Crate(Base, RLItem):
    __tablename__ = 'crates'
    retire_date = Column(Date)
    _relations = [('items', 'item_id', 'SELECT * FROM crate_item_relations WHERE crate_id = {0}')]

class CrateItemsRelation(Base):
    __tablename__ = 'crate_item_relations'
    crate_id = Column(ForeignKey('crates.id'), primary_key=True)
    item_id = Column(ForeignKey('unique_ids.id'), primary_key=True) # Foreign key to all returnable types

class DLC(Base, RLObtainable):
    __tablename__ = 'dlcs'
    _relations = [('items', 'item_id', 'SELECT * FROM dlc_item_relations WHERE dlc_id = {0}')]

class DLCItemsRelation(Base):
    __tablename__ = 'dlc_item_relations'
    dlc_id = Column(ForeignKey('dlcs.id'), primary_key=True)
    item_id = Column(ForeignKey('unique_ids.id'), primary_key=True) # Foreign key to all returnable types

class Player(Base, RLObject):
    __tablename__ = 'players'
    platform = Column(Integer, ForeignKey('platforms.id')) # ForeignKey
    skill_rating = Column(Integer) # Average of Ranked modes in most recent season
    wins = Column(Integer)

TYPE_TO_CLASS = {
    'paint': Paint,
    'body': Body,
    'decal': Decal,
    'crate': Crate,
    'dlc': DLC,
    'player': Player,
    'wheel': Wheel
}

CLASS_TO_TYPE = {v: k for k, v in TYPE_TO_CLASS.items()}

def serialize(rl_object):
    if rl_object is None:
        return None
    sdict = {k: rl_object.__dict__[k] for k in rl_object.__dict__ if not k.startswith('_')}
    sdict['type'] = CLASS_TO_TYPE.get(type(rl_object))
    conn = db.connect()
    for rel in rl_object._relations:
        res = conn.execute(rel[2].format(rl_object.id))
        sdict[rel[0]] = [k[rel[1]] for k in res]
    return sdict

def serialize_str(rl_object):
    return json.dumps(serialize(rl_object))

# Deserializes json into an object (or None if type unknown)
# this returns a new instance of that object
def deserialize(json_str):
    sdict = json.loads(json_str)
    return __deserialize_helper(sdict)

def __deserialize_helper(sdict):
    class_ = TYPE_TO_CLASS.get(sdict.get('type'))
    if class_:
        del sdict['type']
        return class_(**sdict)
    return None

def deserialize_list(json_str):
    json_list = json.loads(json_str)
    object_list = [__deserialize_helper(json) for json in json_list]
    return object_list

