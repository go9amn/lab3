from kubernetes import client, config

def get_pod_resources(namespace, pod_name):
    # Загрузка конфигурации Kubernetes из текущего контекста
    config.load_kube_config()

    # Создание объекта для взаимодействия с API Kubernetes
    v1 = client.CoreV1Api()

    try:
        # Получение информации о поде
        pod = v1.read_namespaced_pod(name=pod_name, namespace=namespace)

        # Получение ресурсов CPU и памяти из спецификации пода
        cpu = pod.spec.containers[0].resources.requests['cpu']
        memory = pod.spec.containers[0].resources.requests['memory']

        return {'cpu': cpu, 'memory': memory}

    except client.ApiException as e:
        print(f"Exception when calling CoreV1Api->read_namespaced_pod: {e}")
        return None


if __name__ == '__main__':
    namespace = 'default'  # Замените на нужное вам пространство имен (namespace)
    pod_name = 'worker1'  # Замените на имя вашего пода

    resources = get_pod_resources(namespace, pod_name)
    if resources:
        print(f"Ресурсы для пода {pod_name} в пространстве имен {namespace}:")
        print(f"CPU: {resources['cpu']}")
        print(f"Memory: {resources['memory']}")
