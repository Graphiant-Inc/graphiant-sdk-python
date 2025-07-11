# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_groups_id_get200_response import V1GroupsIdGet200Response

class TestV1GroupsIdGet200Response(unittest.TestCase):
    """V1GroupsIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GroupsIdGet200Response:
        """Test V1GroupsIdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GroupsIdGet200Response`
        """
        model = V1GroupsIdGet200Response()
        if include_optional:
            return V1GroupsIdGet200Response(
                group = graphiant_sdk.models._v1_groups_get_200_response_groups_inner._v1_groups_get_200_response_groups_inner(
                    description = 'example string', 
                    enterprise_ids = [
                        1234567891011
                        ], 
                    group_type = 'ENUM_VALUE', 
                    id = 'example string', 
                    name = 'example string', 
                    permissions = graphiant_sdk.models._v1_groups_get_200_response_groups_inner_permissions._v1_groups_get_200_response_groups_inner_permissions(
                        asset_manager = 'ENUM_VALUE', 
                        b2b = 'ENUM_VALUE', 
                        billing_and_invoicing = 'ENUM_VALUE', 
                        compliance = 'ENUM_VALUE', 
                        developer_tools = 'ENUM_VALUE', 
                        gateway = 'ENUM_VALUE', 
                        global_services = 'ENUM_VALUE', 
                        insights = 'ENUM_VALUE', 
                        licensing = 'ENUM_VALUE', 
                        logs = 'ENUM_VALUE', 
                        monitoring_and_troubleshooting = 'ENUM_VALUE', 
                        network_configuration = 'ENUM_VALUE', 
                        order_status = 'ENUM_VALUE', 
                        reports = 'ENUM_VALUE', 
                        safety_and_security = 'ENUM_VALUE', 
                        service_policies = 'ENUM_VALUE', 
                        support = 'ENUM_VALUE', 
                        user_and_tenant_management = 'ENUM_VALUE', ), 
                    time_window_end = 1234567891011, 
                    time_window_start = 1234567891011, )
            )
        else:
            return V1GroupsIdGet200Response(
        )
        """

    def testV1GroupsIdGet200Response(self):
        """Test V1GroupsIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
