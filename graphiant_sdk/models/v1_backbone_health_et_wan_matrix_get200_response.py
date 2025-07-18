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
from graphiant_sdk.models.v1_backbone_health_et_wan_matrix_get200_response_device_etwan_summary_inner import V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner
from graphiant_sdk.models.v1_backbone_health_et_wan_matrix_get200_response_region_sla_status_inner import V1BackboneHealthEtWanMatrixGet200ResponseRegionSlaStatusInner
from typing import Optional, Set
from typing_extensions import Self

class V1BackboneHealthEtWanMatrixGet200Response(BaseModel):
    """
    V1BackboneHealthEtWanMatrixGet200Response
    """ # noqa: E501
    device_etwan_summary: Optional[List[V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner]] = Field(default=None, alias="deviceEtwanSummary")
    region_sla_status: Optional[List[V1BackboneHealthEtWanMatrixGet200ResponseRegionSlaStatusInner]] = Field(default=None, alias="regionSlaStatus")
    __properties: ClassVar[List[str]] = ["deviceEtwanSummary", "regionSlaStatus"]

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
        """Create an instance of V1BackboneHealthEtWanMatrixGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in device_etwan_summary (list)
        _items = []
        if self.device_etwan_summary:
            for _item_device_etwan_summary in self.device_etwan_summary:
                if _item_device_etwan_summary:
                    _items.append(_item_device_etwan_summary.to_dict())
            _dict['deviceEtwanSummary'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in region_sla_status (list)
        _items = []
        if self.region_sla_status:
            for _item_region_sla_status in self.region_sla_status:
                if _item_region_sla_status:
                    _items.append(_item_region_sla_status.to_dict())
            _dict['regionSlaStatus'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1BackboneHealthEtWanMatrixGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deviceEtwanSummary": [V1BackboneHealthEtWanMatrixGet200ResponseDeviceEtwanSummaryInner.from_dict(_item) for _item in obj["deviceEtwanSummary"]] if obj.get("deviceEtwanSummary") is not None else None,
            "regionSlaStatus": [V1BackboneHealthEtWanMatrixGet200ResponseRegionSlaStatusInner.from_dict(_item) for _item in obj["regionSlaStatus"]] if obj.get("regionSlaStatus") is not None else None
        })
        return _obj


