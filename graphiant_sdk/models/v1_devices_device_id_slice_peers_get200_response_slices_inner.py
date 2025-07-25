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
from graphiant_sdk.models.v1_devices_device_id_slice_peers_get200_response_slices_inner_peers_inner import V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner
from typing import Optional, Set
from typing_extensions import Self

class V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner(BaseModel):
    """
    V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner
    """ # noqa: E501
    id: Optional[StrictInt] = None
    peers: Optional[List[V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner]] = None
    slice_index: Optional[StrictInt] = Field(default=None, alias="sliceIndex")
    tags: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["id", "peers", "sliceIndex", "tags"]

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
        """Create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item_peers in self.peers:
                if _item_peers:
                    _items.append(_item_peers.to_dict())
            _dict['peers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "peers": [V1DevicesDeviceIdSlicePeersGet200ResponseSlicesInnerPeersInner.from_dict(_item) for _item in obj["peers"]] if obj.get("peers") is not None else None,
            "sliceIndex": obj.get("sliceIndex"),
            "tags": obj.get("tags")
        })
        return _obj


