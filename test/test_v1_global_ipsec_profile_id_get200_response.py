# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_global_ipsec_profile_id_get200_response import V1GlobalIpsecProfileIdGet200Response

class TestV1GlobalIpsecProfileIdGet200Response(unittest.TestCase):
    """V1GlobalIpsecProfileIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1GlobalIpsecProfileIdGet200Response:
        """Test V1GlobalIpsecProfileIdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1GlobalIpsecProfileIdGet200Response`
        """
        model = V1GlobalIpsecProfileIdGet200Response()
        if include_optional:
            return V1GlobalIpsecProfileIdGet200Response(
                ipsec_profile = graphiant_sdk.models._v1_global_config_patch_request_vpn_profiles_value_vpn_profile._v1_global_config_patch_request_vpnProfiles_value_vpnProfile(
                    anti_replay_window_size = 123, 
                    dpd_interval = 123, 
                    esn = True, 
                    id = 1234567891011, 
                    ike_dh_group = 'ENUM_VALUE', 
                    ike_encryption_alg = 'ENUM_VALUE', 
                    ike_integrity = 'ENUM_VALUE', 
                    ipsec_encryption_alg = 'ENUM_VALUE', 
                    ipsec_integrity = 'ENUM_VALUE', 
                    name = 'example string', 
                    perfect_forward_secrecy = 'ENUM_VALUE', 
                    reauth_interval = 123, 
                    rekey_interval = 123, )
            )
        else:
            return V1GlobalIpsecProfileIdGet200Response(
        )
        """

    def testV1GlobalIpsecProfileIdGet200Response(self):
        """Test V1GlobalIpsecProfileIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
