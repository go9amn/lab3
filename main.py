import datetime
import matplotlib.pyplot as plt
import psutil
import json


def get_resources() -> list:
    data = []
    now = datetime.datetime.now().second
    after = datetime.datetime.now().second + 20
    while now < after:
        date = f'{datetime.datetime.now().time().minute}.{datetime.datetime.now().time().second}'
        data.append({'time': date, 'cpu': psutil.cpu_percent(3), 'ram': psutil.virtual_memory().used / pow(1024, 2)})
        now = datetime.datetime.now().minute
        print(now)
        return data


def write_to_json(data):
    with open('outout.json', 'w') as file:
        json.dump(data, file)


def get_from_json() -> list:
    with open('outout.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def graph_from_json(file: json):
    pass


if __name__ == '__main__':
    #output_data = get_resources()
    #write_to_json(output_data)
    print(get_from_json())