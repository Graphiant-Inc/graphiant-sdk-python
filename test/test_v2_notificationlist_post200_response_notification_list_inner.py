# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_notificationlist_post200_response_notification_list_inner import V2NotificationlistPost200ResponseNotificationListInner

class TestV2NotificationlistPost200ResponseNotificationListInner(unittest.TestCase):
    """V2NotificationlistPost200ResponseNotificationListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2NotificationlistPost200ResponseNotificationListInner:
        """Test V2NotificationlistPost200ResponseNotificationListInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2NotificationlistPost200ResponseNotificationListInner`
        """
        model = V2NotificationlistPost200ResponseNotificationListInner()
        if include_optional:
            return V2NotificationlistPost200ResponseNotificationListInner(
                alert_type = 'example string',
                mute_count = 1234567891011,
                name = 'example string',
                notification_body = graphiant_sdk.models._v2_notification_create_post_request_notification_body._v2_notification_create_post_request_notificationBody(
                    description = 'example string', 
                    duration = 'ENUM_VALUE', 
                    enabled = True, 
                    frequency = 12345678910, 
                    message_body = 'example string', 
                    notification_name = 'example string', 
                    opsgenie_list = [
                        'example string'
                        ], 
                    opsramp_list = [
                        'example string'
                        ], 
                    recipient_list = [
                        'example string'
                        ], 
                    teams_list = [
                        'example string'
                        ], ),
                notification_id = 'example string',
                rule_id = 'example string',
                times_triggered = 12345678910
            )
        else:
            return V2NotificationlistPost200ResponseNotificationListInner(
        )
        """

    def testV2NotificationlistPost200ResponseNotificationListInner(self):
        """Test V2NotificationlistPost200ResponseNotificationListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
