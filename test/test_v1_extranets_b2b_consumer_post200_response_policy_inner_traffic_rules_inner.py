# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_b2b_consumer_post200_response_policy_inner_traffic_rules_inner import V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner

class TestV1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner(unittest.TestCase):
    """V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner:
        """Test V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner`
        """
        model = V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner()
        if include_optional:
            return V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner(
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
                seq = 123
            )
        else:
            return V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner(
        )
        """

    def testV1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner(self):
        """Test V1ExtranetsB2bConsumerPost200ResponsePolicyInnerTrafficRulesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
