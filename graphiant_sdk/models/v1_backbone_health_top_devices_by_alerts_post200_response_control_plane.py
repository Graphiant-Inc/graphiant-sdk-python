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
from graphiant_sdk.models.v1_backbone_health_top_devices_by_alerts_post200_response_control_plane_device_counts_inner import V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlaneDeviceCountsInner
from typing import Optional, Set
from typing_extensions import Self

class V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane(BaseModel):
    """
    V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane
    """ # noqa: E501
    device_counts: Optional[List[V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlaneDeviceCountsInner]] = Field(default=None, alias="deviceCounts")
    __properties: ClassVar[List[str]] = ["deviceCounts"]

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
        """Create an instance of V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in device_counts (list)
        _items = []
        if self.device_counts:
            for _item_device_counts in self.device_counts:
                if _item_device_counts:
                    _items.append(_item_device_counts.to_dict())
            _dict['deviceCounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlane from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deviceCounts": [V1BackboneHealthTopDevicesByAlertsPost200ResponseControlPlaneDeviceCountsInner.from_dict(_item) for _item in obj["deviceCounts"]] if obj.get("deviceCounts") is not None else None
        })
        return _obj


