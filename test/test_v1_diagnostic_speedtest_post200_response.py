# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_diagnostic_speedtest_post200_response import V1DiagnosticSpeedtestPost200Response

class TestV1DiagnosticSpeedtestPost200Response(unittest.TestCase):
    """V1DiagnosticSpeedtestPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DiagnosticSpeedtestPost200Response:
        """Test V1DiagnosticSpeedtestPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DiagnosticSpeedtestPost200Response`
        """
        model = V1DiagnosticSpeedtestPost200Response()
        if include_optional:
            return V1DiagnosticSpeedtestPost200Response(
                result = graphiant_sdk.models._v1_diagnostic_speedtest_post_200_response_result._v1_diagnostic_speedtest_post_200_response_result(
                    avg_ping_time = 3, 
                    date_time = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                        nanos = 123, 
                        seconds = 1234567891011, ), 
                    download_speed = 30.1, 
                    isp = 'Google Fiber', 
                    max_ping_time = 5, 
                    min_ping_time = 10, 
                    result = 'Failed', 
                    server_details = graphiant_sdk.models._v1_diagnostic_speedtest_servers_get_200_response_server_inner._v1_diagnostic_speedtest_servers_get_200_response_server_inner(
                        country = 'United Kingdom', 
                        host = 'speedtest.fastmetrics.com', 
                        id = '29113', 
                        ip_address = '1213:1::6451', 
                        location = 'Sheffield', 
                        name = 'Google Fiber', ), 
                    upload_speed = 21, ),
                token = 'example string'
            )
        else:
            return V1DiagnosticSpeedtestPost200Response(
        )
        """

    def testV1DiagnosticSpeedtestPost200Response(self):
        """Test V1DiagnosticSpeedtestPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
