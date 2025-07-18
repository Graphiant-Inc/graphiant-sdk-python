# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_data_plane_session_slas_inner_values_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner

class TestV1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner(unittest.TestCase):
    """V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner:
        """Test V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner`
        """
        model = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner()
        if include_optional:
            return V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner(
                delay_value = 123.45,
                jitter_value = 123.45,
                loss_value = 123.45,
                status = 'ENUM_VALUE',
                time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                    nanos = 123, 
                    seconds = 1234567891011, ),
                value = 123.45
            )
        else:
            return V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner(
        )
        """

    def testV1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner(self):
        """Test V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlaneSessionSlasInnerValuesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
