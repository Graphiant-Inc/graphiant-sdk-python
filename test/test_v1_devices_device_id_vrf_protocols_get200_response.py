# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_vrf_protocols_get200_response import V1DevicesDeviceIdVrfProtocolsGet200Response

class TestV1DevicesDeviceIdVrfProtocolsGet200Response(unittest.TestCase):
    """V1DevicesDeviceIdVrfProtocolsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdVrfProtocolsGet200Response:
        """Test V1DevicesDeviceIdVrfProtocolsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdVrfProtocolsGet200Response`
        """
        model = V1DevicesDeviceIdVrfProtocolsGet200Response()
        if include_optional:
            return V1DevicesDeviceIdVrfProtocolsGet200Response(
                bgp = True,
                connected = True,
                graphiant = True,
                ospfv2 = True,
                ospfv3 = True,
                static = True
            )
        else:
            return V1DevicesDeviceIdVrfProtocolsGet200Response(
        )
        """

    def testV1DevicesDeviceIdVrfProtocolsGet200Response(self):
        """Test V1DevicesDeviceIdVrfProtocolsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
