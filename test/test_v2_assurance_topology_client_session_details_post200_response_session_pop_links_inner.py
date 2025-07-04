# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_topology_client_session_details_post200_response_session_pop_links_inner import V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner

class TestV2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner(unittest.TestCase):
    """V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner:
        """Test V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner`
        """
        model = V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner()
        if include_optional:
            return V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner(
                first_pop_name = 'example string',
                jitter = 12.34,
                latency = 12.34,
                loss = 12.34,
                second_pop_name = 'example string'
            )
        else:
            return V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner(
        )
        """

    def testV2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner(self):
        """Test V2AssuranceTopologyClientSessionDetailsPost200ResponseSessionPopLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
