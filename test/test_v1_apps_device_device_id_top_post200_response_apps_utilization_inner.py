# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_apps_device_device_id_top_post200_response_apps_utilization_inner import V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner

class TestV1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner(unittest.TestCase):
    """V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner:
        """Test V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner`
        """
        model = V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner()
        if include_optional:
            return V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner(
                app_id = 123,
                app_name = 'example string',
                usage = 1234567891011
            )
        else:
            return V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner(
        )
        """

    def testV1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner(self):
        """Test V1AppsDeviceDeviceIdTopPost200ResponseAppsUtilizationInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
