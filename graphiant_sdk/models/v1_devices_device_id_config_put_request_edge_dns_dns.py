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
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_dns_dns_dynamic import V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsDynamic
from graphiant_sdk.models.v1_devices_device_id_config_put_request_edge_dns_dns_static import V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdConfigPutRequestEdgeDnsDns(BaseModel):
    """
    V1DevicesDeviceIdConfigPutRequestEdgeDnsDns
    """ # noqa: E501
    cloudflare: Optional[Dict[str, Any]] = None
    dynamic: Optional[V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsDynamic] = None
    static: Optional[V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic] = None
    __properties: ClassVar[List[str]] = ["cloudflare", "dynamic", "static"]

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
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDns from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dynamic
        if self.dynamic:
            _dict['dynamic'] = self.dynamic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of static
        if self.static:
            _dict['static'] = self.static.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdConfigPutRequestEdgeDnsDns from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudflare": obj.get("cloudflare"),
            "dynamic": V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsDynamic.from_dict(obj["dynamic"]) if obj.get("dynamic") is not None else None,
            "static": V1DevicesDeviceIdConfigPutRequestEdgeDnsDnsStatic.from_dict(obj["static"]) if obj.get("static") is not None else None
        })
        return _obj


