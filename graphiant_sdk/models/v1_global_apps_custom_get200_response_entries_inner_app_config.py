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
from graphiant_sdk.models.v1_global_config_patch_request_traffic_policies_security_rulesets_value_ruleset_rules_value_rule_match_destination_port_range import V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange
from typing import Optional, Set
from typing_extensions import Self

class V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig(BaseModel):
    """
    V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig
    """ # noqa: E501
    description: Optional[StrictStr] = None
    ip_lists: Optional[List[StrictStr]] = Field(default=None, alias="ipLists")
    ip_prefixes: Optional[List[StrictStr]] = Field(default=None, alias="ipPrefixes")
    ip_protocol: Optional[StrictStr] = Field(default=None, alias="ipProtocol")
    name: Optional[StrictStr] = None
    port_ranges: Optional[List[V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange]] = Field(default=None, alias="portRanges")
    url: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "ipLists", "ipPrefixes", "ipProtocol", "name", "portRanges", "url"]

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
        """Create an instance of V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in port_ranges (list)
        _items = []
        if self.port_ranges:
            for _item_port_ranges in self.port_ranges:
                if _item_port_ranges:
                    _items.append(_item_port_ranges.to_dict())
            _dict['portRanges'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1GlobalAppsCustomGet200ResponseEntriesInnerAppConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "ipLists": obj.get("ipLists"),
            "ipPrefixes": obj.get("ipPrefixes"),
            "ipProtocol": obj.get("ipProtocol"),
            "name": obj.get("name"),
            "portRanges": [V1GlobalConfigPatchRequestTrafficPoliciesSecurityRulesetsValueRulesetRulesValueRuleMatchDestinationPortRange.from_dict(_item) for _item in obj["portRanges"]] if obj.get("portRanges") is not None else None,
            "url": obj.get("url")
        })
        return _obj


