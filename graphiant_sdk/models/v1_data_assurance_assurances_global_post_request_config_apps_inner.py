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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from graphiant_sdk.models.v1_data_assurance_assurances_global_post_request_config_apps_inner_servers_inner import V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInnerServersInner
from typing import Optional, Set
from typing_extensions import Self

class V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner(BaseModel):
    """
    V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner
    """ # noqa: E501
    bucket_id: Optional[StrictInt] = Field(default=None, alias="bucketId")
    builtin_app_id: Optional[StrictInt] = Field(default=None, alias="builtinAppId")
    custom_app_id: Optional[StrictInt] = Field(default=None, alias="customAppId")
    is_domain: Optional[StrictBool] = Field(default=None, alias="isDomain")
    name: Optional[StrictStr] = None
    servers: Optional[List[V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInnerServersInner]] = None
    use_all_servers: Optional[StrictBool] = Field(default=None, alias="useAllServers")
    __properties: ClassVar[List[str]] = ["bucketId", "builtinAppId", "customAppId", "isDomain", "name", "servers", "useAllServers"]

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
        """Create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in servers (list)
        _items = []
        if self.servers:
            for _item_servers in self.servers:
                if _item_servers:
                    _items.append(_item_servers.to_dict())
            _dict['servers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bucketId": obj.get("bucketId"),
            "builtinAppId": obj.get("builtinAppId"),
            "customAppId": obj.get("customAppId"),
            "isDomain": obj.get("isDomain"),
            "name": obj.get("name"),
            "servers": [V1DataAssuranceAssurancesGlobalPostRequestConfigAppsInnerServersInner.from_dict(_item) for _item in obj["servers"]] if obj.get("servers") is not None else None,
            "useAllServers": obj.get("useAllServers")
        })
        return _obj


