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
from graphiant_sdk.models.v2_monitoring_extranet_edge_status_get200_response_edge_statuses_inner import V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner
from typing import Optional, Set
from typing_extensions import Self

class V2MonitoringExtranetEdgeStatusGet200Response(BaseModel):
    """
    V2MonitoringExtranetEdgeStatusGet200Response
    """ # noqa: E501
    edge_statuses: Optional[List[V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner]] = Field(default=None, alias="edgeStatuses")
    __properties: ClassVar[List[str]] = ["edgeStatuses"]

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
        """Create an instance of V2MonitoringExtranetEdgeStatusGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in edge_statuses (list)
        _items = []
        if self.edge_statuses:
            for _item_edge_statuses in self.edge_statuses:
                if _item_edge_statuses:
                    _items.append(_item_edge_statuses.to_dict())
            _dict['edgeStatuses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2MonitoringExtranetEdgeStatusGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edgeStatuses": [V2MonitoringExtranetEdgeStatusGet200ResponseEdgeStatusesInner.from_dict(_item) for _item in obj["edgeStatuses"]] if obj.get("edgeStatuses") is not None else None
        })
        return _obj


