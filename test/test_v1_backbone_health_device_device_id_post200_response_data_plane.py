# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_data_plane import V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane

class TestV1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane(unittest.TestCase):
    """V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane:
        """Test V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane`
        """
        model = V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane()
        if include_optional:
            return V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane(
                down_transitions = [
                    graphiant_sdk.models._v1_backbone_health_device__device_id__post_200_response_control_plane_control_transitions_transitions_inner._v1_backbone_health_device__deviceId__post_200_response_controlPlane_controlTransitions_transitions_inner(
                        name = 'example string', 
                        transitions = [
                            graphiant_sdk.models._v1_backbone_health_device__device_id__post_200_response_control_plane_control_transitions_transitions_inner_transitions_inner._v1_backbone_health_device__deviceId__post_200_response_controlPlane_controlTransitions_transitions_inner_transitions_inner(
                                interface_name = 'example string', 
                                peer_name = 'example string', 
                                time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                value = 123.45, )
                            ], )
                    ],
                session_slas = [
                    graphiant_sdk.models._v1_backbone_health_device__device_id__post_200_response_data_plane_session_slas_inner._v1_backbone_health_device__deviceId__post_200_response_dataPlane_sessionSlas_inner(
                        name = 'example string', 
                        values = [
                            graphiant_sdk.models._v1_backbone_health_device__device_id__post_200_response_data_plane_session_slas_inner_values_inner._v1_backbone_health_device__deviceId__post_200_response_dataPlane_sessionSlas_inner_values_inner(
                                delay_value = 123.45, 
                                jitter_value = 123.45, 
                                loss_value = 123.45, 
                                status = 'ENUM_VALUE', 
                                time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                                    nanos = 123, 
                                    seconds = 1234567891011, ), 
                                value = 123.45, )
                            ], )
                    ],
                status = 'ENUM_VALUE'
            )
        else:
            return V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane(
        )
        """

    def testV1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane(self):
        """Test V1BackboneHealthDeviceDeviceIdPost200ResponseDataPlane"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
