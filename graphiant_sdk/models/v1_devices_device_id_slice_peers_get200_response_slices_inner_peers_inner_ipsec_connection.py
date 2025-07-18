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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_alarm_history_get200_response_history_inner_time import V1AlarmHistoryGet200ResponseHistoryInnerTime
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_interfaces_inner import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection(BaseModel):
    """
    V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection
    """ # noqa: E501
    anti_replay_w_size: Optional[StrictInt] = Field(default=None, alias="antiReplayWSize")
    established_time: Optional[V1AlarmHistoryGet200ResponseHistoryInnerTime] = Field(default=None, alias="establishedTime")
    local_circuit: Optional[StrictStr] = Field(default=None, alias="localCircuit")
    local_interface: Optional[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner] = Field(default=None, alias="localInterface")
    local_port: Optional[StrictInt] = Field(default=None, alias="localPort")
    local_spi: Optional[StrictInt] = Field(default=None, alias="localSpi")
    negotiated_algorithms: Optional[StrictStr] = Field(default=None, alias="negotiatedAlgorithms")
    oper_state: Optional[StrictBool] = Field(default=None, alias="operState")
    peer_address: Optional[StrictStr] = Field(default=None, alias="peerAddress")
    protocol: Optional[StrictStr] = None
    rekey_time: Optional[V1AlarmHistoryGet200ResponseHistoryInnerTime] = Field(default=None, alias="rekeyTime")
    remote_port: Optional[StrictInt] = Field(default=None, alias="remotePort")
    remote_spi: Optional[StrictInt] = Field(default=None, alias="remoteSpi")
    session_id: Optional[StrictInt] = Field(default=None, alias="sessionId")
    source_address: Optional[StrictStr] = Field(default=None, alias="sourceAddress")
    tunnel_interface: Optional[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner] = Field(default=None, alias="tunnelInterface")
    __properties: ClassVar[List[str]] = ["antiReplayWSize", "establishedTime", "localCircuit", "localInterface", "localPort", "localSpi", "negotiatedAlgorithms", "operState", "peerAddress", "protocol", "rekeyTime", "remotePort", "remoteSpi", "sessionId", "sourceAddress", "tunnelInterface"]

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
        """Create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of established_time
        if self.established_time:
            _dict['establishedTime'] = self.established_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_interface
        if self.local_interface:
            _dict['localInterface'] = self.local_interface.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rekey_time
        if self.rekey_time:
            _dict['rekeyTime'] = self.rekey_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tunnel_interface
        if self.tunnel_interface:
            _dict['tunnelInterface'] = self.tunnel_interface.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInnerIpsecConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "antiReplayWSize": obj.get("antiReplayWSize"),
            "establishedTime": V1AlarmHistoryGet200ResponseHistoryInnerTime.from_dict(obj["establishedTime"]) if obj.get("establishedTime") is not None else None,
            "localCircuit": obj.get("localCircuit"),
            "localInterface": V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.from_dict(obj["localInterface"]) if obj.get("localInterface") is not None else None,
            "localPort": obj.get("localPort"),
            "localSpi": obj.get("localSpi"),
            "negotiatedAlgorithms": obj.get("negotiatedAlgorithms"),
            "operState": obj.get("operState"),
            "peerAddress": obj.get("peerAddress"),
            "protocol": obj.get("protocol"),
            "rekeyTime": V1AlarmHistoryGet200ResponseHistoryInnerTime.from_dict(obj["rekeyTime"]) if obj.get("rekeyTime") is not None else None,
            "remotePort": obj.get("remotePort"),
            "remoteSpi": obj.get("remoteSpi"),
            "sessionId": obj.get("sessionId"),
            "sourceAddress": obj.get("sourceAddress"),
            "tunnelInterface": V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerInterfacesInner.from_dict(obj["tunnelInterface"]) if obj.get("tunnelInterface") is not None else None
        })
        return _obj


