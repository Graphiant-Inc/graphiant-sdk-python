# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_core_vrf_bgp_redistribution_value import V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue

class TestV1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue(unittest.TestCase):
    """V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue:
        """Test V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue`
        """
        model = V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue()
        if include_optional:
            return V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue(
                protocol = graphiant_sdk.models._v1_global_config_patch_request_snmps_value_config_notify_filter_profiles_value_notify_filter_profile_include_exclude_list_value._v1_global_config_patch_request_snmps_value_config_notifyFilterProfiles_value_notifyFilterProfile_includeExcludeList_value(
                    enabled = True, )
            )
        else:
            return V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue(
        )
        """

    def testV1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue(self):
        """Test V1DevicesDeviceIdConfigPutRequestCoreCoreVrfBgpRedistributionValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
