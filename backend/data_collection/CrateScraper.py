import requests
import json
from lxml import etree
import re
import os
import hashlib

wikia_crates = []
crate_items = dict()
WIKIA_API = 'http://rocketleague.wikia.com/api/v1/'
session = requests.Session()
def get_hash(name):
    return int(hashlib.sha256(name.strip().lower().encode('utf-8')).hexdigest(), 16) % 10**8
def get_type(type):
    type = type.lower()
    if 'decal' in type:
        return 'decal'
    if 'wheel' in type:
        return 'wheel'
    if 'body' in type:
        return 'body'
    if 'explosion' in type:
        return 'explosion'
    if 'boost' in type:
        return 'boost'
    if 'trail' in type:
        return 'trail'
    if 'paint' in type:
        return 'paint'
    if 'banner' in type:
        return 'banner'
    raise TypeError(type)

def get_article_url(id):
    rep = session.get('{base}Articles/Details?ids={id}&abstract=500&width=200&height=200'.format(base=WIKIA_API, id=str(id))).json()    
    return rep['basepath'] + rep['items'][str(id)]['url']

def get_items_in_crate(crate):
    id = crate['id']
    article_url = get_article_url(id)
    rep = session.get(article_url).text
    tree = etree.HTML(rep)
    rows = tree.xpath('//table[@class="article-table sortable"]/tr[td]')
    for row in rows:        
        item = row[1]
        type = get_type(row[2].text.strip().lower())
        if item.tag == 'td' and (not item.text or not item.text.strip()):
            name = item[0].text.strip()
        else:            
            name = item.text.strip()
        if not id in crate_items:
            crate_items[id] = []
        crate_items[id].append(get_hash(type+name))
    


if __name__ == '__main__':
    with open('serial.txt', 'r') as f:
        for line in f:
            item = json.loads(line)
            if item['type'].lower() == 'crate':
                wikia_crates.append(item)
    
    for crate in wikia_crates:
        get_items_in_crate(crate)
    with open('crate_items.txt', 'w') as f:        
        for crate in crate_items:
            for item in crate_items[crate]:
                f.write(json.dumps({"from_type": "crate", "from_id": crate, "from_relation": "items", "to_id": item}) + '\n')            