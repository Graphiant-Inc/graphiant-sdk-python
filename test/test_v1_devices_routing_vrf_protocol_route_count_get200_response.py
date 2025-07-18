# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_routing_vrf_protocol_route_count_get200_response import V1DevicesRoutingVrfProtocolRouteCountGet200Response

class TestV1DevicesRoutingVrfProtocolRouteCountGet200Response(unittest.TestCase):
    """V1DevicesRoutingVrfProtocolRouteCountGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesRoutingVrfProtocolRouteCountGet200Response:
        """Test V1DevicesRoutingVrfProtocolRouteCountGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesRoutingVrfProtocolRouteCountGet200Response`
        """
        model = V1DevicesRoutingVrfProtocolRouteCountGet200Response()
        if include_optional:
            return V1DevicesRoutingVrfProtocolRouteCountGet200Response(
                counts = [
                    graphiant_sdk.models._v1_devices_routing_vrf_protocol_route_count_get_200_response_counts_inner._v1_devices_routing_vrf_protocol_route_count_get_200_response_counts_inner(
                        protocol = 'OSPF', 
                        route_count = graphiant_sdk.models._v1_device_routing_vrf_bgp_eibgp_route_count_get_200_response_ebgp_route_count._v1_device_routing_vrf_bgp_eibgp_route_count_get_200_response_ebgpRouteCount(
                            ipv4 = 32, 
                            ipv6 = 6532, ), )
                    ]
            )
        else:
            return V1DevicesRoutingVrfProtocolRouteCountGet200Response(
        )
        """

    def testV1DevicesRoutingVrfProtocolRouteCountGet200Response(self):
        """Test V1DevicesRoutingVrfProtocolRouteCountGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
