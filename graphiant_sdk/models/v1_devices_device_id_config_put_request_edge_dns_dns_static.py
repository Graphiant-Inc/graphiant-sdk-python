# coding: utf-8

"""
    Graphiant APIs

    Graphiant API documentation.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_addresses_value import V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic(BaseModel):
    """
    V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic
    """ # noqa: E501
    primary_ipv4_v2: Optional[V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue] = Field(default=None, alias="primaryIpv4V2")
    primary_ipv6_v2: Optional[V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue] = Field(default=None, alias="primaryIpv6V2")
    secondary_ipv4_v2: Optional[V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue] = Field(default=None, alias="secondaryIpv4V2")
    secondary_ipv6_v2: Optional[V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue] = Field(default=None, alias="secondaryIpv6V2")
    __properties: ClassVar[List[str]] = ["primaryIpv4V2", "primaryIpv6V2", "secondaryIpv4V2", "secondaryIpv6V2"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of primary_ipv4_v2
        if self.primary_ipv4_v2:
            _dict['primaryIpv4V2'] = self.primary_ipv4_v2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_ipv6_v2
        if self.primary_ipv6_v2:
            _dict['primaryIpv6V2'] = self.primary_ipv6_v2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_ipv4_v2
        if self.secondary_ipv4_v2:
            _dict['secondaryIpv4V2'] = self.secondary_ipv4_v2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_ipv6_v2
        if self.secondary_ipv6_v2:
            _dict['secondaryIpv6V2'] = self.secondary_ipv6_v2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "primaryIpv4V2": V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.from_dict(obj["primaryIpv4V2"]) if obj.get("primaryIpv4V2") is not None else None,
            "primaryIpv6V2": V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.from_dict(obj["primaryIpv6V2"]) if obj.get("primaryIpv6V2") is not None else None,
            "secondaryIpv4V2": V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.from_dict(obj["secondaryIpv4V2"]) if obj.get("secondaryIpv4V2") is not None else None,
            "secondaryIpv6V2": V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.from_dict(obj["secondaryIpv6V2"]) if obj.get("secondaryIpv6V2") is not None else None
        })
        return _obj


