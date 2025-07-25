# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v2_assurance_create_user_report_post_request import V2AssuranceCreateUserReportPostRequest

class TestV2AssuranceCreateUserReportPostRequest(unittest.TestCase):
    """V2AssuranceCreateUserReportPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssuranceCreateUserReportPostRequest:
        """Test V2AssuranceCreateUserReportPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssuranceCreateUserReportPostRequest`
        """
        model = V2AssuranceCreateUserReportPostRequest()
        if include_optional:
            return V2AssuranceCreateUserReportPostRequest(
                created_on = 1234567891011,
                email_list = [
                    'example string'
                    ],
                pdf_content = '[B@7de0c6ae',
                raw_content = [
                    '[B@a486d78'
                    ],
                report_name = 'example string',
                report_type = 'ENUM_VALUE',
                time_period = 'ENUM_VALUE'
            )
        else:
            return V2AssuranceCreateUserReportPostRequest(
        )
        """

    def testV2AssuranceCreateUserReportPostRequest(self):
        """Test V2AssuranceCreateUserReportPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
