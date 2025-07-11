# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner_bgp_connection import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection

class TestV1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection(unittest.TestCase):
    """V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection:
        """Test V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection`
        """
        model = V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection()
        if include_optional:
            return V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection(
                local_address = 'example string',
                oper_status = True,
                remote_address = 'example string',
                state = 'ENUM_VALUE',
                time_since_last_oper_change = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                    nanos = 123, 
                    seconds = 1234567891011, ),
                up = True
            )
        else:
            return V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection(
        )
        """

    def testV1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection(self):
        """Test V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerBgpConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
