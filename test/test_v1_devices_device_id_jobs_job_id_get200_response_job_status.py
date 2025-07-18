# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_device_id_jobs_job_id_get200_response_job_status import V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus

class TestV1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus(unittest.TestCase):
    """V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus:
        """Test V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus`
        """
        model = V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus()
        if include_optional:
            return V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus(
                completed_at = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                    nanos = 123, 
                    seconds = 1234567891011, ),
                created_at = graphiant_sdk.models._v1_alarm_history_get_200_response_history_inner_time._v1_alarm_history_get_200_response_history_inner_time(
                    nanos = 123, 
                    seconds = 1234567891011, ),
                error = 'example string',
                error_count = 123,
                job_id = 1234567891011,
                job_state = 'ENUM_VALUE'
            )
        else:
            return V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus(
        )
        """

    def testV1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus(self):
        """Test V1DevicesDeviceIdJobsJobIdGet200ResponseJobStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
