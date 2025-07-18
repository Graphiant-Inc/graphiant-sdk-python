# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup

class TestV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup(unittest.TestCase):
    """V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup:
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup`
        """
        model = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup()
        if include_optional:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup(
                accept_mode = True,
                allow_inter_operability = True,
                description = 'example string',
                effective_priority = 123,
                enabled = True,
                group_members = [
                    graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_group_members_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_interfaces_inner_ipv4_vrrpGroup_groupMembers_inner(
                        circuit = 'example string', 
                        device_id = 1234567891011, 
                        effective_priority = 123, 
                        hostname = 'example string', 
                        interface = 'example string', 
                        lan = 'example string', 
                        local_ip_address = 'example string', 
                        priority = 123, 
                        state = 'ENUM_VALUE', )
                    ],
                id = 1234567891011,
                name = 'example string',
                preempt = True,
                priority = 123,
                state = 'ENUM_VALUE',
                tracked_interfaces = [
                    graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_tracked_interfaces_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_interfaces_inner_ipv4_vrrpGroup_trackedInterfaces_inner(
                        interface = 'example string', 
                        priority_decrement = 123, )
                    ],
                virtual_ip_address = 'example string',
                virtual_mac_address = 'example string'
            )
        else:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup(
        )
        """

    def testV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup(self):
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInnerIpv4VrrpGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
