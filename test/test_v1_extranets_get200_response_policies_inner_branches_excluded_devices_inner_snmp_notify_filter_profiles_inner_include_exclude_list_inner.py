# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_snmp_notify_filter_profiles_inner_include_exclude_list_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner

class TestV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner(unittest.TestCase):
    """V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner:
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner`
        """
        model = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner()
        if include_optional:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner(
                id = 1234567891011,
                include = True,
                subtree = 'example string'
            )
        else:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner(
        )
        """

    def testV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner(self):
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSnmpNotifyFilterProfilesInnerIncludeExcludeListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
