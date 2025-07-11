# coding: utf-8

"""
    Graphiant APIs

    **To use the APIs:**  1) Login using `/api/v1/auth/login`   2) Copy the value of \"token\" in the response   3) Click the \"Authorize\" button   4) In the \"Value\" text field enter: `Bearer <your token>`   5) Click \"Authorize\"   6) All requests are now authorized.  **Token valid for 2 hours. If expired:**   - Login again, click \"Authorize\", paste new token.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from graphiant_sdk.models.v1_enterprise_contract_put_request import V1EnterpriseContractPutRequest

class TestV1EnterpriseContractPutRequest(unittest.TestCase):
    """V1EnterpriseContractPutRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EnterpriseContractPutRequest:
        """Test V1EnterpriseContractPutRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EnterpriseContractPutRequest`
        """
        model = V1EnterpriseContractPutRequest()
        if include_optional:
            return V1EnterpriseContractPutRequest(
                contracted_credits = 12.34,
                expiration_date = graphiant_sdk.models._v1_enterprise_allocation_get_200_response_consumption_summary_contractual_summary_expiration_date._v1_enterprise_allocation_get_200_response_consumptionSummary_contractualSummary_expirationDate(
                    month = 123, 
                    year = 123, )
            )
        else:
            return V1EnterpriseContractPutRequest(
        )
        """

    def testV1EnterpriseContractPutRequest(self):
        """Test V1EnterpriseContractPutRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
