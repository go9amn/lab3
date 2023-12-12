from kubernetes import client, config

def get_node_load(node_name):
    try:
        # Загрузка конфигурации Kubernetes из текущего контекста
        config.load_kube_config()

        # Создание объекта для взаимодействия с API Kubernetes
        v1 = client.CoreV1Api()

        # Получение информации о ноде
        node = v1.read_node(name=node_name)

        # Извлечение ресурсов CPU
        capacity_cpu = node.status.capacity.get('cpu', 1.0)  # По умолчанию 1.0, если не удалось получить значение
        usage_cpu = node.status.allocatable.get('cpu', 0.0)

        # Расчет приблизительной нагрузки на CPU в процентах
        cpu_load_percentage = (usage_cpu / capacity_cpu) * 100.0

        # Извлечение ресурсов памяти
        capacity_memory = node.status.capacity.get('memory', 'N/A')
        usage_memory = node.status.allocatable.get('memory', 'N/A')

        return {'cpu_load_percentage': cpu_load_percentage,
                'memory_capacity': capacity_memory, 'memory_usage': usage_memory}

    except Exception as e:
        print(f"Exception: {e}")
        return None

if __name__ == '__main__':
    node_name = 'worker1'  # Замените на имя вашей ноды

    node_load = get_node_load(node_name)
    if node_load:
        print(f"Нагрузка на ноде {node_name}:")
        print(f"CPU Load Percentage: {node_load['cpu_load_percentage']:.2f}%")
        print(f"Memory Capacity: {node_load['memory_capacity']}")
        print(f"Memory Usage: {node_load['memory_usage']}")
