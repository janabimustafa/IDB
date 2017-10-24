from db_definitions import *
import sys
import json
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

if len(sys.argv) != 2:
    exit()

db = create_engine('{dialect}://{user}:{password}@{host}/{db}'.format(dialect=DB_DIALECT, user=DB_USER, password=DB_PASS, host=DB_HOST, db=DB_NAME))
Session = sessionmaker(bind=db)

if len(inspect(db).get_table_names()) == 0:
    print('No tables detected, creating...')
    Base.metadata.create_all(db)

s = Session()

filename = sys.argv[1]

id_ = 1

with open(filename, 'r') as f:
    for line in f:
        j = json.loads(line)
        j['id'] = id_
        if 'related' in j:
            del j['related']
        if 'type' in j:
            j['type'] = j['type'].lower()
        new = deserialize(json.dumps(j))
        if new:
            s.add(new)
            id_ += 1

s.commit()
 