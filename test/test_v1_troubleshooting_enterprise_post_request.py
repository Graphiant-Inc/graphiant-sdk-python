# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_troubleshooting_enterprise_post_request import V1TroubleshootingEnterprisePostRequest

class TestV1TroubleshootingEnterprisePostRequest(unittest.TestCase):
    """V1TroubleshootingEnterprisePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1TroubleshootingEnterprisePostRequest:
        """Test V1TroubleshootingEnterprisePostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1TroubleshootingEnterprisePostRequest`
        """
        model = V1TroubleshootingEnterprisePostRequest()
        if include_optional:
            return V1TroubleshootingEnterprisePostRequest(
                dimensions = graphiant_sdk.models._v1_troubleshooting_enterprise_post_request_dimensions._v1_troubleshooting_enterprise_post_request_dimensions(
                    certificate_expiry = True, 
                    core_connectivity = True, 
                    core_transitions = True, 
                    cpu = True, 
                    crashes = True, 
                    credit_expiry = True, 
                    disk = True, 
                    fan_speed = True, 
                    license_expiry = True, 
                    memory = True, 
                    odp_connectivity = True, 
                    odp_transitions = True, 
                    sla_performance = True, 
                    t2_connectivity = True, 
                    t2_transitions = True, 
                    temperature = True, ),
                filter = graphiant_sdk.models._v1_backbone_health_overview_post_request_filter._v1_backbone_health_overview_post_request_filter(
                    circuit_names = [
                        'example string'
                        ], 
                    device_ids = [
                        1234567891011
                        ], 
                    lan_segments = [
                        'example string'
                        ], 
                    region_ids = [
                        1234567891011
                        ], 
                    site_ids = [
                        1234567891011
                        ], )
            )
        else:
            return V1TroubleshootingEnterprisePostRequest(
        )
        """

    def testV1TroubleshootingEnterprisePostRequest(self):
        """Test V1TroubleshootingEnterprisePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
