# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_dns_cloudflare_servers_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner

class TestV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner(unittest.TestCase):
    """V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner:
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner`
        """
        model = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner()
        if include_optional:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner(
                circuit_name = 'example string',
                interface_name = 'example string',
                ipv4 = 'example string',
                ipv6 = 'example string',
                source = 'example string',
                stale = True,
                type = 'ENUM_VALUE'
            )
        else:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner(
        )
        """

    def testV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner(self):
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerDnsCloudflareServersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
