# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_healthcheck_devices_get200_response import V1HealthcheckDevicesGet200Response

class TestV1HealthcheckDevicesGet200Response(unittest.TestCase):
    """V1HealthcheckDevicesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1HealthcheckDevicesGet200Response:
        """Test V1HealthcheckDevicesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1HealthcheckDevicesGet200Response`
        """
        model = V1HealthcheckDevicesGet200Response()
        if include_optional:
            return V1HealthcheckDevicesGet200Response(
                details = [
                    graphiant_sdk.models._v1_healthcheck_devices_get_200_response_details_inner._v1_healthcheck_devices_get_200_response_details_inner(
                        bgp_core_state = [
                            True
                            ], 
                        bgp_odp_state = [
                            True
                            ], 
                        core_tunnel_state = [
                            True
                            ], 
                        device_id = 1234567891011, 
                        enterprise_id = 1234567891011, 
                        gnmi_state = True, 
                        ipsec_core_status = 'example string', 
                        ipsec_odp_status = 'example string', 
                        odp_status = graphiant_sdk.models._v1_healthcheck_devices_get_200_response_details_inner_odp_status._v1_healthcheck_devices_get_200_response_details_inner_odpStatus(
                            ip_address = 'example string', 
                            state = True, ), 
                        odp_tunnel_state = [
                            True
                            ], 
                        onboarding_status = graphiant_sdk.models._v1_healthcheck_devices_get_200_response_details_inner_onboarding_status._v1_healthcheck_devices_get_200_response_details_inner_onboardingStatus(
                            state = 'example string', 
                            status = 'example string', ), 
                        t2_status = graphiant_sdk.models._v1_healthcheck_devices_get_200_response_details_inner_odp_status._v1_healthcheck_devices_get_200_response_details_inner_odpStatus(
                            ip_address = 'example string', 
                            state = True, ), 
                        topo_gw_state = 'example string', 
                        tt_tunnel_state = [
                            True
                            ], )
                    ]
            )
        else:
            return V1HealthcheckDevicesGet200Response(
        )
        """

    def testV1HealthcheckDevicesGet200Response(self):
        """Test V1HealthcheckDevicesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
