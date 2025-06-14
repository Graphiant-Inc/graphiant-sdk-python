# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_topology_overview_post200_response_topology_edges_inner import V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner

class TestV2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner(unittest.TestCase):
    """V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner:
        """Test V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner`
        """
        model = V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner()
        if include_optional:
            return V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner(
                destination_node_id = 'example string',
                performance = [
                    graphiant_sdk.models._v2_assurance_topology_overview_post_200_response_topology_edges_inner_performance_inner._v2_assurance_topology_overview_post_200_response_topology_edges_inner_performance_inner(
                        jitter = 12.34, 
                        latency = 12.34, 
                        loss = 12.34, )
                    ],
                source_node_id = 'example string'
            )
        else:
            return V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner(
        )
        """

    def testV2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner(self):
        """Test V2AssuranceTopologyOverviewPost200ResponseTopologyEdgesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
