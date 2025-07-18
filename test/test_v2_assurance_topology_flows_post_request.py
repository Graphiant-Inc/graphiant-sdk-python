# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_topology_flows_post_request import V2AssuranceTopologyFlowsPostRequest

class TestV2AssuranceTopologyFlowsPostRequest(unittest.TestCase):
    """V2AssuranceTopologyFlowsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceTopologyFlowsPostRequest:
        """Test V2AssuranceTopologyFlowsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceTopologyFlowsPostRequest`
        """
        model = V2AssuranceTopologyFlowsPostRequest()
        if include_optional:
            return V2AssuranceTopologyFlowsPostRequest(
                app_name = 'example string',
                time_window = graphiant_sdk.models._v2_notificationlist_post_request_time_window._v2_notificationlist_post_request_timeWindow(
                    bucket_size_sec = 123, 
                    old_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                        nanos = 123, 
                        seconds = 1234567891011, ), 
                    recent_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                        nanos = 123, 
                        seconds = 1234567891011, ), ),
                topology_id = 123,
                topology_type = 'ENUM_VALUE'
            )
        else:
            return V2AssuranceTopologyFlowsPostRequest(
        )
        """

    def testV2AssuranceTopologyFlowsPostRequest(self):
        """Test V2AssuranceTopologyFlowsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
