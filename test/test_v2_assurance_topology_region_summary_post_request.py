# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_topology_region_summary_post_request import V2AssuranceTopologyRegionSummaryPostRequest

class TestV2AssuranceTopologyRegionSummaryPostRequest(unittest.TestCase):
    """V2AssuranceTopologyRegionSummaryPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceTopologyRegionSummaryPostRequest:
        """Test V2AssuranceTopologyRegionSummaryPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceTopologyRegionSummaryPostRequest`
        """
        model = V2AssuranceTopologyRegionSummaryPostRequest()
        if include_optional:
            return V2AssuranceTopologyRegionSummaryPostRequest(
                region_id = 123
            )
        else:
            return V2AssuranceTopologyRegionSummaryPostRequest(
        )
        """

    def testV2AssuranceTopologyRegionSummaryPostRequest(self):
        """Test V2AssuranceTopologyRegionSummaryPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
