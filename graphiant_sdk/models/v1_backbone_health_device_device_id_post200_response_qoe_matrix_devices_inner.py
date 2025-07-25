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
from graphiant_sdk.models.v2_assurance_topology_inventory_post200_response_regions_inner import V2AssuranceTopologyInventoryPost200ResponseRegionsInner
from typing import Optional, Set
from typing_extensions import Self

class V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner(BaseModel):
    """
    V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner
    """ # noqa: E501
    device_id: Optional[StrictInt] = Field(default=None, alias="deviceId")
    device_name: Optional[StrictStr] = Field(default=None, alias="deviceName")
    region: Optional[V2AssuranceTopologyInventoryPost200ResponseRegionsInner] = None
    __properties: ClassVar[List[str]] = ["deviceId", "deviceName", "region"]

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
        """Create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1BackboneHealthDeviceDeviceIdPost200ResponseQoeMatrixDevicesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deviceId": obj.get("deviceId"),
            "deviceName": obj.get("deviceName"),
            "region": V2AssuranceTopologyInventoryPost200ResponseRegionsInner.from_dict(obj["region"]) if obj.get("region") is not None else None
        })
        return _obj


