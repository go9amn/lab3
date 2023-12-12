import datetime
import os
import json


def get_stats() -> list:
    output = os.popen('kubectl get --raw "/api/v1/nodes/worker1/proxy/stats/summary"').read()
    output_json = json.loads(output)
    print(output_json['node']['nodeName'], output_json['node']['cpu']['usageNanoCores'], output_json['node']['memory']['workingSetBytes'],)
    return [
        output_json['node']['nodeName'],
        output_json['node']['cpu']['usageNanoCores'],
        output_json['node']['memory']['workingSetBytes'],
    ]


def get_stats_by_time() -> list:
    data = []

    now = datetime.datetime.now().minute
    after = datetime.datetime.now().minute + 5
    while now < after:
        data.append(get_stats().append(
                int(f'{datetime.datetime.now().time().minute}.{datetime.datetime.now().time().second}'),
            )
        )
        now = datetime.datetime.now().minute

        return data


def write_stats_to_json() -> None:
    with open('outout.json', 'w+', encoding='utf-8') as file:
        json.dump(get_stats_by_time(), file)


if __name__ == '__main__':
    write_stats_to_json()
