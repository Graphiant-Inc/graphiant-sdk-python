# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_devices_running_version_post200_response_versions_inner import V1DevicesRunningVersionPost200ResponseVersionsInner

class TestV1DevicesRunningVersionPost200ResponseVersionsInner(unittest.TestCase):
    """V1DevicesRunningVersionPost200ResponseVersionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DevicesRunningVersionPost200ResponseVersionsInner:
        """Test V1DevicesRunningVersionPost200ResponseVersionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DevicesRunningVersionPost200ResponseVersionsInner`
        """
        model = V1DevicesRunningVersionPost200ResponseVersionsInner()
        if include_optional:
            return V1DevicesRunningVersionPost200ResponseVersionsInner(
                device_id = 1234567891011,
                version = graphiant_sdk.models._v1_edges_hardware_assigned_get_200_response_edges_summary_inner_upgrade_summary_running_version._v1_edges_hardware_assigned_get_200_response_edgesSummary_inner_upgradeSummary_runningVersion(
                    name = 'example string', 
                    release = 'ENUM_VALUE', )
            )
        else:
            return V1DevicesRunningVersionPost200ResponseVersionsInner(
        )
        """

    def testV1DevicesRunningVersionPost200ResponseVersionsInner(self):
        """Test V1DevicesRunningVersionPost200ResponseVersionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
