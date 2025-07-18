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
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match import V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_traffic_rulesets_value_ruleset_rules_value_rule_action import V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction
from typing import Optional, Set
from typing_extensions import Self

class V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule(BaseModel):
    """
    V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule
    """ # noqa: E501
    action: Optional[V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction] = None
    description: Optional[StrictStr] = None
    match: Optional[V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch] = None
    name: Optional[StrictStr] = None
    seq: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    __properties: ClassVar[List[str]] = ["action", "description", "match", "name", "seq"]

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
        """Create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of match
        if self.match:
            _dict['match'] = self.match.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": V1GlobalConfigPatchRequestTrafficPoliciesTrafficRulesetsValueRulesetRulesValueRuleAction.from_dict(obj["action"]) if obj.get("action") is not None else None,
            "description": obj.get("description"),
            "match": V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatch.from_dict(obj["match"]) if obj.get("match") is not None else None,
            "name": obj.get("name"),
            "seq": obj.get("seq")
        })
        return _obj


