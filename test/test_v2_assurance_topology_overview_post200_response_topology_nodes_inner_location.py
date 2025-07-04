# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_topology_overview_post200_response_topology_nodes_inner_location import V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation

class TestV2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation(unittest.TestCase):
    """V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation:
        """Test V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation`
        """
        model = V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation()
        if include_optional:
            return V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation(
                lat = 12.34,
                long = 12.34
            )
        else:
            return V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation(
        )
        """

    def testV2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation(self):
        """Test V2AssuranceTopologyOverviewPost200ResponseTopologyNodesInnerLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
