# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_flow_summary_post_request import V2AssuranceFlowSummaryPostRequest

class TestV2AssuranceFlowSummaryPostRequest(unittest.TestCase):
    """V2AssuranceFlowSummaryPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceFlowSummaryPostRequest:
        """Test V2AssuranceFlowSummaryPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceFlowSummaryPostRequest`
        """
        model = V2AssuranceFlowSummaryPostRequest()
        if include_optional:
            return V2AssuranceFlowSummaryPostRequest(
                client_ip = 'example string',
                server_ip = 'example string',
                server_port = 123,
                time_window = graphiant_sdk.models._v2_notificationlist_post_request_time_window._v2_notificationlist_post_request_timeWindow(
                    bucket_size_sec = 123, 
                    old_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                        nanos = 123, 
                        seconds = 1234567891011, ), 
                    recent_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                        nanos = 123, 
                        seconds = 1234567891011, ), )
            )
        else:
            return V2AssuranceFlowSummaryPostRequest(
        )
        """

    def testV2AssuranceFlowSummaryPostRequest(self):
        """Test V2AssuranceFlowSummaryPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
