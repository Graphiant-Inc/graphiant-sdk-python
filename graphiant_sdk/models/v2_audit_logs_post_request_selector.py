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
from graphiant_sdk.models.v1_activity_logs_post_request_selector_job_entity import V1ActivityLogsPostRequestSelectorJobEntity
from typing import Optional, Set
from typing_extensions import Self

class V2AuditLogsPostRequestSelector(BaseModel):
    """
    V2AuditLogsPostRequestSelector
    """ # noqa: E501
    categories: Optional[List[StrictStr]] = None
    entities: Optional[List[V1ActivityLogsPostRequestSelectorJobEntity]] = None
    job_types: Optional[List[StrictStr]] = Field(default=None, alias="jobTypes")
    targets: Optional[List[V1ActivityLogsPostRequestSelectorJobEntity]] = None
    users: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["categories", "entities", "jobTypes", "targets", "users"]

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
        """Create an instance of V2AuditLogsPostRequestSelector from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item_entities in self.entities:
                if _item_entities:
                    _items.append(_item_entities.to_dict())
            _dict['entities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2AuditLogsPostRequestSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": obj.get("categories"),
            "entities": [V1ActivityLogsPostRequestSelectorJobEntity.from_dict(_item) for _item in obj["entities"]] if obj.get("entities") is not None else None,
            "jobTypes": obj.get("jobTypes"),
            "targets": [V1ActivityLogsPostRequestSelectorJobEntity.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None,
            "users": obj.get("users")
        })
        return _obj


