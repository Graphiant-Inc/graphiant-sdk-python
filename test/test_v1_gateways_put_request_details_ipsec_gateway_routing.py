# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_gateways_put_request_details_ipsec_gateway_routing import V1GatewaysPutRequestDetailsIpsecGatewayRouting

class TestV1GatewaysPutRequestDetailsIpsecGatewayRouting(unittest.TestCase):
    """V1GatewaysPutRequestDetailsIpsecGatewayRouting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GatewaysPutRequestDetailsIpsecGatewayRouting:
        """Test V1GatewaysPutRequestDetailsIpsecGatewayRouting
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GatewaysPutRequestDetailsIpsecGatewayRouting`
        """
        model = V1GatewaysPutRequestDetailsIpsecGatewayRouting()
        if include_optional:
            return V1GatewaysPutRequestDetailsIpsecGatewayRouting(
                bgp = graphiant_sdk.models._v1_gateways_put_request_details_ipsec_gateway_routing_bgp._v1_gateways_put_request_details_ipsecGateway_routing_bgp(
                    address_families = {
                        'key' : graphiant_sdk.models._v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value._v1_gateways_put_request_details_ipsecGateway_routing_bgp_addressFamilies_value(
                            family = graphiant_sdk.models._v1_gateways_put_request_details_ipsec_gateway_routing_bgp_address_families_value_family._v1_gateways_put_request_details_ipsecGateway_routing_bgp_addressFamilies_value_family(
                                address_family = 'ENUM_VALUE', 
                                inbound_policy = graphiant_sdk.models._v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_call_policy._v1_global_config_patch_request_routingPolicies_value_policy_statements_value_statement_actions_value_action_callPolicy(
                                    policy = 'example string', ), 
                                outbound_policy = graphiant_sdk.models._v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_call_policy._v1_global_config_patch_request_routingPolicies_value_policy_statements_value_statement_actions_value_action_callPolicy(
                                    policy = 'example string', ), ), )
                        }, 
                    hold_timer = 123, 
                    keepalive_timer = 123, 
                    md5_password = graphiant_sdk.models._v1_gateways_put_request_details_ipsec_gateway_routing_bgp_md5_password._v1_gateways_put_request_details_ipsecGateway_routing_bgp_md5Password(), 
                    peer_asn = 123, 
                    send_community = True, ),
                static = graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_ipsec_tunnels_inner_static._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_ipsecTunnels_inner_static(
                    destination_prefix = [
                        'example string'
                        ], )
            )
        else:
            return V1GatewaysPutRequestDetailsIpsecGatewayRouting(
        )
        """

    def testV1GatewaysPutRequestDetailsIpsecGatewayRouting(self):
        """Test V1GatewaysPutRequestDetailsIpsecGatewayRouting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
