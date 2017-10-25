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
# updates DB to create tables that don't already exist in the DB
Base.metadata.create_all(db)

s = Session()

filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        try:
            j = json.loads(line)
        except:
            print("Error, could not parse line.")
            print(line)
        #j['id'] = id_
        if 'related' in j:
            del j['related']
        if 'type' in j:
            j['type'] = j['type'].lower()
        new = deserialize(json.dumps(j))
        if new:
            s.merge(new)

s.commit()
 