# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_gateways_put_request_details_aws_transit_connection_gateway_transit_gateways_inner_vpcs_inner_subnets_inner import V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner

class TestV1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner(unittest.TestCase):
    """V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner:
        """Test V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner`
        """
        model = V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner()
        if include_optional:
            return V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner(
                cidr = 'example string',
                id = 'example string'
            )
        else:
            return V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner(
        )
        """

    def testV1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner(self):
        """Test V1GatewaysPutRequestDetailsAwsTransitConnectionGatewayTransitGatewaysInnerVpcsInnerSubnetsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
