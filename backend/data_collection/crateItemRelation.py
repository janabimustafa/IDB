from models import *
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker


'''
This file provides supplemental Rarity values for the RL Objects.
'''

db = create_engine('{dialect}://{user}:{password}@{host}/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, host=DB_HOST, db=DB_NAME))
Session = sessionmaker(bind=db)

Base.metadata.create_all(db)

s = Session()

crateItems = [
    CrateItemsRelation(crate_id=6991, item_id=10014),
    CrateItemsRelation(crate_id=6991, item_id=6937),
    CrateItemsRelation(crate_id=7237, item_id=10005),
    CrateItemsRelation(crate_id=7237, item_id=10006),
    CrateItemsRelation(crate_id=7237, item_id=7236),
    CrateItemsRelation(crate_id=7237, item_id=7235),
    CrateItemsRelation(crate_id=8313, item_id=10007),
    CrateItemsRelation(crate_id=8313, item_id=8310),
    CrateItemsRelation(crate_id=6987, item_id=6956),
    CrateItemsRelation(crate_id=6987, item_id=6963),
    CrateItemsRelation(crate_id=6983, item_id=6934),
    CrateItemsRelation(crate_id=6988, item_id=6950),
    CrateItemsRelation(crate_id=6988, item_id=6947),
    CrateItemsRelation(crate_id=6990, item_id=6956),
    CrateItemsRelation(crate_id=6990, item_id=6944),
    CrateItemsRelation(crate_id=6990, item_id=6941),
    CrateItemsRelation(crate_id=6992, item_id=6944),
    CrateItemsRelation(crate_id=6994, item_id=6941)
]

for relation in crateItems:
    s.merge(relation)
s.commit()