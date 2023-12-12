from kubernetes import client, config


def get_node_resources(node_name):
    try:
        # Загрузка конфигурации Kubernetes из текущего контекста
        config.load_kube_config()

        # Создание объекта для взаимодействия с API Kubernetes
        v1 = client.CoreV1Api()

        # Получение информации о ноде
        node = v1.read_node(name=node_name)

        # Извлечение ресурсов CPU и памяти
        capacity = node.status.capacity
        cpu_capacity = capacity.get('cpu', 'N/A')
        memory_capacity = capacity.get('memory', 'N/A')

        # Извлечение ресурсов, используемых в данный момент
        usage = node.status.allocatable
        cpu_usage = usage.get('cpu', 'N/A')
        memory_usage = usage.get('memory', 'N/A')

        return {'cpu_capacity': cpu_capacity, 'memory_capacity': memory_capacity,
                'cpu_usage': cpu_usage, 'memory_usage': memory_usage}

    except Exception as e:
        print(f"Exception: {e}")
        return None


if __name__ == '__main__':
    node_name = 'worker1'  # Замените на имя вашей ноды

    node_resources = get_node_resources(node_name)
    if node_resources:
        print(f"Ресурсы на ноде {node_name}:")
        print(f"CPU Capacity: {node_resources['cpu_capacity']}")
        print(f"Memory Capacity: {node_resources['memory_capacity']}")
        print(f"CPU Usage: {node_resources['cpu_usage']}")
        print(f"Memory Usage: {node_resources['memory_usage']}")
