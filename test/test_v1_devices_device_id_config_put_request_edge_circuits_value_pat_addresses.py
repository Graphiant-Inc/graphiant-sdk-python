# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_circuits_value_pat_addresses import V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses

class TestV1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses(unittest.TestCase):
    """V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses:
        """Test V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses`
        """
        model = V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses()
        if include_optional:
            return V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses(
                addresses = [
                    'example string'
                    ]
            )
        else:
            return V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses(
        )
        """

    def testV1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses(self):
        """Test V1DevicesDeviceIdConfigPutRequestEdgeCircuitsValuePatAddresses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
