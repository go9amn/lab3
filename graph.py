import json

import matplotlib.pyplot as pl


def get_data_from_json():
    with open('outout.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


get_data_from_json()