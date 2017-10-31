from models import *
import sys
import json

if len(sys.argv) != 2:
    exit()

s = Session()

filename = sys.argv[1]

with open(filename, 'r') as f:
    for line in f:
        try:
            j = json.loads(line)
        except:
            print("Error, could not parse line.")
            print(line)
        if 'from_type' in j:
            j['from_type'] = TYPE_TO_CLASS[j['from_type'].lower()]
        if 'from_relation' in j:
            j['to_type'] = RELATION_KEY_TARGETS[j['from_relation'].lower()]
        a = s.query(j['from_type']).filter(j['from_type'].id == j['from_id']).first()
        b = s.query(j['to_type']).filter(j['to_type'].id == j['to_id']).first()
        if a and b and b not in getattr(a, j['from_relation']):
            getattr(a, j['from_relation']).append(b)

s.commit()
 