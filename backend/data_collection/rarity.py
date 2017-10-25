from db_definitions import *
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker


'''
This file provides supplemental Rarity values for the RL Objects.
'''

db = create_engine('{dialect}://{user}:{password}@{host}/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, host=DB_HOST, db=DB_NAME))
Session = sessionmaker(bind=db)
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

for rarity in rarities:
    s.add(rarity)
s.commit()