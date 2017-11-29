import requests
import json
from lxml import etree
import re
import os
import hashlib
import copy


def get_hash(name):
    return int(hashlib.sha256(name.strip().lower().encode('utf-8')).hexdigest(), 16) % 10**8

#this is the only data that had to be inputted manually
dlcs = [
    {
        'id': get_hash('dlc' + 'Supersonic Fury'),
        'name': 'Supersonic Fury',
        'release_date': '2015-8-13',
        'image': 'http://www.dlcompare.com/upload/gameimage/file/7522.jpeg',
        'type': 'dlc',
        'description': 'Supersonic Fury was the first major DLC pack to be released for Rocket League.',
        'items': [
            get_hash('body' + 'Dominus'),
            get_hash('body' + 'Takumi'),
            get_hash('decal' + 'Chaser'),
            get_hash('decal' + 'Copycat'),
            get_hash('decal' + 'Crazy-8'),
            get_hash('decal' + 'Gaki'),
            get_hash('decal' + 'Reiko'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Scorpions'),
            get_hash('decal' + 'Skulls'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Tats'),
            get_hash('decal' + 'Wings'),
            get_hash('wheel' + 'Cristiano'),
            get_hash('wheel' + 'Spinner'),
            get_hash('paint' + 'wood'),
            get_hash('paint' + 'pearlescent'),
            get_hash('paint' + 'metallic pearl'),
            get_hash('paint' + 'carbon fiber'),
            get_hash('paint' + 'brushed metal'),
            get_hash('boost' + 'nitrous'),
            get_hash('boost' + 'burnout'),
        ]
    },
    {
        'id': get_hash('dlc' + 'Revenge of the Battle-Cars'),
        'name': 'Revenge of the Battle-Cars',
        'release_date': '2015-10-13',
        'image': 'http://ecx.images-amazon.com/images/I/61OeESrZ35L._SX342_QL70_.jpg',
        'type': 'dlc',
        'description': 'Revenge of the Battle-Cars was the second major DLC pack to be released for Rocket League.',
        'items': [
            get_hash('body' + 'Scarab'),
            get_hash('body' + 'Zippy'),
            get_hash('decal' + 'Chaser'),
            get_hash('decal' + 'Bomani'),
            get_hash('decal' + 'Derby Girl'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Hearts'),
            get_hash('decal' + 'Tiger'),
            get_hash('decal' + 'Tribal'),         
            get_hash('decal' + 'Caboodle'),
            get_hash('decal' + 'Callous'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Hearts'),
            get_hash('decal' + 'Leopard'),
            get_hash('decal' + 'Tiger'),
            get_hash('wheel' + 'Zippy'),
            get_hash('wheel' + 'Scarab'),
            get_hash('paint' + 'toon matte'),
            get_hash('paint' + 'toon glossy'),
            get_hash('paint' + 'toon wood'),            
            get_hash('boost' + 'Accelerato'),
            get_hash('boost' + 'Battle-Stars'),
            get_hash('topper' + 'Cavalier'),
            get_hash('topper' + 'Locomotive'),
            get_hash('topper' + 'Pixelated Shades'),
            get_hash('topper' + 'Shark Fin'),
            get_hash('antenna' + 'Retro Ball - Urban'),
            get_hash('antenna' + 'Retro Ball - Utopia'),
        ]
    },
    {
        'id': get_hash('dlc' + 'Chaos Run'),
        'name': 'Chaos Run',
        'release_date': '2015-12-1',
        'description': 'Chaos Run was the third major DLC pack added to the game.',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/0/03/Chaosr.jpg/revision/latest?cb=20161110054220',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Ripper'),
            get_hash('body' + 'Grog'),
            get_hash('decal' + 'Bomber'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Ockie'),
            get_hash('decal' + 'Shot Fox'),
            get_hash('decal' + 'Spikes'),
            get_hash('decal' + 'Tribal'),
            get_hash('decal' + 'Bomber'),
            get_hash('decal' + 'Cyclops'),
            get_hash('decal' + 'Lepus'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Tagged'),
            get_hash('decal' + 'Tribal'),
            get_hash('wheel' + 'Grog'),
            get_hash('wheel' + 'Ripper'),
            get_hash('paint' + 'Camo'),
            get_hash('paint' + 'Sun-Damaged'),       
            get_hash('boost' + 'Nuts & Bolts'),
            get_hash('boost' + 'Sandstorm'),
            get_hash('topper' + 'Boombox'),
            get_hash('topper' + 'Cow Skull'),
            get_hash('topper' + 'Mohawk'),
            get_hash('antenna' + 'Bomb Pole'),
            get_hash('antenna' + 'Radioactive'),
            get_hash('antenna' + 'Retro Ball - Wasteland'),
        ]
    },
    {
        'id': get_hash('dlc' + 'DeLorean Time Machine'),
        'release_date': '2015-10-21',
        'description': 'Great Scott! The time continuum has been disrupted and as of October 21, 2015, the "Future" is now!\nCelebrate one of the most anticipated days of the last 30 years in Rocket League with the official Back to the Future DeLorean Time Machine!\nDon\'t waste another minute. Get yours today!',
        'name': 'DeLorean Time Machine',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/9/95/DeLorean_Time_Machine_promo_art_1.jpg/revision/latest/scale-to-width-down/310?cb=20170530114548',
        'type': 'dlc',
        'items': [get_hash('body' + 'DeLorean Time Machine'), get_hash('trail' + 'DeLorean Time Machine'), get_hash('wheel' + 'DeLorean Time Machine')]
    },
    {
        'id': get_hash('dlc' + 'Batman v Superman: Dawn of Justice'),
        'description': 'Black and blue, god vs man, day vs night!\nUnleash your own one-car reign of terror with the official Batmobile Battle-Car from the upcoming blockbuster mega-film, Batman v Superman: Dawn of Justice!\nThree exclusive antenna flags to pledge your allegiance to the World\'s Finest trio of Batman, Superman, or Wonder Woman.',
        'release_date': '2016-3-8',
        'name': 'Batman v Superman: Dawn of Justice',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/3/3c/Batman_v_Superman_Dawn_of_Justice_DLC_pack.jpg/revision/latest/scale-to-width-down/310?cb=20170710214612',
        'type': 'dlc',
        'items': [get_hash('body' + 'Batmobile'), get_hash('trail' + 'Batmobile'), get_hash('wheel' + 'Batmobile'), get_hash('boost' + 'Batmobile'), get_hash('antenna' + 'batman'), get_hash('antenna' + 'superman'), get_hash('antenna' + 'wonder woman')]
    },
    {
        'id': get_hash('dlc' + 'Aftershock'),
        'name': 'Aftershock',
        'description': 'Drive the fan-favorite, jet-inspired dynamo, Aftershock, and relive the glory days of the original Supersonic Acrobatic Rocket-Powered Battle-Cars, today!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/2/2e/Aftershock_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170531180331',
        'type': 'dlc',
        'release_date': '2016-7-18',
        'items': [
            get_hash('body' + 'Aftershock'),            
            get_hash('wheel' + 'Aftershock'),       
            get_hash('decal' + 'Copycat'),
            get_hash('decal' + 'MIRV'),
            get_hash('decal' + 'Seismic'),
            get_hash('decal' + 'Tiger'),
            get_hash('decal' + 'Tribal'),
            get_hash('decal' + 'Wings'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Marauder'),
        'name': 'Marauder',
        'description': 'Because you demanded it, a Supersonic Acrobatic Rocket-Powered Battle-Cars classic, the monstrous Marauder, returns to the pitch!',
        'release_date': '2016-7-18',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/7/79/Marauder_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170531202512',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Marauder'),            
            get_hash('wheel' + 'Marauder'),       
            get_hash('decal' + 'Big Buck'),
            get_hash('decal' + 'Ruffian'),
            get_hash('decal' + 'Safari'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Vagabond'),
            get_hash('decal' + 'Wings'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Esper'),
        'name': 'Esper',
        'description': 'Taken from the streets of Japan\'s not-too-distant future, Esper combines roadster and motorcycle for the coolest ride in the apocalypse!',
        'release_date': '2016-7-18',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/3/3b/Esper_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170601160548',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Esper'),            
            get_hash('wheel' + 'Esper'),       
            get_hash('decal' + 'Kaiju'),
            get_hash('decal' + 'Mouse Cat'),
            get_hash('decal' + 'Neo'),
            get_hash('decal' + 'Pegasus'),
            get_hash('decal' + 'Shank'),
            get_hash('decal' + 'Super F3'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Masamune'),
        'name': 'Masamune',
        'release_date': '2016-7-18',
        'description': 'Use the science of aerodynamics and slice through the competition with Masamune, a cutting-edge racer from the streets of Neo Tokyo!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/8/81/Masamune_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170601162859',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Masamune'),            
            get_hash('wheel' + 'Masamune'),       
            get_hash('decal' + 'DJ Sushi'),
            get_hash('decal' + 'Otaku'),
            get_hash('decal' + 'Road Rage'),
            get_hash('decal' + 'Stars'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Wildfire'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Proteus'),
        'name': 'Proteus',
        'description': 'From the darkest fathoms of the ocean comes Proteus, an imposing deep-sea diver built to handle pressure!',
        'release_date': '2016-10-4',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/c/cf/Proteus_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170602180338',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Proteus'),            
            get_hash('wheel' + 'Proteus'),       
            get_hash('decal' + 'Crash Dive'),
            get_hash('decal' + 'Cuttle Time'),
            get_hash('decal' + 'Fathom'),
            get_hash('decal' + 'Ladybug'),
            get_hash('decal' + 'Stripes'),
            get_hash('decal' + 'Tiger Shark'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Triton'),
        'name': 'Triton',
        'release_date': '2016-10-4',
        'description': 'Embrace your inner sea god and rule the high seas with Triton, the AquaDome\'s sleekest submersible Battle-Car!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/9/94/Triton_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170602185705',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Triton'),            
            get_hash('wheel' + 'Triton'),       
            get_hash('decal' + 'Daddy-O'),
            get_hash('decal' + 'Fugu'),
            get_hash('decal' + 'Makai'),
            get_hash('decal' + 'Modus Bestia'),
            get_hash('decal' + 'Ragnarok'),
            get_hash('decal' + 'Stripes'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Vulcan'),
        'name': 'Vulcan',
        'release_date': '2016-12-6',
        'description': 'Defend the universe (and your goal line) with Vulcan, the most elite sports-craft in the galaxy!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/6/64/Vulcan_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170529185045',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Vulcan'),            
            get_hash('wheel' + 'Vulcan'),       
            get_hash('decal' + 'ARC'),
            get_hash('decal' + 'Armada'),
            get_hash('decal' + 'Combat'),
            get_hash('decal' + 'Cryo-Flames'),
            get_hash('decal' + 'Medic'),
            get_hash('decal' + 'Space Worm'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'TWIN MILL III'),
        'name': 'Twin Mill III',
        'release_date': '2017-02-21',
        'description': 'Powered by not one, but TWO blown big-block engines and dual front intakes, Hot Wheels® world famous Twin Mill™ III has arrived!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/3/30/Twin_Mill_III_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170611140210',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'TWIN MILL III'),            
            get_hash('wheel' + 'OH5'),       
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Javelin'),
            get_hash('decal' + 'Overline'),
            get_hash('decal' + 'Primo'),
            get_hash('decal' + 'Pyro'),
            get_hash('decal' + 'Speedster'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Bone Shaker'),
        'name': 'Bone Shaker',
        'description': 'Take control of the field with one of the most beloved hot rods of all time, the Hot Wheels® Bone Shaker™!',
        'release_date': '2017-02-21',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/4/41/Bone_Shaker_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170611123904',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Bone Shaker'),            
            get_hash('wheel' + 'WW5SP'),       
            get_hash('decal' + 'Bone Jack'),
            get_hash('decal' + 'Diablo'),
            get_hash('decal' + 'Inferno'),
            get_hash('decal' + 'Pro-Street'),
            get_hash('decal' + 'Starstruck'),
            get_hash('decal' + 'Stripes'),        
        ]
    },
    {
        'id': get_hash('dlc' + 'Ice Charger'),
        'name': 'Ice Charger',
        'release_date': '2017-04-04',
        'description': 'Now you can own Dom Toretto\'s Dodge Ice Charger from Universal Pictures\' explosive movie, The Fate of the Furious.',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/6/68/Ice_Charger_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20170530130044',
        'type': 'dlc',
        'items': [
            get_hash('body' + 'Ice Charger'),            
            get_hash('decal' + 'CDXL'),
            get_hash('decal' + 'Clean Cut'),
            get_hash('decal' + 'Crazy Sandwich'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Rakugaki'),
            get_hash('decal' + 'Rally'),        
        ]
    },
    {
        'id': get_hash('dlc' + '\'70 DODGE CHARGER R-T'),
        'name': '\'70 Dodge Charger R-T',
        'release_date': '2017-10-11',
        'description': 'Challenge the rules with Dom Toretto\'s 1970 Dodge Charger R/T from from the film that launched the epic saga, The Fast and the Furious, by Universal Pictures.',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/4/49/%2770_Dodge_Charger_RT_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20171004211508',
        'type': 'dlc',
        'items': [
            get_hash('body' + '\'70 Dodge Charger R-T'),            
            get_hash('wheel' + '\'70 Dodge Charger R-T'),
            get_hash('decal' + 'Alameda Twin'),
            get_hash('decal' + 'Good Graces'),
            get_hash('decal' + 'Flames'),
            get_hash('decal' + 'Rally'),
            get_hash('decal' + 'Sinclair'),
            get_hash('decal' + 'Wheelman'),        
        ]
    },
    {
        'id': get_hash('dlc' + '\'99 Nissan Skyline GT-R R34'),
        'name': '\'99 Nissan Skyline GT-R R34',
        'release_date': '2017-10-11',
        'description': 'Rev up Brian O\'Conner\'s 1999 Nissan Skyline GT-R R34 from Universal Pictures\' 2 Fast 2 Furious!',
        'image': 'https://vignette.wikia.nocookie.net/rocketleague/images/a/a5/%2799_Nissan_Skyline_GT-R_R34_hero_art.jpg/revision/latest/scale-to-width-down/310?cb=20171004211431',
        'type': 'dlc',
        'items': [
            get_hash('body' + '\'99 Nissan Skyline GT-R R34'),            
            get_hash('wheel' + '\'99 Nissan Skyline GT-R R34'),
            get_hash('decal' + '2Bold'),
            get_hash('decal' + '2Cool'),
            get_hash('decal' + '2Tuff'),
            get_hash('decal' + 'Clean Cut'),
            get_hash('decal' + 'Home Stretch'),
            get_hash('decal' + 'The Clutch'),        
        ]
    }
]

if __name__ == '__main__':
    with open('dlcs_items.txt', 'w') as f:
        for dlc in dlcs:
            for item in dlc['items']:
                item_dlc = {"from_type": "dlc", "from_id": dlc['id'], "from_relation": "items", "to_id": item}
                f.write(json.dumps(item_dlc)+'\n')
    with open('dlcs.txt', 'w') as f:
        for dlc in dlcs:
            del dlc['items']
            f.write(json.dumps(dlc)+'\n')
