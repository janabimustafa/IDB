from models import *
import sys
import json
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 2:
    exit()

if len(inspect(db).get_table_names()) == 0:
    print('No tables detected, creating...')
# updates DB to create tables that don't already exist in the DB
Base.metadata.create_all(db)

s = Session()

filename = sys.argv[1]

relationships = []

with open(filename, 'r') as f:
    for line in f:
        try:
            j = json.loads(line)
        except:
            print("Error, could not parse line.")
            print(line)
        if 'related' in j:
            del j['related']
        if 'type' in j:
            j['type'] = j['type'].lower()
        new = deserialize(json.dumps(j))
        if new:
            s.merge(new)
            for rel in RELATION_KEYS.get(type(new), []):
                for other_id in j.get(rel, []):
                    relationships.append((type(new), RELATION_KEY_TARGETS[rel], new.id, other_id, rel))

for tup in relationships:
    a = s.query(tup[0]).filter(tup[0].id == tup[2]).first()
    b = s.query(tup[1]).filter(tup[1].id == tup[3]).first()
    if a and b and b not in getattr(a, tup[4]):
        getattr(a, tup[4]).append(b)

s.commit()
 