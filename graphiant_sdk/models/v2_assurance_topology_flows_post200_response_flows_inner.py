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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_alarm_history_get200_response_history_inner_time import V1AlarmHistoryGet200ResponseHistoryInnerTime
from graphiant_sdk.models.v2_assurance_flow_summary_post200_response_client_endpoint_site import V2AssuranceFlowSummaryPost200ResponseClientEndpointSite
from typing import Optional, Set
from typing_extensions import Self

class V2AssuranceTopologyFlowsPost200ResponseFlowsInner(BaseModel):
    """
    V2AssuranceTopologyFlowsPost200ResponseFlowsInner
    """ # noqa: E501
    app_name: Optional[StrictStr] = Field(default=None, alias="appName")
    client_ip: Optional[StrictStr] = Field(default=None, alias="clientIp")
    client_site: Optional[V2AssuranceFlowSummaryPost200ResponseClientEndpointSite] = Field(default=None, alias="clientSite")
    first_seen_ts: Optional[V1AlarmHistoryGet200ResponseHistoryInnerTime] = Field(default=None, alias="firstSeenTs")
    lan_segment: Optional[StrictStr] = Field(default=None, alias="lanSegment")
    last_seen_ts: Optional[V1AlarmHistoryGet200ResponseHistoryInnerTime] = Field(default=None, alias="lastSeenTs")
    server_ip: Optional[StrictStr] = Field(default=None, alias="serverIp")
    server_port: Optional[StrictInt] = Field(default=None, alias="serverPort")
    server_site: Optional[V2AssuranceFlowSummaryPost200ResponseClientEndpointSite] = Field(default=None, alias="serverSite")
    __properties: ClassVar[List[str]] = ["appName", "clientIp", "clientSite", "firstSeenTs", "lanSegment", "lastSeenTs", "serverIp", "serverPort", "serverSite"]

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
        """Create an instance of V2AssuranceTopologyFlowsPost200ResponseFlowsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_site
        if self.client_site:
            _dict['clientSite'] = self.client_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of first_seen_ts
        if self.first_seen_ts:
            _dict['firstSeenTs'] = self.first_seen_ts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_seen_ts
        if self.last_seen_ts:
            _dict['lastSeenTs'] = self.last_seen_ts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of server_site
        if self.server_site:
            _dict['serverSite'] = self.server_site.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2AssuranceTopologyFlowsPost200ResponseFlowsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appName": obj.get("appName"),
            "clientIp": obj.get("clientIp"),
            "clientSite": V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.from_dict(obj["clientSite"]) if obj.get("clientSite") is not None else None,
            "firstSeenTs": V1AlarmHistoryGet200ResponseHistoryInnerTime.from_dict(obj["firstSeenTs"]) if obj.get("firstSeenTs") is not None else None,
            "lanSegment": obj.get("lanSegment"),
            "lastSeenTs": V1AlarmHistoryGet200ResponseHistoryInnerTime.from_dict(obj["lastSeenTs"]) if obj.get("lastSeenTs") is not None else None,
            "serverIp": obj.get("serverIp"),
            "serverPort": obj.get("serverPort"),
            "serverSite": V2AssuranceFlowSummaryPost200ResponseClientEndpointSite.from_dict(obj["serverSite"]) if obj.get("serverSite") is not None else None
        })
        return _obj


