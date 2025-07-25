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
from typing_extensions import Annotated
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta_edges_added_inner import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner
from graphiant_sdk.models.v1_flows_topology_post200_response_network_topology_inner_delta_nodes_added_inner import V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner
from graphiant_sdk.models.v2_notificationlist_post_request_time_window import V2NotificationlistPostRequestTimeWindow
from typing import Optional, Set
from typing_extensions import Self

class V1FlowsTopologyPost200ResponseNetworkTopologyInner(BaseModel):
    """
    V1FlowsTopologyPost200ResponseNetworkTopologyInner
    """ # noqa: E501
    circuit_status: Optional[Dict[str, Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="circuitStatus")
    delta: Optional[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta] = None
    edges: Optional[List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner]] = None
    flows: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    nodes: Optional[List[V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner]] = None
    time_window: Optional[V2NotificationlistPostRequestTimeWindow] = Field(default=None, alias="timeWindow")
    __properties: ClassVar[List[str]] = ["circuitStatus", "delta", "edges", "flows", "nodes", "timeWindow"]

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
        """Create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delta
        if self.delta:
            _dict['delta'] = self.delta.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of time_window
        if self.time_window:
            _dict['timeWindow'] = self.time_window.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1FlowsTopologyPost200ResponseNetworkTopologyInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "circuitStatus": obj.get("circuitStatus"),
            "delta": V1FlowsTopologyPost200ResponseNetworkTopologyInnerDelta.from_dict(obj["delta"]) if obj.get("delta") is not None else None,
            "edges": [V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaEdgesAddedInner.from_dict(_item) for _item in obj["edges"]] if obj.get("edges") is not None else None,
            "flows": obj.get("flows"),
            "nodes": [V1FlowsTopologyPost200ResponseNetworkTopologyInnerDeltaNodesAddedInner.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None,
            "timeWindow": V2NotificationlistPostRequestTimeWindow.from_dict(obj["timeWindow"]) if obj.get("timeWindow") is not None else None
        })
        return _obj


