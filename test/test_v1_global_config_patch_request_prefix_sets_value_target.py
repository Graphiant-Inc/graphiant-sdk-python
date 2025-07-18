# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_config_patch_request_prefix_sets_value_target import V1GlobalConfigPatchRequestPrefixSetsValueTarget

class TestV1GlobalConfigPatchRequestPrefixSetsValueTarget(unittest.TestCase):
    """V1GlobalConfigPatchRequestPrefixSetsValueTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalConfigPatchRequestPrefixSetsValueTarget:
        """Test V1GlobalConfigPatchRequestPrefixSetsValueTarget
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalConfigPatchRequestPrefixSetsValueTarget`
        """
        model = V1GlobalConfigPatchRequestPrefixSetsValueTarget()
        if include_optional:
            return V1GlobalConfigPatchRequestPrefixSetsValueTarget(
                prefix_set = graphiant_sdk.models._v1_global_config_patch_request_prefix_sets_value_target_prefix_set._v1_global_config_patch_request_prefixSets_value_target_prefixSet(
                    description = 'example string', 
                    entries = [
                        graphiant_sdk.models._v1_global_config_patch_request_global_prefix_sets_value_prefix_set_entries_value_entry._v1_global_config_patch_request_globalPrefixSets_value_prefixSet_entries_value_entry(
                            ip_prefix = 'example string', 
                            mask_lower = 123, 
                            mask_upper = 123, 
                            seq = 123, )
                        ], 
                    mode = 'ENUM_VALUE', )
            )
        else:
            return V1GlobalConfigPatchRequestPrefixSetsValueTarget(
        )
        """

    def testV1GlobalConfigPatchRequestPrefixSetsValueTarget(self):
        """Test V1GlobalConfigPatchRequestPrefixSetsValueTarget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
