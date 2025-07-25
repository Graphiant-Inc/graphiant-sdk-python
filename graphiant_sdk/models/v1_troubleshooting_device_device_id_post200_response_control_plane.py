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
from graphiant_sdk.models.v1_backbone_health_device_device_id_post200_response_control_plane_control_transitions_transitions_inner import V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner
from typing import Optional, Set
from typing_extensions import Self

class V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane(BaseModel):
    """
    V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane
    """ # noqa: E501
    control_transitions: Optional[List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner]] = Field(default=None, alias="controlTransitions")
    management_transitions: Optional[List[V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner]] = Field(default=None, alias="managementTransitions")
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["controlTransitions", "managementTransitions", "status"]

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
        """Create an instance of V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in control_transitions (list)
        _items = []
        if self.control_transitions:
            for _item_control_transitions in self.control_transitions:
                if _item_control_transitions:
                    _items.append(_item_control_transitions.to_dict())
            _dict['controlTransitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in management_transitions (list)
        _items = []
        if self.management_transitions:
            for _item_management_transitions in self.management_transitions:
                if _item_management_transitions:
                    _items.append(_item_management_transitions.to_dict())
            _dict['managementTransitions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1TroubleshootingDeviceDeviceIdPost200ResponseControlPlane from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "controlTransitions": [V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner.from_dict(_item) for _item in obj["controlTransitions"]] if obj.get("controlTransitions") is not None else None,
            "managementTransitions": [V1BackboneHealthDeviceDeviceIdPost200ResponseControlPlaneControlTransitionsTransitionsInner.from_dict(_item) for _item in obj["managementTransitions"]] if obj.get("managementTransitions") is not None else None,
            "status": obj.get("status")
        })
        return _obj


