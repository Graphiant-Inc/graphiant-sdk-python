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
from graphiant_sdk.models.v1_extranets_get200_response_policies_inner_branches_excluded_devices_inner_site_policy_tag_level_one import V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne
from typing import Optional, Set
from typing_extensions import Self

class V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag(BaseModel):
    """
    V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag
    """ # noqa: E501
    level_one: Optional[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne] = Field(default=None, alias="levelOne")
    level_two: Optional[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne] = Field(default=None, alias="levelTwo")
    level_zero: Optional[V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne] = Field(default=None, alias="levelZero")
    __properties: ClassVar[List[str]] = ["levelOne", "levelTwo", "levelZero"]

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
        """Create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of level_one
        if self.level_one:
            _dict['levelOne'] = self.level_one.to_dict()
        # override the default output from pydantic by calling `to_dict()` of level_two
        if self.level_two:
            _dict['levelTwo'] = self.level_two.to_dict()
        # override the default output from pydantic by calling `to_dict()` of level_zero
        if self.level_zero:
            _dict['levelZero'] = self.level_zero.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "levelOne": V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne.from_dict(obj["levelOne"]) if obj.get("levelOne") is not None else None,
            "levelTwo": V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne.from_dict(obj["levelTwo"]) if obj.get("levelTwo") is not None else None,
            "levelZero": V1ExtranetsGet200ResponsePoliciesInnerBranchesExcludedDevicesInnerSitePolicyTagLevelOne.from_dict(obj["levelZero"]) if obj.get("levelZero") is not None else None
        })
        return _obj


