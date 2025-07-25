# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_interfaces_value_interface import V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface

class TestV1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface(unittest.TestCase):
    """V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface:
        """Test V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface`
        """
        model = V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface()
        if include_optional:
            return V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface(
                admin_status = True,
                alias = 'example string',
                circuit = 'example string',
                description = 'example string',
                ipsec = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_ipsec._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_ipsec(
                    anti_replay_window_size = 123, 
                    dh_group = 'ENUM_VALUE', 
                    dpd_interval = 123, 
                    encryption_alg = 'ENUM_VALUE', 
                    esn = True, 
                    ike_integrity = 'ENUM_VALUE', 
                    initiator = True, 
                    ipsec_encryption_alg = 'ENUM_VALUE', 
                    ipsec_integrity = 'ENUM_VALUE', 
                    label = 'ENUM_VALUE', 
                    local_address = 'example string', 
                    local_circuit = 'example string', 
                    local_ike_peer_identity = 'example string', 
                    perfect_forward_secrecy = 'ENUM_VALUE', 
                    preshared_key = 'example string', 
                    reauth_interval = 123, 
                    rekey_interval = 123, 
                    remote_address = 'example string', 
                    remote_ike_peer_identity = 'example string', ),
                ipv4 = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw(
                    address = graphiant_sdk.models._v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_addresses_value._v1_global_config_patch_request_snmps_value_config_engineEndpoints_value_engineEndpoint_addresses_value(), 
                    dhcp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp(
                        dhcp_client = True, 
                        dhcp_relay = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcp_relay._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcpRelay(
                            relay_servers = [
                                'example string'
                                ], ), ), 
                    vrrp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp(
                        group = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group(
                            accept_mode = True, 
                            allow_inter_operability = True, 
                            description = 'example string', 
                            enabled = True, 
                            preempt = True, 
                            priority = 123, 
                            tracked_interfaces = [
                                graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_tracked_interfaces_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_interfaces_inner_ipv4_vrrpGroup_trackedInterfaces_inner(
                                    interface = 'example string', 
                                    priority_decrement = 123, )
                                ], 
                            virtual_ip = 'example string', 
                            virtual_router_id = 123, ), ), ),
                ipv6 = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw(
                    address = graphiant_sdk.models._v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_addresses_value._v1_global_config_patch_request_snmps_value_config_engineEndpoints_value_engineEndpoint_addresses_value(), 
                    dhcp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp(
                        dhcp_client = True, 
                        dhcp_relay = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcp_relay._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcpRelay(
                            relay_servers = [
                                'example string'
                                ], ), ), 
                    vrrp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp(
                        group = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group(
                            accept_mode = True, 
                            allow_inter_operability = True, 
                            description = 'example string', 
                            enabled = True, 
                            preempt = True, 
                            priority = 123, 
                            tracked_interfaces = [
                                graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_tracked_interfaces_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_interfaces_inner_ipv4_vrrpGroup_trackedInterfaces_inner(
                                    interface = 'example string', 
                                    priority_decrement = 123, )
                                ], 
                            virtual_ip = 'example string', 
                            virtual_router_id = 123, ), ), ),
                lan = 'example string',
                lldp_enabled = True,
                loopback = True,
                max_transmission_unit = 123,
                security_zone = 'example string',
                subinterfaces = {
                    'key' : graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value(
                        interface = graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface(
                            admin_status = True, 
                            alias = 'example string', 
                            circuit = 'example string', 
                            description = 'example string', 
                            ipv4 = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw(
                                address = graphiant_sdk.models._v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_addresses_value._v1_global_config_patch_request_snmps_value_config_engineEndpoints_value_engineEndpoint_addresses_value(), 
                                dhcp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp(
                                    dhcp_client = True, 
                                    dhcp_relay = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcp_relay._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_dhcp_dhcpRelay(
                                        relay_servers = [
                                            'example string'
                                            ], ), ), 
                                vrrp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp(
                                    group = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp_group(
                                        accept_mode = True, 
                                        allow_inter_operability = True, 
                                        description = 'example string', 
                                        enabled = True, 
                                        preempt = True, 
                                        priority = 123, 
                                        tracked_interfaces = [
                                            graphiant_sdk.models._v1_extranets_get_200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner_ipv4_vrrp_group_tracked_interfaces_inner._v1_extranets_get_200_response_policies_inner_branches_excludedDevices_inner_interfaces_inner_ipv4_vrrpGroup_trackedInterfaces_inner(
                                                priority_decrement = 123, )
                                            ], 
                                        virtual_ip = 'example string', 
                                        virtual_router_id = 123, ), ), ), 
                            ipv6 = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw(), 
                            lan = 'example string', 
                            lldp_enabled = True, 
                            max_transmission_unit = 123, 
                            security_zone = 'example string', 
                            tcp_mss = 123, 
                            tcp_mss_v4 = 123, 
                            tcp_mss_v6 = 123, 
                            v4_tcp_mss = graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v4_tcp_mss._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v4TcpMss(
                                tcp_mss_v4 = 123, ), 
                            v6_tcp_mss = graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v6_tcp_mss._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v6TcpMss(
                                tcp_mss_v6 = 123, ), 
                            vlan = 123, 
                            vrrp = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_gw_gw_vrrp._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_gw_gw_vrrp(), ), )
                    },
                tcp_mss = 123,
                tcp_mss_v4 = 123,
                tcp_mss_v6 = 123,
                v4_tcp_mss = graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v4_tcp_mss._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v4TcpMss(
                    tcp_mss_v4 = 123, ),
                v6_tcp_mss = graphiant_sdk.models._v1_devices__device_id__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v6_tcp_mss._v1_devices__deviceId__config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v6TcpMss(
                    tcp_mss_v6 = 123, )
            )
        else:
            return V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface(
        )
        """

    def testV1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface(self):
        """Test V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
