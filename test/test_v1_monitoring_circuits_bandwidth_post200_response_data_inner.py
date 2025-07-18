# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_monitoring_circuits_bandwidth_post200_response_data_inner import V1MonitoringCircuitsBandwidthPost200ResponseDataInner

class TestV1MonitoringCircuitsBandwidthPost200ResponseDataInner(unittest.TestCase):
    """V1MonitoringCircuitsBandwidthPost200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1MonitoringCircuitsBandwidthPost200ResponseDataInner:
        """Test V1MonitoringCircuitsBandwidthPost200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1MonitoringCircuitsBandwidthPost200ResponseDataInner`
        """
        model = V1MonitoringCircuitsBandwidthPost200ResponseDataInner()
        if include_optional:
            return V1MonitoringCircuitsBandwidthPost200ResponseDataInner(
                carrier = 'example string',
                device_id = 12345678910,
                dl_bw_kbps_samples = [
                    graphiant_sdk.models._v2_monitoring_bfd_post_200_response_data_inner_samples_inner._v2_monitoring_bfd_post_200_response_data_inner_samples_inner(
                        status = 'ENUM_VALUE', 
                        ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), 
                        value = 123.45, )
                    ],
                selector = graphiant_sdk.models._v1_monitoring_circuits_bandwidth_post_request_selectors_inner._v1_monitoring_circuits_bandwidth_post_request_selectors_inner(
                    circuit_name = 'example string', 
                    device_id = 12345678910, ),
                ul_bw_kbps_samples = [
                    graphiant_sdk.models._v2_monitoring_bfd_post_200_response_data_inner_samples_inner._v2_monitoring_bfd_post_200_response_data_inner_samples_inner(
                        status = 'ENUM_VALUE', 
                        ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), 
                        value = 123.45, )
                    ]
            )
        else:
            return V1MonitoringCircuitsBandwidthPost200ResponseDataInner(
        )
        """

    def testV1MonitoringCircuitsBandwidthPost200ResponseDataInner(self):
        """Test V1MonitoringCircuitsBandwidthPost200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
