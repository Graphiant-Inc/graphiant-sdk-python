# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_policy_prefix_sets_post200_response import V1PolicyPrefixSetsPost200Response

class TestV1PolicyPrefixSetsPost200Response(unittest.TestCase):
    """V1PolicyPrefixSetsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PolicyPrefixSetsPost200Response:
        """Test V1PolicyPrefixSetsPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PolicyPrefixSetsPost200Response`
        """
        model = V1PolicyPrefixSetsPost200Response()
        if include_optional:
            return V1PolicyPrefixSetsPost200Response(
                prefix_set = graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_prefixSets_inner(
                    description = 'example string', 
                    entries = [
                        graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_entries_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_prefixSets_inner_entries_inner(
                            id = 1234567891011, 
                            ip_prefix = 'example string', 
                            mask_lower = 123, 
                            mask_upper = 123, 
                            seq = 123, )
                        ], 
                    error_message = 'example string', 
                    global_id = 1234567891011, 
                    id = 1234567891011, 
                    mode = 'ENUM_VALUE', 
                    name = 'example string', 
                    policies = [
                        graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_prefix_sets_inner_policies_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_prefixSets_inner_policies_inner(
                            attach_point = 'ENUM_VALUE', 
                            id = 1234567891011, 
                            name = 'example string', )
                        ], 
                    policy_count = 123, 
                    status = 'ENUM_VALUE', )
            )
        else:
            return V1PolicyPrefixSetsPost200Response(
        )
        """

    def testV1PolicyPrefixSetsPost200Response(self):
        """Test V1PolicyPrefixSetsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
