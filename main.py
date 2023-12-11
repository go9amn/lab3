import os
import kubernetes.client

from dotenv import load_dotenv
from kubernetes.client.rest import ApiException
from pprint import pprint


load_dotenv()


configuration = kubernetes.client.Configuration()
# Configure API key authorization: BearerToken
configuration.api_key['authorization'] = os.getenv('TOKEN')
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'


with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.WellKnownApi(api_client)

    try:
        api_response = api_instance.get_service_account_issuer_open_id_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
