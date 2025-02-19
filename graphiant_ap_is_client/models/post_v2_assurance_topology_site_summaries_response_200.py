from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_site_summaries_response_200_summaries_item import (
        PostV2AssuranceTopologySiteSummariesResponse200SummariesItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologySiteSummariesResponse200")


@_attrs_define
class PostV2AssuranceTopologySiteSummariesResponse200:
    """
    Attributes:
        summaries (Union[Unset, list['PostV2AssuranceTopologySiteSummariesResponse200SummariesItem']]):
    """

    summaries: Union[Unset, list["PostV2AssuranceTopologySiteSummariesResponse200SummariesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summaries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = []
            for summaries_item_data in self.summaries:
                summaries_item = summaries_item_data.to_dict()
                summaries.append(summaries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summaries is not UNSET:
            field_dict["summaries"] = summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_site_summaries_response_200_summaries_item import (
            PostV2AssuranceTopologySiteSummariesResponse200SummariesItem,
        )

        d = src_dict.copy()
        summaries = []
        _summaries = d.pop("summaries", UNSET)
        for summaries_item_data in _summaries or []:
            summaries_item = PostV2AssuranceTopologySiteSummariesResponse200SummariesItem.from_dict(summaries_item_data)

            summaries.append(summaries_item)

        post_v2_assurance_topology_site_summaries_response_200 = cls(
            summaries=summaries,
        )

        post_v2_assurance_topology_site_summaries_response_200.additional_properties = d
        return post_v2_assurance_topology_site_summaries_response_200

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
