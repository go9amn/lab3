import time
import datetime
import os
import json


def get_stats(node_name: str = 'worker1') -> list:
    '''Собирает необходимые данные из нода'''
    output = os.popen(f'kubectl get --raw "/api/v1/nodes/{node_name}/proxy/stats/summary"').read()
    output_json = json.loads(output)

    print(output_json['node']['nodeName'], output_json['node']['cpu']['usageNanoCores'], output_json['node']['memory']['workingSetBytes'],)
    return [
        round(float(output_json['node']['cpu']['usageNanoCores']/4000000000) * 100, 3),
        round(float(output_json['node']['memory']['workingSetBytes'] / 1048576), 3),
    ]


def get_stats_by_time() -> list:
    '''В течении 5 минут собирает статистику и возвращает список собранных данных'''
    data = []

    now = datetime.datetime.now().minute
    after = datetime.datetime.now().minute + 5
    while now < after:
        stat = get_stats()
        stat.append(f'{datetime.datetime.now().time().minute}:{datetime.datetime.now().time().second}',)
        data.append(stat)
        now = datetime.datetime.now().minute
        print(stat)
        time.sleep(1)

    return data


def write_stats_to_json() -> None:
    '''Записывает данные в json файл'''
    with open('outout.json', 'w+', encoding='utf-8') as file:
        json.dump(get_stats_by_time(), file)


if __name__ == '__main__':
    write_stats_to_json()
