from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
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

class RLObject: # Everything
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __eq__(self, other):
        return serialize(self) == serialize(other)

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
class Source(Base, RLObject):
    __tablename__ = 'sources'

# Used for ForeignKey
class Rarity(Base, RLObject):
    __tablename__ = 'rarities'

# Used for ForeignKey
class Platform(Base, RLObject):
    __tablename__ = 'platforms'

class Paint(Base, RLItem):
    __tablename__ = 'paints'
    crate = Column(ForeignKey('crates.id')) # ForeignKey
    #list of decals stored in PaintDecalsRelation table

# Maps paints to decals
class PaintDecalsRelation(Base):
    __tablename__ = 'paint_decal_relations'
    paint_id = Column(ForeignKey('paints.id'), primary_key=True)
    decal_id = Column(ForeignKey('decals.id'), primary_key=True)

class Body(Base, RLItem):
    __tablename__ = 'bodies'
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
    #list of bodies stored in BodyDecalsRelation table

class Crate(Base, RLItem):
    __tablename__ = 'crates'
    retire_date = Column(Date)
    # Not sure how to do this, maybe just a bunch of other tables for Crate to each other type?
    items = Column(String(50)) # Should be a list of ids or something

class DLC(Base, RLObtainable):
    __tablename__ = 'dlcs'
    items = Column(String(50)) # Should be a list of ids (ForeignKeys)

class Player(Base, RLObject):
    __tablename__ = 'players'
    platform = Column(Integer, ForeignKey('platforms.id')) # ForeignKey
    skill_rating = Column(String(50)) # Should be a list of skill ratings (or dict)
    rank = Column(Integer)
    wins = Column(Integer)

TYPE_TO_CLASS = {
    'paint': Paint,
    'body': Body,
    'decal': Decal,
    'crate': Crate,
    'dlc': DLC,
    'player': Player
}

CLASS_TO_TYPE = {v: k for k, v in TYPE_TO_CLASS.items()}

def serialize(rl_object):
    if rl_object is None:
        return None
    sdict = {k: rl_object.__dict__[k] for k in rl_object.__dict__ if not k.startswith('_')}
    sdict['type'] = CLASS_TO_TYPE.get(type(rl_object))
    return sdict

def serialize_str(rl_object):
    return json.dumps(serialize(rl_object))

# Deserializes json into an object (or None if type unknown)
# this returns a new instance of that object
def deserialize(json_str):
    sdict = json.loads(json_str)
    class_ = TYPE_TO_CLASS.get(sdict.get('type'))
    if class_:
        del sdict['type']
        return class_(**sdict)
    return None
