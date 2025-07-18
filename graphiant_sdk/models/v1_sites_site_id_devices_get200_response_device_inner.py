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
from graphiant_sdk.models.v1_alarm_history_get200_response_history_inner_time import V1AlarmHistoryGet200ResponseHistoryInnerTime
from typing import Optional, Set
from typing_extensions import Self

class V1SitesSiteIdDevicesGet200ResponseDeviceInner(BaseModel):
    """
    V1SitesSiteIdDevicesGet200ResponseDeviceInner
    """ # noqa: E501
    device_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="deviceId")
    hostname: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    maintenance_mode: Optional[StrictBool] = Field(default=None, alias="maintenanceMode")
    management_ip: Optional[StrictStr] = Field(default=None, alias="managementIp")
    model: Optional[StrictStr] = None
    role: Optional[StrictStr] = None
    serial_number: Optional[StrictStr] = Field(default=None, alias="serialNumber")
    site_id: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="siteId")
    software_version: Optional[StrictStr] = Field(default=None, alias="softwareVersion")
    staging_mode: Optional[StrictBool] = Field(default=None, alias="stagingMode")
    uptime: Optional[V1AlarmHistoryGet200ResponseHistoryInnerTime] = None
    vrrp_interface: Optional[StrictStr] = Field(default=None, alias="vrrpInterface")
    vrrp_state: Optional[StrictStr] = Field(default=None, alias="vrrpState")
    __properties: ClassVar[List[str]] = ["deviceId", "hostname", "location", "maintenanceMode", "managementIp", "model", "role", "serialNumber", "siteId", "softwareVersion", "stagingMode", "uptime", "vrrpInterface", "vrrpState"]

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
        """Create an instance of V1SitesSiteIdDevicesGet200ResponseDeviceInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of uptime
        if self.uptime:
            _dict['uptime'] = self.uptime.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1SitesSiteIdDevicesGet200ResponseDeviceInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deviceId": obj.get("deviceId"),
            "hostname": obj.get("hostname"),
            "location": obj.get("location"),
            "maintenanceMode": obj.get("maintenanceMode"),
            "managementIp": obj.get("managementIp"),
            "model": obj.get("model"),
            "role": obj.get("role"),
            "serialNumber": obj.get("serialNumber"),
            "siteId": obj.get("siteId"),
            "softwareVersion": obj.get("softwareVersion"),
            "stagingMode": obj.get("stagingMode"),
            "uptime": V1AlarmHistoryGet200ResponseHistoryInnerTime.from_dict(obj["uptime"]) if obj.get("uptime") is not None else None,
            "vrrpInterface": obj.get("vrrpInterface"),
            "vrrpState": obj.get("vrrpState")
        })
        return _obj


