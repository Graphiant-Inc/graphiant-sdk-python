# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_policy_prefix_sets_post_request import V1PolicyPrefixSetsPostRequest

class TestV1PolicyPrefixSetsPostRequest(unittest.TestCase):
    """V1PolicyPrefixSetsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PolicyPrefixSetsPostRequest:
        """Test V1PolicyPrefixSetsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PolicyPrefixSetsPostRequest`
        """
        model = V1PolicyPrefixSetsPostRequest()
        if include_optional:
            return V1PolicyPrefixSetsPostRequest(
                description = 'example string',
                entries = {
                    'key' : graphiant_sdk.models._v1_policy_prefix_sets_post_request_entries_value._v1_policy_prefix_sets_post_request_entries_value(
                        ip_prefix = 'example string', 
                        mask_lower = 123, 
                        mask_upper = 123, )
                    },
                mode = 'ENUM_VALUE',
                name = 'example string',
                prefix_set_entries = {
                    'key' : graphiant_sdk.models._v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry._v1_global_config_patch_request_globalPrefixSets_value_prefixSet_entries_value_entry(
                        ip_prefix = 'example string', 
                        mask_lower = 123, 
                        mask_upper = 123, 
                        seq = 123, )
                    }
            )
        else:
            return V1PolicyPrefixSetsPostRequest(
        )
        """

    def testV1PolicyPrefixSetsPostRequest(self):
        """Test V1PolicyPrefixSetsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
