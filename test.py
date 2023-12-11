from kubernetes import client, config

config.load_kube_config()

api = client.CoreV1Api()

for item in api.list_node().items:
    node = api.read_node(name=item.metadata.name)
    print(node.get('status'))
