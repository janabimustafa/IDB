from db_definitions import *
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker


'''
This file provides supplemental Rarity values for the RL Objects.
'''

db = create_engine('{dialect}://{user}:{password}@{host}/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, host=DB_HOST, db=DB_NAME))
Session = sessionmaker(bind=db)

Base.metadata.reflect(db)
Base.metadata.drop_all(db)
# for tbl in reversed(Base.metadata.sorted_tables):
#     try:
#         tbl.drop(db)
#     except:
#         pass
Base.metadata.create_all(db)

s = Session()
rarities = [
    Rarity(id=1, name='common'),
    Rarity(id=2, name='uncommon'),
    Rarity(id=3, name='rare'),
    Rarity(id=4, name='very_rare'),
    Rarity(id=5, name='limited'),
    Rarity(id=6, name='premium'),
    Rarity(id=7, name='import'),
    Rarity(id=8, name='exotic'),
    Rarity(id=9, name='black_market')
]

platforms = [
    Platform(id=1, name="Steam"),
    Platform(id=2, name="Playstation"),
    Platform(id=3, name="Xbox")
]

crateItems = [
    CrateItemsRelation(id=1, crate_id=6991, item_id=10017),
    CrateItemsRelation(id=2, crate_id=6991, item_id=6937),
    CrateItemsRelation(id=3, crate_id=7237, item_id=10005),
    CrateItemsRelation(id=4, crate_id=7237, item_id=10006),
    CrateItemsRelation(id=5, crate_id=7237, item_id=7236),
    CrateItemsRelation(id=6, crate_id=7237, item_id=7235),
    CrateItemsRelation(id=7, crate_id=8313, item_id=10007),
    CrateItemsRelation(id=8, crate_id=8313, item_id=8310),
    CrateItemsRelation(id=9, crate_id=6987, item_id=6956),
    CrateItemsRelation(id=10, crate_id=6987, item_id=6963),
    CrateItemsRelation(id=11, crate_id=6983, item_id=6934),
    CrateItemsRelation(id=12, crate_id=6988, item_id=6950),
    CrateItemsRelation(id=13, crate_id=6988, item_id=6947),
    CrateItemsRelation(id=14, crate_id=6990, item_id=6956),
    CrateItemsRelation(id=15, crate_id=6990, item_id=6944),
    CrateItemsRelation(id=16, crate_id=6990, item_id=6941),
    CrateItemsRelation(id=17, crate_id=6992, item_id=6944),
    CrateItemsRelation(id=18, crate_id=6994, item_id=6941)
]

for rarity in rarities:
    s.merge(rarity)
for platform in platforms:
    s.merge(platform)
for relation in crateItems:
    s.merge(relation)
s.commit()