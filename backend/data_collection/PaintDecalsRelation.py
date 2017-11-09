from models import *
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, configure_mappers

s = Session()
if __name__ == '__main__':    
    decals = s.query(Decal).filter(Decal.rarity != 9).all()
    for paint in s.query(Paint):
        paint.decals = decals
        s.merge(paint)
    s.commit()
    s.close()
