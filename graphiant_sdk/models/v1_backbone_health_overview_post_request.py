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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_backbone_health_overview_post_request_dimensions import V1BackboneHealthOverviewPostRequestDimensions
from graphiant_sdk.models.v1_backbone_health_overview_post_request_filter import V1BackboneHealthOverviewPostRequestFilter
from typing import Optional, Set
from typing_extensions import Self

class V1BackboneHealthOverviewPostRequest(BaseModel):
    """
    V1BackboneHealthOverviewPostRequest
    """ # noqa: E501
    dimensions: Optional[V1BackboneHealthOverviewPostRequestDimensions] = None
    filter: Optional[V1BackboneHealthOverviewPostRequestFilter] = None
    __properties: ClassVar[List[str]] = ["dimensions", "filter"]

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
        """Create an instance of V1BackboneHealthOverviewPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1BackboneHealthOverviewPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dimensions": V1BackboneHealthOverviewPostRequestDimensions.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None,
            "filter": V1BackboneHealthOverviewPostRequestFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None
        })
        return _obj


