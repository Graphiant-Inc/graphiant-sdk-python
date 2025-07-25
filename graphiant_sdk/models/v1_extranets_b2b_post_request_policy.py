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
from graphiant_sdk.models.v1_extranets_b2b_consumer_post_request_site_information_inner import V1ExtranetsB2bConsumerPostRequestSiteInformationInner
from graphiant_sdk.models.v1_extranets_b2b_post_request_policy_profiles_inner import V1ExtranetsB2bPostRequestPolicyProfilesInner
from graphiant_sdk.models.v1_extranets_b2b_post_request_policy_sla import V1ExtranetsB2bPostRequestPolicySla
from typing import Optional, Set
from typing_extensions import Self

class V1ExtranetsB2bPostRequestPolicy(BaseModel):
    """
    V1ExtranetsB2bPostRequestPolicy
    """ # noqa: E501
    nat_pools: Optional[List[StrictStr]] = Field(default=None, alias="natPools")
    profiles: Optional[List[V1ExtranetsB2bPostRequestPolicyProfilesInner]] = None
    service_lan_segment: Optional[StrictInt] = Field(default=None, alias="serviceLanSegment")
    service_prefixes: Optional[List[StrictStr]] = Field(default=None, alias="servicePrefixes")
    sites: Optional[List[V1ExtranetsB2bConsumerPostRequestSiteInformationInner]] = None
    sla: Optional[V1ExtranetsB2bPostRequestPolicySla] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["natPools", "profiles", "serviceLanSegment", "servicePrefixes", "sites", "sla", "type"]

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
        """Create an instance of V1ExtranetsB2bPostRequestPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in profiles (list)
        _items = []
        if self.profiles:
            for _item_profiles in self.profiles:
                if _item_profiles:
                    _items.append(_item_profiles.to_dict())
            _dict['profiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sites (list)
        _items = []
        if self.sites:
            for _item_sites in self.sites:
                if _item_sites:
                    _items.append(_item_sites.to_dict())
            _dict['sites'] = _items
        # override the default output from pydantic by calling `to_dict()` of sla
        if self.sla:
            _dict['sla'] = self.sla.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1ExtranetsB2bPostRequestPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "natPools": obj.get("natPools"),
            "profiles": [V1ExtranetsB2bPostRequestPolicyProfilesInner.from_dict(_item) for _item in obj["profiles"]] if obj.get("profiles") is not None else None,
            "serviceLanSegment": obj.get("serviceLanSegment"),
            "servicePrefixes": obj.get("servicePrefixes"),
            "sites": [V1ExtranetsB2bConsumerPostRequestSiteInformationInner.from_dict(_item) for _item in obj["sites"]] if obj.get("sites") is not None else None,
            "sla": V1ExtranetsB2bPostRequestPolicySla.from_dict(obj["sla"]) if obj.get("sla") is not None else None,
            "type": obj.get("type")
        })
        return _obj


