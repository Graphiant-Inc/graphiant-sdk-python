# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_vacm_groups_value_group_members_value_member import V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember

class TestV1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember(unittest.TestCase):
    """V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember:
        """Test V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember`
        """
        model = V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember()
        if include_optional:
            return V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember(
                community = 'example string',
                security_model = 'ENUM_VALUE',
                security_name = 'example string',
                type = 'ENUM_VALUE'
            )
        else:
            return V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember(
        )
        """

    def testV1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember(self):
        """Test V1GlobalConfigPatchRequestSnmpsValueConfigVacmGroupsValueGroupMembersValueMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
