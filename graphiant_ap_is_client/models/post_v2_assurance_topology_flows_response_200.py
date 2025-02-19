from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_flows_response_200_flows_item import (
        PostV2AssuranceTopologyFlowsResponse200FlowsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyFlowsResponse200")


@_attrs_define
class PostV2AssuranceTopologyFlowsResponse200:
    """
    Attributes:
        flows (Union[Unset, list['PostV2AssuranceTopologyFlowsResponse200FlowsItem']]):
    """

    flows: Union[Unset, list["PostV2AssuranceTopologyFlowsResponse200FlowsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flows: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.flows, Unset):
            flows = []
            for flows_item_data in self.flows:
                flows_item = flows_item_data.to_dict()
                flows.append(flows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flows is not UNSET:
            field_dict["flows"] = flows

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_flows_response_200_flows_item import (
            PostV2AssuranceTopologyFlowsResponse200FlowsItem,
        )

        d = src_dict.copy()
        flows = []
        _flows = d.pop("flows", UNSET)
        for flows_item_data in _flows or []:
            flows_item = PostV2AssuranceTopologyFlowsResponse200FlowsItem.from_dict(flows_item_data)

            flows.append(flows_item)

        post_v2_assurance_topology_flows_response_200 = cls(
            flows=flows,
        )

        post_v2_assurance_topology_flows_response_200.additional_properties = d
        return post_v2_assurance_topology_flows_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
