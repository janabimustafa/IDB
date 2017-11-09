from requests import Session
import datetime
import re
import json
import os
import hashlib
WIKIA_API = 'http://rocketleague.wikia.com/api/v1/'

# Names of category pages mapped to the Category of object
CATEGORIES = {'Crates': 'Crate', 'Decals': 'Decal', 'Bodies': 'Body', 'Wheels': 'Wheel', 'Images - antennas': 'Antenna', 'Toppers': 'Topper', 'Images - trails': 'Boost', 'Arenas': 'Arena'}

# Antenna and Trail objects have a title of '<Name> antenna/trail.png' because they're just pictures
REPLACEMENTS = {'Antenna': ' antenna', 'Boost': ' trail'}

NO_DESCRIPT = {'Antenna', 'Trail'}

session = Session()

all_objects = {}
category_sets = {}


def get_hash(name):
    return int(hashlib.sha256(name.strip().lower().encode('utf-8')).hexdigest(), 16) % 10**8

class ImportableObject:

    def __init__(self, type, id, name=None, related=None, description=None, image=None):
        self.type = type
        self.id = id
        self.release_date = ""
        prop = get_properties_from_id(id)

        if name is None:
            if type in REPLACEMENTS:
                self.name = re.sub(REPLACEMENTS[type] + '.*', '', prop.get('title'))
            else:
                self.name = prop.get('title')
        else:
            self.name = name
        # create a new database ID for bodies. Used for scraping Decal relations
        if not type == 'Crate':
            self.id = get_hash(self.type.lower()+self.name.lower())

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


    # More for debug, allows str(ImportableObject)
    def __repr__(self):
        return str(self.id) + ": " + str(self.name) + " (" + str(self.type) + ")"


    # Serializes an Object to JSON for database storaage
    def serialize(self):
        return json.dumps({'id': self.id, 'name': self.name, 'type': self.type, 'release_date':self.release_date, 'related': list(self.related), 'description': self.description, 'image': self.image})


    # Deserializes an object, only really used for caching
    def deserialize(s):
        j = json.loads(s)
        return ImportableObject.GetObject(j['type'], j['id'], j['name'], set(j['related']), j['description'], j['image'])


    # Static factory
    def GetObject(type, id, name=None, related=None, description=None, image=None):
        if id in all_objects:
            return all_objects[id]

        n = ImportableObject(type, id, name, related, description, image)
        n.SetReleaseDate()
        all_objects[id] = n
        if type not in category_sets:
            category_sets[type] = {}
        category_sets[type] = n
        return n

    def SetReleaseDate(self):
        MONTHS = {  'January' : 1, 
                'February': 2,
                'March' : 3, 
                'April' : 4, 
                'May' : 5, 
                'June' : 6, 
                'July' : 7, 
                'August' : 8, 
                'September' : 9, 
                'October' : 10, 
                'November' : 11, 
                'December' : 12 }
        delimiter = 'released on '
        index = self.description.find(delimiter)
        if (index > -1): # Release date mentioned in description
            max_len = 19 # max length of a date is "September, 30, 2017" characters long
            start = index + delimiter.__len__()
            end = start + max_len
            substring = self.description[start:end]
            substring = substring.replace(",", "") # "September 30 2017. <...>"
            substring = substring.replace(".", "") # "September 30 2017 <...>"
            date_parts = substring.split() # ['September', '30', '2017']
            if (date_parts[1].isdigit() and date_parts[2].isdigit()): # make sure the day and year are numbers
                releaseDate = datetime.date(int(date_parts[2]), MONTHS[date_parts[0]], int(date_parts[1])) # Year, Month, Day
                self.release_date = str(releaseDate)



# Generator for ids related objects
# I'm not entirely sure what 'related' means, and the api doesn't give any context.
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
    for cat in CATEGORIES:
        for i in get_objects_from_category(cat):
            ImportableObject.GetObject(CATEGORIES[cat], i)

    for rlid in all_objects:
        for relid in get_related_objects(rlid):
            if relid in all_objects:
                all_objects[rlid].related.add(relid)


    with open('serial.txt', 'w') as f:
        for rl in all_objects.values():
            f.write(rl.serialize() + '\n')
