# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_b2b_consumer_post_request_policy_inner import V1ExtranetsB2bConsumerPostRequestPolicyInner

class TestV1ExtranetsB2bConsumerPostRequestPolicyInner(unittest.TestCase):
    """V1ExtranetsB2bConsumerPostRequestPolicyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsB2bConsumerPostRequestPolicyInner:
        """Test V1ExtranetsB2bConsumerPostRequestPolicyInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsB2bConsumerPostRequestPolicyInner`
        """
        model = V1ExtranetsB2bConsumerPostRequestPolicyInner()
        if include_optional:
            return V1ExtranetsB2bConsumerPostRequestPolicyInner(
                consumer_lan_segment = 1234567891011,
                restricted_prefixes = [
                    'example string'
                    ],
                rules = [
                    graphiant_sdk.models._v1_extranets_b2b_consumer_post_request_policy_inner_rules_inner._v1_extranets_b2b_consumer_post_request_policy_inner_rules_inner(
                        outside_nat_prefix = 'example string', 
                        service_prefix = 'example string', )
                    ]
            )
        else:
            return V1ExtranetsB2bConsumerPostRequestPolicyInner(
        )
        """

    def testV1ExtranetsB2bConsumerPostRequestPolicyInner(self):
        """Test V1ExtranetsB2bConsumerPostRequestPolicyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
