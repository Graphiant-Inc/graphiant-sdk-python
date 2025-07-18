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
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_edges_inner import V2DeviceDeviceIdTopologyPost200ResponseEdgesInner
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_nodes_inner import V2DeviceDeviceIdTopologyPost200ResponseNodesInner
from graphiant_sdk.models.v2_device_device_id_topology_post200_response_snapshots_inner import V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner
from typing import Optional, Set
from typing_extensions import Self

class V2DeviceDeviceIdTopologyPost200Response(BaseModel):
    """
    V2DeviceDeviceIdTopologyPost200Response
    """ # noqa: E501
    edges: Optional[List[V2DeviceDeviceIdTopologyPost200ResponseEdgesInner]] = None
    nodes: Optional[List[V2DeviceDeviceIdTopologyPost200ResponseNodesInner]] = None
    snapshots: Optional[List[V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner]] = None
    __properties: ClassVar[List[str]] = ["edges", "nodes", "snapshots"]

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
        """Create an instance of V2DeviceDeviceIdTopologyPost200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item_edges in self.edges:
                if _item_edges:
                    _items.append(_item_edges.to_dict())
            _dict['edges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item_nodes in self.nodes:
                if _item_nodes:
                    _items.append(_item_nodes.to_dict())
            _dict['nodes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in snapshots (list)
        _items = []
        if self.snapshots:
            for _item_snapshots in self.snapshots:
                if _item_snapshots:
                    _items.append(_item_snapshots.to_dict())
            _dict['snapshots'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V2DeviceDeviceIdTopologyPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edges": [V2DeviceDeviceIdTopologyPost200ResponseEdgesInner.from_dict(_item) for _item in obj["edges"]] if obj.get("edges") is not None else None,
            "nodes": [V2DeviceDeviceIdTopologyPost200ResponseNodesInner.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "snapshots": [V2DeviceDeviceIdTopologyPost200ResponseSnapshotsInner.from_dict(_item) for _item in obj["snapshots"]] if obj.get("snapshots") is not None else None
        })
        return _obj


