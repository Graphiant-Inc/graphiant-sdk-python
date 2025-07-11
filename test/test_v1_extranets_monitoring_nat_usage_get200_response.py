# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_monitoring_nat_usage_get200_response import V1ExtranetsMonitoringNatUsageGet200Response

class TestV1ExtranetsMonitoringNatUsageGet200Response(unittest.TestCase):
    """V1ExtranetsMonitoringNatUsageGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsMonitoringNatUsageGet200Response:
        """Test V1ExtranetsMonitoringNatUsageGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsMonitoringNatUsageGet200Response`
        """
        model = V1ExtranetsMonitoringNatUsageGet200Response()
        if include_optional:
            return V1ExtranetsMonitoringNatUsageGet200Response(
                allocated_count = 123,
                allocations = [
                    graphiant_sdk.models._v1_extranets_monitoring_nat_usage_get_200_response_allocations_inner._v1_extranets_monitoring_nat_usage_get_200_response_allocations_inner(
                        device_id = 1234567891011, 
                        hostname = 'example string', 
                        ip_address = 'example string', 
                        site_id = 1234567891011, 
                        site_name = 'example string', )
                    ],
                usage_count = 123
            )
        else:
            return V1ExtranetsMonitoringNatUsageGet200Response(
        )
        """

    def testV1ExtranetsMonitoringNatUsageGet200Response(self):
        """Test V1ExtranetsMonitoringNatUsageGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
