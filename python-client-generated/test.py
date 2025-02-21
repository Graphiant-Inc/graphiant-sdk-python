from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# custom host
configuration = swagger_client.Configuration()
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer gr-auth-0d2bb29d-c810-478b-988b-1840912401bc-38f58c18-78e9-4513-8610-4ba3b61bae82'

api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    body = swagger_client.AuthLoginBody(username="due@graphiant.com", password="Demo123!")
    api_response = api_instance.v1_auth_login_post(body=body, _preload_content=False)

    print(api_response)
    # api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
    # api_response = api_instance.v1_edges_summary_get()
    # pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
