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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_wan_gw_gw_dhcp import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwDhcp
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_subinterfaces_value_interface_wan_gw_gw_vrrp import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwVrrp
from graphiant_sdk.models.v1_global_config_patch_request_snmps_value_config_engine_endpoints_value_engine_endpoint_addresses_value import V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGw(BaseModel):
    """
    V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGw
    """ # noqa: E501
    address: Optional[V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue] = None
    dhcp: Optional[V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwDhcp] = None
    vrrp: Optional[V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwVrrp] = None
    __properties: ClassVar[List[str]] = ["address", "dhcp", "vrrp"]

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
        """Create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGw from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dhcp
        if self.dhcp:
            _dict['dhcp'] = self.dhcp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vrrp
        if self.vrrp:
            _dict['vrrp'] = self.vrrp.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGw from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": V1GlobalConfigPatchRequestSnmpsValueConfigEngineEndpointsValueEngineEndpointAddressesValue.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "dhcp": V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwDhcp.from_dict(obj["dhcp"]) if obj.get("dhcp") is not None else None,
            "vrrp": V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceSubinterfacesValueInterfaceWanGwGwVrrp.from_dict(obj["vrrp"]) if obj.get("vrrp") is not None else None
        })
        return _obj


