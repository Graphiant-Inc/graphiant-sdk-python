from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem")


@_attrs_define
class PostV2AssuranceTopologyOverviewResponse200TopologyPathsItem:
    """
    Attributes:
        node_ids (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    node_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.node_ids, Unset):
            node_ids = self.node_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_ids is not UNSET:
            field_dict["nodeIds"] = node_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        node_ids = cast(list[str], d.pop("nodeIds", UNSET))

        post_v2_assurance_topology_overview_response_200_topology_paths_item = cls(
            node_ids=node_ids,
        )

        post_v2_assurance_topology_overview_response_200_topology_paths_item.additional_properties = d
        return post_v2_assurance_topology_overview_response_200_topology_paths_item

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
