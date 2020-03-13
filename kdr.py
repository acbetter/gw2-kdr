import json
import datetime
from os import path

import requests


def parse_iso(text):
    # input like '2019-01-04T16:41:24Z'
    return datetime.datetime.strptime(text, '%Y-%m-%dT%H:%M:%S%z')


def get_now_iso():
    # output like 2020-03-05T08:03:38Z
    return datetime.datetime.utcnow().isoformat()[:19] + 'Z'


def init_data():
    # init data
    print(get_now_iso(), 'init data')

    # get matches data
    print(get_now_iso(), 'get matches data')
    data_matches = {}
    r = requests.get('https://api.guildwars2.com/v2/wvw/matches?ids=all')
    for i in r.json():
        match = {
            'start_time': i['start_time'],
            'end_time': i['end_time'],
            'all_worlds': i['all_worlds'],
            'deaths': i['deaths'],
            'kills': i['kills'],
            'victory_points': i['victory_points'],
            'skirmishes': [{
                'id': 1,
                'start_time': i['start_time'],
                'end_time': get_now_iso(),
                'deaths': i['deaths'],
                'kills': i['kills'],
            }]
        }
        data_matches[i['id']] = match

    # write matches data
    print(get_now_iso(), 'write matches data')
    with open('matches.json', 'w', encoding='utf-8') as file:
        json.dump(data_matches, file)
        print(get_now_iso(), 'save_data_matches')


def loop_data():
    # loop data
    now_iso = get_now_iso()
    print(get_now_iso(), 'loop data')

    # load matches data
    data_matches = {}
    with open('matches.json', 'r', encoding='utf-8') as file:
        data_matches = json.load(file)

    # get matches data
    print(get_now_iso(), 'get matches data')
    r = requests.get('https://api.guildwars2.com/v2/wvw/matches?ids=all')
    for i in r.json():
        # check na/eu reset datetime
        print(get_now_iso(), 'check na/eu reset datetime', i['end_time'])
        if parse_iso(now_iso) > parse_iso(i['end_time']):
            # update reset data
            print(get_now_iso(), 'update reset data')
            data_matches[i['id']] = {
                'start_time': i['start_time'],
                'end_time': i['end_time'],
                'all_worlds': i['all_worlds'],
                'deaths': i['deaths'],
                'kills': i['kills'],
                'victory_points': i['victory_points'],
                'skirmishes': [{
                    'id': 1,
                    'start_time': i['start_time'],
                    'end_time': get_now_iso(),
                    'deaths': i['deaths'],
                    'kills': i['kills'],
                }]
            }
        else:
            # update skirmish data
            match = data_matches[i['id']]
            print(get_now_iso(), 'update skirmish data')
            data_skirmishes = match['skirmishes']
            prev_skirmish = data_skirmishes[-1]
            next_skirmish = {
                'id': prev_skirmish['id'] + 1,
                'start_time': prev_skirmish['end_time'],
                'end_time': now_iso,
                'deaths': {},
                'kills': {}
            }
            for c in ['red', 'blue', 'green']:
                next_skirmish['deaths'][c] = i['deaths'][c] - \
                    match['deaths'][c]
                next_skirmish['kills'][c] = i['kills'][c] - match['kills'][c]
            data_skirmishes.append(next_skirmish)
            # update match data
            print(get_now_iso(), 'update match data')
            match['deaths'] = i['deaths']
            match['kills'] = i['kills']
            match['victory_points'] = i['victory_points']

    # write matches data
    print(get_now_iso(), 'write matches data')
    with open('matches.json', 'w', encoding='utf-8') as file:
        json.dump(data_matches, file)
        print(get_now_iso(), 'save_data_matches')


def my_job():
    # job run @xx:00
    print('***********************')
    print(get_now_iso(), 'job run')
    if path.exists('matches.json'):
        loop_data()
    else:
        init_data()

    # get worlds data
    print(get_now_iso(), 'get worlds data')
    r = requests.get('https://api.guildwars2.com/v2/worlds?ids=all')
    data_world = {}
    for w in r.json():
        data_world[w['id']] = {
            'name': w['name'],
            'population': w['population']
        }
    with open('worlds.json', 'w', encoding='utf-8') as file:
        json.dump(data_world, file)


if (__name__ == '__main__'):
    my_job()
