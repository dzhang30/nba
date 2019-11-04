import asyncio
import os
from pprint import pprint

import requests
import pandas as pd

NBA_BASE_URL = 'https://stats.nba.com/'

def get_game_play_by_play(game_id, write_to_file_path):
    if os.path.isfile(write_to_file_path):
        return pd.read_csv(write_to_file_path)

    pbp_url = f'{NBA_BASE_URL}/playbyplayv2'
    headers = {'User-Agent': 'test',}
    params = {
        'EndPeriod': '4',
        'EndRange': '55800',
        'GameID': game_id,
        'RangeType': '2',
        'Season': '2019-20',
        'SeasonType': 'Regular Season',
        'StartPeriod': '1',
        'StartRange': '0',
    }
    response = requests.get(pbp_url, headers=headers, params=params)
    results = response.json()['resultSets']
    headers = results[0]['headers']
    plays = results[0]['rowSet']
    df = pd.DataFrame(plays, columns=headers)
    pd.to_csv(write_to_file_path, index=False)

    return df

# 'https://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=0021900069&RangeType=2&Season=2019-20&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'
if __name__ == '__main__':
    plays = get_game_play_by_play('0021900069', 'rockets_nets_pbp.csv')

    for play in plays.iter:

