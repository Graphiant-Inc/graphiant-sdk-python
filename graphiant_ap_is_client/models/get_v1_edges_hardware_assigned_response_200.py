from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_edges_hardware_assigned_response_200_edges_summary_item import (
        GetV1EdgesHardwareAssignedResponse200EdgesSummaryItem,
    )


T = TypeVar("T", bound="GetV1EdgesHardwareAssignedResponse200")


@_attrs_define
class GetV1EdgesHardwareAssignedResponse200:
    """
    Attributes:
        edges_summary (Union[Unset, list['GetV1EdgesHardwareAssignedResponse200EdgesSummaryItem']]):
    """

    edges_summary: Union[Unset, list["GetV1EdgesHardwareAssignedResponse200EdgesSummaryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edges_summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges_summary, Unset):
            edges_summary = []
            for edges_summary_item_data in self.edges_summary:
                edges_summary_item = edges_summary_item_data.to_dict()
                edges_summary.append(edges_summary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edges_summary is not UNSET:
            field_dict["edgesSummary"] = edges_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_edges_hardware_assigned_response_200_edges_summary_item import (
            GetV1EdgesHardwareAssignedResponse200EdgesSummaryItem,
        )

        d = src_dict.copy()
        edges_summary = []
        _edges_summary = d.pop("edgesSummary", UNSET)
        for edges_summary_item_data in _edges_summary or []:
            edges_summary_item = GetV1EdgesHardwareAssignedResponse200EdgesSummaryItem.from_dict(
                edges_summary_item_data
            )

            edges_summary.append(edges_summary_item)

        get_v1_edges_hardware_assigned_response_200 = cls(
            edges_summary=edges_summary,
        )

        get_v1_edges_hardware_assigned_response_200.additional_properties = d
        return get_v1_edges_hardware_assigned_response_200

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
