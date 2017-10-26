from requests import Session
import json
from time import sleep
from statistics import mean
import random

# RLDB Bot's API key
API_KEY = 'K9QWM40INDPZ8H2KN6W34F83JC4BUBLD'

s = Session()

resp = s.get('https://api.rocketleaguestats.com/v1/data/playlists', params = {'apikey': API_KEY})

# Sleeps needed due to twice per second rate limit
sleep(.75)

game_type = {}

for desc in resp.json():
    if 'Ranked' in desc['name'] and desc['name'] not in game_type:
        game_type[desc['name']] = desc['id']

players = {}

for id_ in game_type.values():
    resp = s.get('https://api.rocketleaguestats.com/v1/leaderboard/ranked',
        params = {'apikey': API_KEY, 'playlist_id': id_})
    sleep(.75)
    for player in resp.json():
        if player['uniqueId'] not in players:
            players[player['uniqueId']] = player

ids = set()

with open('players.txt', 'w') as f:
    for player in players.values():
        out = {}
        out['name'] = player['displayName']
        out['platform'] = int(player['platform']['id'])

        # These IDs have a high probability of being unique
        # for the 300ish max players we'll have, if we wanted to deal
        # with all players, this should change
        if player['uniqueId'].isdigit():  # Sometimes uniqueId isnt a number for whatever reason
            out['id'] = int(player['uniqueId']) % 2147483647 # 2^31-1 largest prime < 2^31
        else:
            out['id'] = random.randint(0, 2147483646)
        if out['id'] in ids:
                print("Warning: Duplicate ID: " + str(out['id']))
        ids.add(out['id'])

        for i in range(5,0,-1):
            if str(i) in player['rankedSeasons']:
                out['skill_rating'] = round(mean(player['rankedSeasons'][str(i)][t]['rankPoints'] for t in player['rankedSeasons'][str(i)]))
                break
        out['wins'] = player['stats']['wins']
        out['image'] = player['avatar']
        out['type'] = 'player'
        # This has more data than we use, so extract here
        f.write(json.dumps(out))
