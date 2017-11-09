from models import *
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, configure_mappers


'''
This file provides supplemental Rarity values for the RL Objects.
'''
configure_mappers()

Base.metadata.reflect(db)
Base.metadata.drop_all(db)
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
    Platform(id=3, name="Xbox"),
    Platform(id=4, name="All")
]

for rarity in rarities:
    s.merge(rarity)
for platform in platforms:
    s.merge(platform)
s.commit()
s.close()