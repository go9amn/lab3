from kubernetes import client, config


def get_pod_resources(namespace, pod_name):
    # Загрузка конфигурации Kubernetes из текущего контекста
    config.load_kube_config()

    # Создание объекта для взаимодействия с API Kubernetes
    v1 = client.CoreV1Api()
    print(v1.list_namespaced_pod())



if __name__ == '__main__':
    namespace = 'default'  # Замените на нужное вам пространство имен (namespace)
    pod_name = 'worker1'  # Замените на имя вашего пода

    resources = get_pod_resources(namespace, pod_name)
    if resources:
        print(f"Ресурсы для пода {pod_name} в пространстве имен {namespace}:")
        print(f"CPU: {resources['cpu']}")
        print(f"Memory: {resources['memory']}")
