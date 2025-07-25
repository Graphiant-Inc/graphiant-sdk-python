# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action import V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction

class TestV1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction(unittest.TestCase):
    """V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction:
        """Test V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction`
        """
        model = V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction()
        if include_optional:
            return V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction(
                backup_circuit = graphiant_sdk.models._v1_portal_apikeys_post_request._v1_portal_apikeys_post_request(
                    name = 'example string', ),
                backup_circuit_label = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_backup_circuit_label._v1_global_config_patch_request_trafficPolicies_trafficRulesets_value_ruleset_rules_value_rule_action_backupCircuitLabel(
                    ipsec_label = 'ENUM_VALUE', 
                    label = 'ENUM_VALUE', ),
                egress = 'ENUM_VALUE',
                logging = True,
                primary_circuit = graphiant_sdk.models._v1_portal_apikeys_post_request._v1_portal_apikeys_post_request(
                    name = 'example string', ),
                primary_circuit_label = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_backup_circuit_label._v1_global_config_patch_request_trafficPolicies_trafficRulesets_value_ruleset_rules_value_rule_action_backupCircuitLabel(
                    ipsec_label = 'ENUM_VALUE', 
                    label = 'ENUM_VALUE', ),
                remark = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_remark._v1_global_config_patch_request_trafficPolicies_trafficRulesets_value_ruleset_rules_value_rule_action_remark(
                    val = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_dscp_match._v1_global_config_patch_request_trafficPolicies_securityRulesets_value_ruleset_rules_value_rule_match_dscp_match(
                        code_point = 123, ), ),
                set_sla_class = graphiant_sdk.models._v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action_set_sla_class._v1_global_config_patch_request_trafficPolicies_trafficRulesets_value_ruleset_rules_value_rule_action_setSlaClass(
                    class = 'ENUM_VALUE', )
            )
        else:
            return V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction(
        )
        """

    def testV1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction(self):
        """Test V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
