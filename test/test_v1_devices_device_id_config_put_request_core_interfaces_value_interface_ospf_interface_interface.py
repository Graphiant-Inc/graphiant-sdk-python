# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_ospf_interface_interface import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface

class TestV1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface(unittest.TestCase):
    """V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface:
        """Test V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface`
        """
        model = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface()
        if include_optional:
            return V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface(
                bfd = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_core_vrf_bgp_neighbors_value_neighbor_bfd._v1_devices__deviceId__config_put_request_core_coreVrf_bgpNeighbors_value_neighbor_bfd(),
                cost = 123,
                dead_interval_value = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_dead_interval_value._v1_devices__deviceId__config_put_request_core_coreVrf_ospfv2_process_areas_value_area_interfaces_value_interface_deadIntervalValue(
                    dead_interval = 123, ),
                dr_priority = 123,
                hello_interval_value = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_hello_interval_value._v1_devices__deviceId__config_put_request_core_coreVrf_ospfv2_process_areas_value_area_interfaces_value_interface_helloIntervalValue(
                    hello_interval = 123, ),
                interface_name = 'example string',
                mtu = 123,
                mtu_ignore = True,
                prefix_sid = 123,
                retransmit_interval_value = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_core_vrf_ospfv2_process_areas_value_area_interfaces_value_interface_retransmit_interval_value._v1_devices__deviceId__config_put_request_core_coreVrf_ospfv2_process_areas_value_area_interfaces_value_interface_retransmitIntervalValue(
                    retransmit_interval = 123, ),
                type = 'ENUM_VALUE'
            )
        else:
            return V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface(
        )
        """

    def testV1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface(self):
        """Test V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceOspfInterfaceInterface"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
