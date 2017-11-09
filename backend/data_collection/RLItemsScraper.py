import requests
import json
from lxml import etree
import re
import os
import hashlib
import copy

RL_URL = "https://rocket-league.com/items/"
RL_CATEGORIES = {'bodies': 'Body', 'wheels': 'Wheel', 'boosts': 'Boost', 'antennas': 'Antenna', 'toppers': 'Topper', 'trails': 'Trail', 'explosions': 'Explosion', 'paints': 'Paint', 'banners': 'Banner'}
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
PLATFORMS = {
    'All': 4,
    'PC': 1,
    'PS4': 2,
    'XBOX': 3
}

def get_hash(name):
    return int(hashlib.sha256(name.strip().lower().encode('utf-8')).hexdigest(), 16) % 10**8

class RLObject:

    def __init__(self, type, id, name, image=None, rarity=0, platform=4):
        self.type = type
        self.id = id
        self.name = name
        self.platform = platform
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
        return json.dumps({'id': self.id, 'name': self.name, 'type': self.type, 'image': self.image, 'rarity' : self.rarity, 'platform': self.platform})


# decals that can be used on multiple cars. Need to guarantee we're using the same Decal objects
all_items = []

# Scrapes through Rocket-League.com to get the names, images, and rarities of Decals
# Generates body-decal relations
def get_items(category):
    category_items = []
    url = RL_URL + category
    page = requests.get(url)
    tree = etree.HTML(page.text)
    items = tree.xpath('//*[@id="item-display-area"]/div[contains(@class, "item-omg-wtf-bbq")]')    
    for item in items:                        
        new_item = {}
        if item.xpath('@data-name'):           
            new_item['name'] = item.xpath('@data-name')[0]
        else:
            continue        
        new_item['id'] = get_hash(RL_CATEGORIES[category].lower()+new_item['name'])
        rarity = item.xpath('@data-rarity')[0]
        if rarity == 'Super Rare':
            new_item['rarity'] = RARITIES['Very Rare']    
        else:
            new_item['rarity'] = RARITIES[rarity]

        new_item['image'] = 'https://rocket-league.com' + item.xpath('div/img/@src')[0]
        platform = item.xpath('@data-platform')[0]
        if platform in PLATFORMS:
            new_item['platform'] = PLATFORMS[platform]
        else:
            new_item['platform'] = PLATFORMS['All']
        new_object = RLObject(RL_CATEGORIES[category], new_item['id'], new_item['name'], new_item['image'], new_item['rarity'], new_item['platform'])
        category_items.append(new_object)
    return category_items

if __name__ == '__main__':
    for category in RL_CATEGORIES:
        items = get_items(category)
        with open('{0}.txt'.format(category), 'w') as f:
            for x in items:
                f.write(x.serialize() + '\n')    