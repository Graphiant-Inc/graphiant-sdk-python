# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_communities import V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities

class TestV1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities(unittest.TestCase):
    """V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities:
        """Test V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities`
        """
        model = V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities()
        if include_optional:
            return V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities(
                community = graphiant_sdk.models._v1_global_config_patch_request_routing_policies_value_policy_statements_value_statement_actions_value_action_communities_community._v1_global_config_patch_request_routingPolicies_value_policy_statements_value_statement_actions_value_action_communities_community(
                    additive = True, 
                    community_list = [
                        'example string'
                        ], )
            )
        else:
            return V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities(
        )
        """

    def testV1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities(self):
        """Test V1GlobalConfigPatchRequestRoutingPoliciesValuePolicyStatementsValueStatementActionsValueActionCommunities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
