# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_bucket_app_servers_all_get200_response import V2AssuranceBucketAppServersAllGet200Response

class TestV2AssuranceBucketAppServersAllGet200Response(unittest.TestCase):
    """V2AssuranceBucketAppServersAllGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceBucketAppServersAllGet200Response:
        """Test V2AssuranceBucketAppServersAllGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceBucketAppServersAllGet200Response`
        """
        model = V2AssuranceBucketAppServersAllGet200Response()
        if include_optional:
            return V2AssuranceBucketAppServersAllGet200Response(
                app_server_changes = [
                    graphiant_sdk.models._v2_assurance_bucket_app_servers_all_get_200_response_app_server_changes_inner._v2_assurance_bucket_app_servers_all_get_200_response_appServerChanges_inner(
                        added_servers = [
                            graphiant_sdk.models._v2_assurance_bucket_app_servers_all_get_200_response_app_server_changes_inner_added_servers_inner._v2_assurance_bucket_app_servers_all_get_200_response_appServerChanges_inner_addedServers_inner(
                                server_ip = 'example string', 
                                server_port = 'example string', 
                                server_protocol = 'example string', )
                            ], 
                        app = graphiant_sdk.models._v2_assurance_bucket_app_servers_all_get_200_response_app_server_changes_inner_app._v2_assurance_bucket_app_servers_all_get_200_response_appServerChanges_inner_app(
                            app_name = 'example string', 
                            bucket_id = 'ENUM_VALUE', ), 
                        removed_servers = [
                            graphiant_sdk.models._v2_assurance_bucket_app_servers_all_get_200_response_app_server_changes_inner_added_servers_inner._v2_assurance_bucket_app_servers_all_get_200_response_appServerChanges_inner_addedServers_inner(
                                server_ip = 'example string', 
                                server_port = 'example string', 
                                server_protocol = 'example string', )
                            ], )
                    ]
            )
        else:
            return V2AssuranceBucketAppServersAllGet200Response(
        )
        """

    def testV2AssuranceBucketAppServersAllGet200Response(self):
        """Test V2AssuranceBucketAppServersAllGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
