# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv3_process import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process

class TestV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process(unittest.TestCase):
    """V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process:
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process`
        """
        model = V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process()
        if include_optional:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process(
                admin_distance = 100,
                areas = [
                    graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_segments_inner_ospfv2Process_areas_inner(
                        area_id = 'example string', 
                        bfd = graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_circuits_inner_bgpNeighbors_inner_bfd(
                            enabled = True, 
                            minimum_interval = 123, 
                            multiplier = 123, ), 
                        bfd_neighbors = [
                            graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_circuits_inner_bgp_neighbors_inner_bfd_neighbor._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_circuits_inner_bgpNeighbors_inner_bfdNeighbor(
                                desired_minimum_tx_interval = 123, 
                                if_index = 123, 
                                interface = 'example string', 
                                last_updated = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                local_diag = 'ENUM_VALUE', 
                                peer_address = 'example string', 
                                remote_diag = 'ENUM_VALUE', 
                                required_minimum_rx_interval = 123, 
                                segment_name = 'example string', 
                                source_address = 'example string', 
                                state = 'ENUM_VALUE', 
                                time_in_state = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                up = True, )
                            ], 
                        id = 1234567891011, 
                        interfaces = [
                            graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_areas_inner_interfaces_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_segments_inner_ospfv2Process_areas_inner_interfaces_inner(
                                cost = 123, 
                                dead_interval = 123, 
                                dead_interval_value = 123, 
                                dr_priority = 123, 
                                hello_interval = 123, 
                                hello_interval_value = 123, 
                                id = 1234567891011, 
                                if_index = 123, 
                                interface = 'example string', 
                                max_transmission_unit = 123, 
                                mtu_ignore = True, 
                                prefix_sid = 123, 
                                retransmit_interval = 123, 
                                retransmit_interval_value = 123, 
                                type = 'ENUM_VALUE', )
                            ], 
                        name = 'example string', 
                        type = 'ENUM_VALUE', )
                    ],
                default_originate = 'ENUM_VALUE',
                id = 1234567891011,
                redistributed_protocols = [
                    graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_segments_inner_ospfv2_process_redistributed_protocols_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_segments_inner_ospfv2Process_redistributedProtocols_inner(
                        metric = 123, 
                        metric_type = 'ENUM_VALUE', 
                        redist_type = 'ENUM_VALUE', )
                    ],
                router_id = 'example string',
                version = 123
            )
        else:
            return V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process(
        )
        """

    def testV1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process(self):
        """Test V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSegmentsInnerOspfv3Process"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
