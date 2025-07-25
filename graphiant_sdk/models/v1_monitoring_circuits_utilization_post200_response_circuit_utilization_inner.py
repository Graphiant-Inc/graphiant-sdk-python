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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from graphiant_sdk.models.v1_monitoring_circuits_utilization_post200_response_circuit_utilization_inner_queue_utilization_inner import V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInnerQueueUtilizationInner
from typing import Optional, Set
from typing_extensions import Self

class V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner(BaseModel):
    """
    V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner
    """ # noqa: E501
    config_link_up_speed_mbps: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="configLinkUpSpeedMbps")
    name: Optional[StrictStr] = None
    queue_utilization: Optional[List[V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInnerQueueUtilizationInner]] = Field(default=None, alias="queueUtilization")
    __properties: ClassVar[List[str]] = ["configLinkUpSpeedMbps", "name", "queueUtilization"]

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
        """Create an instance of V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in queue_utilization (list)
        _items = []
        if self.queue_utilization:
            for _item_queue_utilization in self.queue_utilization:
                if _item_queue_utilization:
                    _items.append(_item_queue_utilization.to_dict())
            _dict['queueUtilization'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configLinkUpSpeedMbps": obj.get("configLinkUpSpeedMbps"),
            "name": obj.get("name"),
            "queueUtilization": [V1MonitoringCircuitsUtilizationPost200ResponseCircuitUtilizationInnerQueueUtilizationInner.from_dict(_item) for _item in obj["queueUtilization"]] if obj.get("queueUtilization") is not None else None
        })
        return _obj


