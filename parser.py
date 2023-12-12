import os
import json


def get_stats():
    output = os.popen('kubectl get --raw "/api/v1/nodes/worker1/proxy/stats/summary"').read()
    output_json = json.loads(output)
    print(output_json['node']['nodeName'], output_json['node']['cpu']['usageNanoCores'], output_json['node']['memory']['workingSetBytes'],)
    return (
        output_json['node']['nodeName'],
        output_json['node']['cpu']['usageNanoCores'],
        output_json['node']['memory']['workingSetBytes'],
    )