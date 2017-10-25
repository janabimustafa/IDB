from requests import Session
from collections import defaultdict
import json

def get_about_stats():
    s = Session()

    commits = s.get('https://api.github.com/repos/janabimustafa/IDB/commits').json()

    git_stats = defaultdict(int)
    num_commits = 0

    for commit in commits:
        if not commit["commit"]["message"].startswith('Merge pull request'):
            git_stats[commit["commit"]["author"]["name"]] += 1
            num_commits += 1


    trello_stats = defaultdict(int)
    num_issues = 0

    member_names = {}

    LIST_IDs = [
        '59c1b5da4cf5c473d942972e', # Proj 2 master/prod
        '59e93c4769cc96f17177fc3f', # Proj 3 master/prod
    ]

    # API Key and token for RLDB Bot account
    API_KEY = '7883608772d41cef4538aa75fa0187f9'
    API_TOKEN = '4963996f31a4ebb2446a437f256070c6da4db1c5e86d8fbb26405ed8a343e431'

    for LID in LIST_IDs:
        cards = s.get('https://api.trello.com/1/lists/{0}/cards?key={1}&token={2}'.format(
            LID, API_KEY, API_TOKEN)).json()

        for card in cards:
            num_issues += 1
            for member_id in card['idMembers']:
                if member_id in member_names:
                    trello_stats[member_names[member_id]] += 1
                else:
                    name = s.get('https://api.trello.com/1/members/{0}?key={1}&token={2}'.format(
                        member_id, API_KEY, API_TOKEN)).json()['fullName']
                    member_names[member_id] = name
                    trello_stats[name] += 1

    package = {'commits': git_stats, 'num_commits': num_commits, 'issues': trello_stats, 'num_issues': num_issues}

    return package