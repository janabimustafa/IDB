from requests import Session
import re
import json
import os

WIKIA_API = 'http://rocketleague.wikia.com/api/v1/'

# Names of category pages mapped to the Category of object
CATEGORIES = {'Crates': 'Crate', 'Bodies': 'Body', 'Decals': 'Decal', 'Wheels': 'Wheel', 'Images - antennas': 'Antenna', 'Toppers': 'Topper', 'Images - trails': 'Trail', 'Arenas': 'Arena'}

# Antenna and Trail objects have a title of '<Name> antenna/trail.png' because they're just pictures
REPLACEMENTS = {'Antenna': ' antenna', 'Trail': ' trail'}

NO_DESCRIPT = {'Antenna', 'Trail'}

session = Session()

all_rlobjects = {}
category_sets = {}
class RLObject:

    def __init__(self, type, id, name=None, related=None, description=None, image=None):
        self.type = type
        self.id = id
        prop = get_properties_from_id(id)

        if name is None:
            if type in REPLACEMENTS:
                self.name = re.sub(REPLACEMENTS[type] + '.*', '', prop.get('title'))
            else:
                self.name = prop.get('title')
        else:
            self.name = name

        if related is None:
            self.related = set()
        else:
            self.related = related

        if description is None:
            if type not in NO_DESCRIPT:
                self.description = prop.get('abstract')
            else:
                self.description = ""
        else:
            self.description = description

        # Image is a URL to an image
        if image is None:
            self.image = prop.get('thumbnail')
        else:
            self.image = image


    # More for debug, allows str(RLObject)
    def __repr__(self):
        return str(self.id) + ": " + str(self.name) + " (" + str(self.type) + ")"


    # Serializes an Object to JSON for database storaage
    def serialize(self):
        return json.dumps({'id': self.id, 'name': self.name, 'type': self.type, 'related': list(self.related), 'description': self.description, 'image': self.image})


    # Deserializes an object, only really used for caching
    def deserialize(s):
        j = json.loads(s)
        return RLObject.GetObject(j['type'], j['id'], j['name'], set(j['related']), j['description'], j['image'])


    # Static factory
    def GetObject(type, id, name=None, related=None, description=None, image=None):
        if id in all_rlobjects:
            return all_rlobjects[id]
        n = RLObject(type, id, name, related, description, image)
        all_rlobjects[id] = n
        if type not in category_sets:
            category_sets[type] = {}
        category_sets[type] = n
        return n


# Generator for ids related objects
# I'm not entirel y sure what 'related' means, and the api doesn't give any context.
def get_related_objects(id):
    items = session.get(WIKIA_API + 'RelatedPages/List?ids=' + str(id) + '&limit=-1').json()['items']
    for article in items[str(id)]:
        yield article['id'] # id is an int, no conversion necessary


# Generator for ids of objects in a category
def get_objects_from_category(category):
    items = session.get(WIKIA_API + 'Articles/List?expand=1&category=' + category + '&limit=1000').json()['items']
    for article in items:
        yield article['id']


# Returns a dictionary of attributes for the requested id
def get_properties_from_id(id):
    rep = session.get('http://rocketleague.wikia.com/api/v1/Articles/Details?ids=' + str(id) + '&abstract=500&width=200&height=200').json()
    return rep['items'][str(id)]


if __name__ == '__main__':
    if os.path.exists('serial.txt'):
        with open('serial.txt', 'r') as f:
            for line in f:
                RLObject.deserialize(line)

  
    for cat in CATEGORIES:
        for i in get_objects_from_category(cat):
            RLObject.GetObject(CATEGORIES[cat], i)

    for rlid in all_rlobjects:
        for relid in get_related_objects(rlid):
            if relid in all_rlobjects:
                all_rlobjects[rlid].related.add(relid)


    with open('serial.txt', 'w') as f:
        for rl in all_rlobjects.values():
            f.write(rl.serialize() + '\n')
