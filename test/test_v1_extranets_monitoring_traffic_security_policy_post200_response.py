# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_monitoring_traffic_security_policy_post200_response import V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response

class TestV1ExtranetsMonitoringTrafficSecurityPolicyPost200Response(unittest.TestCase):
    """V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response:
        """Test V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response`
        """
        model = V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response()
        if include_optional:
            return V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response(
                security_rules = [
                    graphiant_sdk.models._v1_extranets_monitoring_traffic_security_policy_post_200_response_security_rules_inner._v1_extranets_monitoring_traffic_security_policy_post_200_response_securityRules_inner(
                        device = graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_site_devices_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_site_devices_inner(
                            hostname = 'example string', 
                            id = 1234567891011, ), 
                        security_policy_rule = graphiant_sdk.models._v1_extranets_b2b_consumer_post_200_response_policy_inner_inbound_security_rules_inner._v1_extranets_b2b_consumer_post_200_response_policy_inner_inboundSecurityRules_inner(
                            action = 'ENUM_VALUE', 
                            implicit = True, 
                            match = graphiant_sdk.models._v1_extranets_b2b_consumer_post_200_response_policy_inner_inbound_security_rules_inner_match._v1_extranets_b2b_consumer_post_200_response_policy_inner_inboundSecurityRules_inner_match(
                                destination_port = 123, 
                                destination_prefix = 'example string', 
                                icmp_type = 123, 
                                protocol = 123, 
                                source_port = 123, 
                                source_prefix = 'example string', ), 
                            policy_rule_index = 1234567891011, 
                            seq = 123, ), 
                        vrf_name = 'example string', )
                    ],
                traffic_rules = [
                    graphiant_sdk.models._v1_extranets_monitoring_traffic_security_policy_post_200_response_traffic_rules_inner._v1_extranets_monitoring_traffic_security_policy_post_200_response_trafficRules_inner(
                        device = graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_site_devices_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_site_devices_inner(
                            hostname = 'example string', 
                            id = 1234567891011, ), 
                        traffic_policy_rule = graphiant_sdk.models._v1_extranets_b2b_consumer_post_200_response_policy_inner_traffic_rules_inner._v1_extranets_b2b_consumer_post_200_response_policy_inner_trafficRules_inner(
                            action = graphiant_sdk.models._v1_extranets_b2b_consumer_post_200_response_policy_inner_traffic_rules_inner_action._v1_extranets_b2b_consumer_post_200_response_policy_inner_trafficRules_inner_action(
                                backup = 'ENUM_VALUE', 
                                class = 'ENUM_VALUE', 
                                primary = 'ENUM_VALUE', 
                                result = 'ENUM_VALUE', ), 
                            match = graphiant_sdk.models._v1_extranets_b2b_consumer_post_200_response_policy_inner_inbound_security_rules_inner_match._v1_extranets_b2b_consumer_post_200_response_policy_inner_inboundSecurityRules_inner_match(
                                destination_port = 123, 
                                destination_prefix = 'example string', 
                                icmp_type = 123, 
                                protocol = 123, 
                                source_port = 123, 
                                source_prefix = 'example string', ), 
                            policy_rule_index = 1234567891011, 
                            seq = 123, ), 
                        vrf_name = 'example string', )
                    ]
            )
        else:
            return V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response(
        )
        """

    def testV1ExtranetsMonitoringTrafficSecurityPolicyPost200Response(self):
        """Test V1ExtranetsMonitoringTrafficSecurityPolicyPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
