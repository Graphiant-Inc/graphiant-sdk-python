# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_zones_value_zone import V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone

class TestV1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone(unittest.TestCase):
    """V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone:
        """Test V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone`
        """
        model = V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone()
        if include_optional:
            return V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone(
                inside = 'example string',
                pairs = {
                    'key' : graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_zones_value_zone_pairs_value._v1_global_config_patch_request_trafficPolicies_zones_value_zone_pairs_value(
                        pair = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_zones_value_zone_pairs_value_pair._v1_global_config_patch_request_trafficPolicies_zones_value_zone_pairs_value_pair(
                            outside = 'example string', 
                            ruleset = 'example string', 
                            tcp_protection = True, ), )
                    }
            )
        else:
            return V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone(
        )
        """

    def testV1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone(self):
        """Test V1GlobalConfigPatchRequestTrafficPoliciesZonesValueZone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
