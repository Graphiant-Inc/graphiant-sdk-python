# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_nat_entries_device_id_get200_response import V1NatEntriesDeviceIdGet200Response

class TestV1NatEntriesDeviceIdGet200Response(unittest.TestCase):
    """V1NatEntriesDeviceIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NatEntriesDeviceIdGet200Response:
        """Test V1NatEntriesDeviceIdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NatEntriesDeviceIdGet200Response`
        """
        model = V1NatEntriesDeviceIdGet200Response()
        if include_optional:
            return V1NatEntriesDeviceIdGet200Response(
                nat_entries = [
                    graphiant_sdk.models._v1_nat_entries__device_id__get_200_response_nat_entries_inner._v1_nat_entries__deviceId__get_200_response_natEntries_inner(
                        destination_ip_address = 'example string', 
                        destination_port = 123, 
                        inside_global_ip_address = 'example string', 
                        inside_global_port = 123, 
                        inside_local_ip_address = 'example string', 
                        inside_local_port = 123, 
                        nat_type = 'ENUM_VALUE', 
                        outside_global_ip_address = 'example string', 
                        outside_global_port = 123, 
                        pre_destination_ip_address = 'example string', 
                        pre_destination_port = 123, 
                        vrf_id = 12345678910, )
                    ],
                page_info = graphiant_sdk.models._v1_nat_entries__device_id__get_200_response_page_info._v1_nat_entries__deviceId__get_200_response_pageInfo(
                    current_page = 1, 
                    end_cursor = 'xxxxxxy', 
                    has_next_page = False, 
                    has_prev_page = True, 
                    start_cursor = 'xxxxxx', 
                    total_pages = 4, 
                    total_records = 400, ),
                ts = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                    nanos = 123, 
                    seconds = 1234567891011, )
            )
        else:
            return V1NatEntriesDeviceIdGet200Response(
        )
        """

    def testV1NatEntriesDeviceIdGet200Response(self):
        """Test V1NatEntriesDeviceIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
