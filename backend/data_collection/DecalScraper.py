import requests
import json
from lxml import etree
import re
import os
import hashlib

RL_DECAL_URL = "https://rocket-league.com/items/decals"
RARITIES = {
    'Common' : 1,
    'Uncommon' : 2,
    'Rare' : 3,
    'Very Rare' : 4,
    'Limited' : 5,
    'Premium' : 6,
    'Import' : 7,
    'Exotic' : 8,
    'Black Market' : 9
}

def get_hash(name):
    return int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16) % 10**8

class DecalObject:

    def __init__(self, type, id, name, image=None, rarity=0):
        self.type = type
        self.id = id
        self.name = name
        if image is None:
            image = ""
        else:
            self.image = image
        self.rarity = rarity


    # More for debug, allows str(ImportableObject)
    def __repr__(self):
        return str(self.id) + ": " + str(self.name) + " (" + str(self.type) + ")"


    # Serializes an Object to JSON for database storaage
    def serialize(self):
        return json.dumps({'id': self.id, 'name': self.name, 'type': self.type, 'image': self.image, 'rarity' : self.rarity})


    # Deserializes an object, only really used for caching
    def deserialize(s):
        j = json.loads(s)
        return DecalObject.GetObject(j['type'], j['id'], j['name'], j['image'], j['rarity'])


    # Static factory
    def GetObject(type, id, name=None, image=None, rarity=0):
        # if id in all_objects:
        #     return all_objects[id]
        # n = ImportableObject(type, id, name, related, description, image)
        # all_objects[id] = n
        # if type not in category_sets:
        #     category_sets[type] = {}
        # category_sets[type] = n
        # return n
        return

# decals that can be used on multiple cars. Need to guarantee we're using the same Decal objects
all_decals = [
    DecalObject('decal', get_hash('Dots'),      'Dots',      'https://rocket-league.com/content/media/items/avatar/220px/e5147b07251509216026.png', 1),    
    DecalObject('decal', get_hash('Flames'),    'Flames',    'https://rocket-league.com/content/media/items/avatar/220px/3a77a2c0181507818326.png', 1),    
    DecalObject('decal', get_hash('Lightning'), 'Lightning',  'https://rocket-league.com/content/media/items/avatar/220px/ac4f5768f71509216051.png', 1),
    DecalObject('decal', get_hash('Skulls'),    'Skulls',    'https://rocket-league.com/content/media/items/avatar/220px/d02b3129971509215270.png', 1),   
    DecalObject('decal', get_hash('Stars'),     'Stars',     'https://rocket-league.com/content/media/items/avatar/220px/09e17bf46a1509216360.png', 1),    
    DecalObject('decal', get_hash('Stripes'),   'Stripes',   'https://rocket-league.com/content/media/items/avatar/220px/6958e354d31509214827.png', 1),    
    DecalObject('decal', get_hash('Tech'),      'Tech',      'https://rocket-league.com/content/media/items/avatar/220px/a13fbc2c621509216420.png', 1),    
    DecalObject('decal', get_hash('Wings'),     'Wings',     'https://rocket-league.com/content/media/items/avatar/220px/9fd40f41f01509215299.png', 1),

    DecalObject('decal', get_hash('Funny Book'),'Funny Book',  'https://rocket-league.com/content/media/items/avatar/220px/5ed3a3db6e1499315069.png', 3),

    DecalObject('decal', get_hash('Distortion'),'Distortion',  'https://rocket-league.com/content/media/items/avatar/220px/d7374716691474311319.png', 4), 
    DecalObject('decal', get_hash('Snakeskin'), 'Snakeskin',  'https://rocket-league.com/content/media/items/avatar/220px/b1b96580d41473420476.png', 4),  

    DecalObject('decal', get_hash('Copycat'),   'Copycat',  'https://rocket-league.com/content/media/items/avatar/220px/9a177381711466510006.png', 6), 
    DecalObject('decal', get_hash('Hearts'),    'Hearts',  'https://rocket-league.com/content/media/items/avatar/220px/df89ce9d711509217269.png', 6),
    DecalObject('decal', get_hash('Tiger'),     'Tiger',  'https://rocket-league.com/content/media/items/avatar/220px/508c5e58531509217099.png', 6)            
]

body_decal_relations = []

# Scrapes through Rocket-League.com to get the names, images, and rarities of Decals
# Generates body-decal relations
def get_decals_from_rl():
    page = requests.get(RL_DECAL_URL)
    tree = etree.HTML(page.text)
    bodies = tree.xpath('//*[@id="item-display-area"]/h2')
    universal_decal_ids = []
    for index in range(1, len(bodies)+1):
        body_name = tree.xpath('//*[@id="item-display-area"]/h2[{0}]'.format(index))[0].text        
        xpath_string = '//*[@id="item-display-area"]/div[count(preceding-sibling::h2)={0}]'.format(index)
        decals = tree.xpath(xpath_string)
        for decal in decals:
            new_item = {}
            if decal.xpath('@data-name'):           
                new_item['name'] = decal.xpath('@data-name')[0]
            else:
                continue

            if get_hash(new_item['name']) in map(lambda x : x.id, all_decals):
                new_item['id'] = get_hash(new_item['name'])
                body_decal_relations.append({"from_type": "body", "from_id": get_hash(body_name), "from_relation": "decals", "to_id": new_item['id']})
                continue
            else:
                new_item['id'] = get_hash(new_item['name'] + body_name)

            new_item['rarity'] = RARITIES[decal.xpath('@data-rarity')[0]]
            if body_name == 'Universal':
                universal_decal_ids.append(new_item['id'])

            new_item['image'] = 'https://rocket-league.com' + decal.xpath('div/img/@src')[0]
            new_item['platform'] = decal.xpath('@data-platform')[0]
            new_object = DecalObject('decal', new_item['id'], new_item['name'], new_item['image'], new_item['rarity'])
            all_decals.append(new_object)

            body_decal_relations.append({"from_type": "body", "from_id": get_hash(body_name), "from_relation": "decals", "to_id": new_item['id']})

        if not body_name == 'Universal':
            for id in universal_decal_ids:
                body_decal_relations.append({"from_type": "body", "from_id": get_hash(body_name), "from_relation": "decals", "to_id": id})

if __name__ == '__main__':
    # if os.path.exists('decals.txt'):
    #     with open('decals.txt', 'r') as f:
    #         for line in f:
    #             ImportableObject.deserialize(line)

    get_decals_from_rl()
    # for x in all_decals:
    #     print(x.serialize(), end='\n')

    # for x in body_decal_relations:
    #     print(json.dumps(x) , end='\n')


    with open('decals.txt', 'w') as f:
        for x in all_decals:
            f.write(x.serialize() + '\n')

    with open('body_decals.txt', 'w') as f:
        for x in body_decal_relations:
            f.write(json.dumps(x) + '\n')