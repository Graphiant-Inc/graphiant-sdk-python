# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_activity_logs_post200_response import V1ActivityLogsPost200Response

class TestV1ActivityLogsPost200Response(unittest.TestCase):
    """V1ActivityLogsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ActivityLogsPost200Response:
        """Test V1ActivityLogsPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ActivityLogsPost200Response`
        """
        model = V1ActivityLogsPost200Response()
        if include_optional:
            return V1ActivityLogsPost200Response(
                cursor_ref = 'example string',
                details = [
                    graphiant_sdk.models._v1_activity_logs_post_200_response_details_inner._v1_activity_logs_post_200_response_details_inner(
                        action = 'example string', 
                        attributes = [
                            graphiant_sdk.models._v1_activity_logs_post_request_selector_job_entity._v1_activity_logs_post_request_selector_jobEntity(
                                id = 1234567891011, 
                                name = 'example string', 
                                type = 'ENUM_VALUE', )
                            ], 
                        category = 'ENUM_VALUE', 
                        disable_auto_timeout = True, 
                        end_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), 
                        enterprise_id = 1234567891011, 
                        id = 'example string', 
                        initiator_type = 'ENUM_VALUE', 
                        job_entities = [
                            graphiant_sdk.models._v1_activity_logs_post_request_selector_job_entity._v1_activity_logs_post_request_selector_jobEntity(
                                id = 1234567891011, 
                                name = 'example string', 
                                type = 'ENUM_VALUE', )
                            ], 
                        job_type = 'ENUM_VALUE', 
                        original_enterprise_id = 1234567891011, 
                        start_ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                            nanos = 123, 
                            seconds = 1234567891011, ), 
                        status = 'ENUM_VALUE', 
                        targets = [
                            graphiant_sdk.models._v1_activity_logs_post_200_response_details_inner_targets_inner._v1_activity_logs_post_200_response_details_inner_targets_inner(
                                detailed_failure_reason = 'example string', 
                                events = [
                                    graphiant_sdk.models._v1_activity_logs_post_200_response_details_inner_targets_inner_events_inner._v1_activity_logs_post_200_response_details_inner_targets_inner_events_inner(
                                        state = 'example string', 
                                        state_id = 123, 
                                        trace_session_id = 'example string', 
                                        ts = , )
                                    ], 
                                failure_reason = 'example string', 
                                ids = [
                                    
                                    ], 
                                status = 'ENUM_VALUE', )
                            ], 
                        trace_session_id = 'example string', 
                        usage = 'ENUM_VALUE', 
                        user = 'example string', 
                        user_id = 'example string', )
                    ],
                filter_entities = {
                    'key' : graphiant_sdk.models._v1_activity_logs_post_200_response_filter_entities_value._v1_activity_logs_post_200_response_filterEntities_value(
                        items = [
                            graphiant_sdk.models._v1_activity_logs_post_request_selector_job_entity._v1_activity_logs_post_request_selector_jobEntity(
                                id = 1234567891011, 
                                name = 'example string', 
                                type = 'ENUM_VALUE', )
                            ], )
                    },
                filter_job_types = [
                    'ENUM_VALUE'
                    ],
                total_logs = 12345678910
            )
        else:
            return V1ActivityLogsPost200Response(
        )
        """

    def testV1ActivityLogsPost200Response(self):
        """Test V1ActivityLogsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
