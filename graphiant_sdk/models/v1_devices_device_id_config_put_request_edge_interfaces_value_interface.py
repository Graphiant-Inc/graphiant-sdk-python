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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_gw_gw import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw
from graphiant_sdk.models.v1_devices_device_id_config_put_request_core_interfaces_value_interface_ipsec import V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_interfaces_value_interface_subinterfaces_value import V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValue
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v4_tcp_mss import V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV4TcpMss
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_interfaces_value_interface_subinterfaces_value_interface_v6_tcp_mss import V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV6TcpMss
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface(BaseModel):
    """
    V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface
    """ # noqa: E501
    admin_status: Optional[StrictBool] = Field(default=None, alias="adminStatus")
    alias: Optional[StrictStr] = None
    circuit: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    ipsec: Optional[V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec] = None
    ipv4: Optional[V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw] = None
    ipv6: Optional[V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw] = None
    lan: Optional[StrictStr] = None
    lldp_enabled: Optional[StrictBool] = Field(default=None, alias="lldpEnabled")
    loopback: Optional[StrictBool] = None
    max_transmission_unit: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="maxTransmissionUnit")
    security_zone: Optional[StrictStr] = Field(default=None, alias="securityZone")
    subinterfaces: Optional[Dict[str, V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValue]] = None
    tcp_mss: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="tcpMss")
    tcp_mss_v4: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="tcpMssV4")
    tcp_mss_v6: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="tcpMssV6")
    v4_tcp_mss: Optional[V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV4TcpMss] = Field(default=None, alias="v4TcpMss")
    v6_tcp_mss: Optional[V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV6TcpMss] = Field(default=None, alias="v6TcpMss")
    __properties: ClassVar[List[str]] = ["adminStatus", "alias", "circuit", "description", "ipsec", "ipv4", "ipv6", "lan", "lldpEnabled", "loopback", "maxTransmissionUnit", "securityZone", "subinterfaces", "tcpMss", "tcpMssV4", "tcpMssV6", "v4TcpMss", "v6TcpMss"]

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
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ipsec
        if self.ipsec:
            _dict['ipsec'] = self.ipsec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ipv4
        if self.ipv4:
            _dict['ipv4'] = self.ipv4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ipv6
        if self.ipv6:
            _dict['ipv6'] = self.ipv6.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in subinterfaces (dict)
        _field_dict = {}
        if self.subinterfaces:
            for _key_subinterfaces in self.subinterfaces:
                if self.subinterfaces[_key_subinterfaces]:
                    _field_dict[_key_subinterfaces] = self.subinterfaces[_key_subinterfaces].to_dict()
            _dict['subinterfaces'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of v4_tcp_mss
        if self.v4_tcp_mss:
            _dict['v4TcpMss'] = self.v4_tcp_mss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of v6_tcp_mss
        if self.v6_tcp_mss:
            _dict['v6TcpMss'] = self.v6_tcp_mss.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adminStatus": obj.get("adminStatus"),
            "alias": obj.get("alias"),
            "circuit": obj.get("circuit"),
            "description": obj.get("description"),
            "ipsec": V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceIpsec.from_dict(obj["ipsec"]) if obj.get("ipsec") is not None else None,
            "ipv4": V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.from_dict(obj["ipv4"]) if obj.get("ipv4") is not None else None,
            "ipv6": V1DevicesDeviceIdConfigPutRequestCoreInterfacesValueInterfaceGwGw.from_dict(obj["ipv6"]) if obj.get("ipv6") is not None else None,
            "lan": obj.get("lan"),
            "lldpEnabled": obj.get("lldpEnabled"),
            "loopback": obj.get("loopback"),
            "maxTransmissionUnit": obj.get("maxTransmissionUnit"),
            "securityZone": obj.get("securityZone"),
            "subinterfaces": dict(
                (_k, V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValue.from_dict(_v))
                for _k, _v in obj["subinterfaces"].items()
            )
            if obj.get("subinterfaces") is not None
            else None,
            "tcpMss": obj.get("tcpMss"),
            "tcpMssV4": obj.get("tcpMssV4"),
            "tcpMssV6": obj.get("tcpMssV6"),
            "v4TcpMss": V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV4TcpMss.from_dict(obj["v4TcpMss"]) if obj.get("v4TcpMss") is not None else None,
            "v6TcpMss": V1DevicesDeviceIdConfigPutRequestEdgeInterfacesValueInterfaceSubinterfacesValueInterfaceV6TcpMss.from_dict(obj["v6TcpMss"]) if obj.get("v6TcpMss") is not None else None
        })
        return _obj


