# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_core_neighbor_cost import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost

class TestV1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost(unittest.TestCase):
    """V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost:
        """Test V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost`
        """
        model = V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost()
        if include_optional:
            return V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost(
                dynamic = graphiant_sdk.models._v1_devices__device_id__config_put_request_core_interfaces_value_interface_core_neighbor_cost_dynamic._v1_devices__deviceId__config_put_request_core_interfaces_value_interface_coreNeighbor_Cost_dynamic(
                    bandwidth = 123, 
                    latency = 123, ),
                static = 123
            )
        else:
            return V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost(
        )
        """

    def testV1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost(self):
        """Test V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceCoreNeighborCost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
