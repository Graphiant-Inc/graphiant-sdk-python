# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_extranets_monitoring_consumers_post200_response_consumers_inner import V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner

class TestV2ExtranetsMonitoringConsumersPost200ResponseConsumersInner(unittest.TestCase):
    """V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner:
        """Test V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner`
        """
        model = V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner()
        if include_optional:
            return V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner(
                id = 1234567891011,
                name = 'example string',
                vrfs = [
                    1234567891011
                    ]
            )
        else:
            return V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner(
        )
        """

    def testV2ExtranetsMonitoringConsumersPost200ResponseConsumersInner(self):
        """Test V2ExtranetsMonitoringConsumersPost200ResponseConsumersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
