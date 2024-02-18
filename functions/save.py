import json
import os
import datetime

directory = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\player_saves\\" if os.name == 'nt' \
    else f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/player_saves/"

default_load = f'{directory}default_save.json'


def save(data):
    pass


def load(save_file=default_load):
    f = open(save_file)
    data = json.load(f)
    return data
