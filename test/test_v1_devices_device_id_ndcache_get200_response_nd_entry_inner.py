# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_ndcache_get200_response_nd_entry_inner import V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner

class TestV1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner(unittest.TestCase):
    """V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner:
        """Test V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner`
        """
        model = V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner()
        if include_optional:
            return V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner(
                interface_name = 'example string',
                ipv6_address = 'example string',
                mac_address = 'example string',
                name = 'example string'
            )
        else:
            return V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner(
        )
        """

    def testV1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner(self):
        """Test V1DevicesDeviceIdNdcacheGet200ResponseNdEntryInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
