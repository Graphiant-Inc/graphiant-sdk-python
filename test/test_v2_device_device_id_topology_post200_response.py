# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_device_device_id_topology_post200_response import V2DeviceDeviceIdTopologyPost200Response

class TestV2DeviceDeviceIdTopologyPost200Response(unittest.TestCase):
    """V2DeviceDeviceIdTopologyPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2DeviceDeviceIdTopologyPost200Response:
        """Test V2DeviceDeviceIdTopologyPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2DeviceDeviceIdTopologyPost200Response`
        """
        model = V2DeviceDeviceIdTopologyPost200Response()
        if include_optional:
            return V2DeviceDeviceIdTopologyPost200Response(
                edges = [
                    graphiant_sdk.models._v2_device__device_id__topology_post_200_response_edges_inner._v2_device__deviceId__topology_post_200_response_edges_inner(
                        a = 123, 
                        b = 123, 
                        circuits_info = [
                            graphiant_sdk.models._v2_device__device_id__topology_post_200_response_edges_inner_circuits_info_inner._v2_device__deviceId__topology_post_200_response_edges_inner_circuitsInfo_inner(
                                circuit_carrier = 'example string', 
                                circuit_name = 'example string', 
                                device_hostname = 'example string', 
                                interface_name = 'example string', 
                                label = 'ENUM_VALUE', 
                                last_resort_circuit = True, 
                                quality = 'ENUM_VALUE', 
                                source_ip = 'example string', 
                                source_public_ip = 'example string', 
                                uptime = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), )
                            ], 
                        connections = [
                            graphiant_sdk.models._v2_device__device_id__topology_post_200_response_edges_inner_connections_inner._v2_device__deviceId__topology_post_200_response_edges_inner_connections_inner(
                                active = True, 
                                circuit_carrier = 'example string', 
                                circuit_name = 'example string', 
                                destination_ip = 'example string', 
                                hostname = 'example string', 
                                last_established_time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                last_resort = True, 
                                quality = 'ENUM_VALUE', 
                                source_ip = 'example string', 
                                source_public_ip = 'example string', )
                            ], 
                        name = 'example string', 
                        quality = 'ENUM_VALUE', )
                    ],
                nodes = [
                    graphiant_sdk.models._v2_device__device_id__topology_post_200_response_nodes_inner._v2_device__deviceId__topology_post_200_response_nodes_inner(
                        circuit_info = [
                            graphiant_sdk.models._v2_device__device_id__topology_post_200_response_nodes_inner_circuit_info_inner._v2_device__deviceId__topology_post_200_response_nodes_inner_circuitInfo_inner(
                                average_downlink_utilization = 123.45, 
                                average_uplink_utilization = 123.45, 
                                circuit_carrier = 'example string', 
                                circuit_name = 'example string', 
                                current_downlink_utilization = 123.45, 
                                current_uplink_utilization = 123.45, 
                                device_id = 1234567891011, 
                                interface_name = 'example string', 
                                jitter = 12345678910, 
                                label = 'ENUM_VALUE', 
                                last_resort = True, 
                                latency = 12345678910, 
                                loss = 12.34, 
                                qoe = 12.34, 
                                quality = 'ENUM_VALUE', )
                            ], 
                        connections = [
                            graphiant_sdk.models._v2_device__device_id__topology_post_200_response_edges_inner_connections_inner._v2_device__deviceId__topology_post_200_response_edges_inner_connections_inner(
                                active = True, 
                                circuit_carrier = 'example string', 
                                circuit_name = 'example string', 
                                destination_ip = 'example string', 
                                hostname = 'example string', 
                                last_established_time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                last_resort = True, 
                                quality = 'ENUM_VALUE', 
                                source_ip = 'example string', 
                                source_public_ip = 'example string', )
                            ], 
                        id = 123, 
                        name = 'example string', 
                        node_info = graphiant_sdk.models._v2_device__device_id__topology_post_200_response_nodes_inner_node_info._v2_device__deviceId__topology_post_200_response_nodes_inner_nodeInfo(
                            control_quality = 'ENUM_VALUE', 
                            cpu = 12.34, 
                            data_quality = 'ENUM_VALUE', 
                            device_id = 1234567891011, 
                            hostname = 'example string', 
                            location = 'example string', 
                            maintenance_mode = True, 
                            memory = 12.34, 
                            mgmt_ip = 'example string', 
                            model = 'example string', 
                            portal_quality = 'ENUM_VALUE', 
                            serial_number = 'example string', 
                            software_version = 'example string', 
                            staging_mode = True, 
                            temperature = 12.34, 
                            uptime = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                nanos = 123, 
                                seconds = 1234567891011, ), ), 
                        quality = 'ENUM_VALUE', 
                        type = 'ENUM_VALUE', )
                    ],
                snapshots = [
                    graphiant_sdk.models._v2_device__device_id__topology_post_200_response_snapshots_inner._v2_device__deviceId__topology_post_200_response_snapshots_inner(
                        quality = 'ENUM_VALUE', 
                        snapshot_time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), )
                    ]
            )
        else:
            return V2DeviceDeviceIdTopologyPost200Response(
        )
        """

    def testV2DeviceDeviceIdTopologyPost200Response(self):
        """Test V2DeviceDeviceIdTopologyPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
