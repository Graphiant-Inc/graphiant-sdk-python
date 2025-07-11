# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_policy_applications_get200_response import V1PolicyApplicationsGet200Response

class TestV1PolicyApplicationsGet200Response(unittest.TestCase):
    """V1PolicyApplicationsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PolicyApplicationsGet200Response:
        """Test V1PolicyApplicationsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PolicyApplicationsGet200Response`
        """
        model = V1PolicyApplicationsGet200Response()
        if include_optional:
            return V1PolicyApplicationsGet200Response(
                applications = [
                    graphiant_sdk.models._v1_policy_applications_get_200_response_applications_inner._v1_policy_applications_get_200_response_applications_inner(
                        app_id = 1234567891011, 
                        description = 'example string', 
                        kind = 'ENUM_VALUE', 
                        name = 'example string', )
                    ],
                page_info = graphiant_sdk.models._v1_nat_entries__device_id__get_200_response_page_info._v1_nat_entries__deviceId__get_200_response_pageInfo(
                    current_page = 1, 
                    end_cursor = 'xxxxxxy', 
                    has_next_page = False, 
                    has_prev_page = True, 
                    start_cursor = 'xxxxxx', 
                    total_pages = 4, 
                    total_records = 400, )
            )
        else:
            return V1PolicyApplicationsGet200Response(
        )
        """

    def testV1PolicyApplicationsGet200Response(self):
        """Test V1PolicyApplicationsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
