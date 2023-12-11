import requests

url = 'https://your.kube-url.com/api/v1/namespaces/kube-system/services/http:heapster:/proxy/apis/metrics/v1alpha1/namespaces/default/pods'
headers = {'authorization': ''}
print(requests.get(url, headers=headers).json())
