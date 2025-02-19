from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_device_routing_rib_route_count_response_200_counts_item import (
        PostV1DeviceRoutingRibRouteCountResponse200CountsItem,
    )


T = TypeVar("T", bound="PostV1DeviceRoutingRibRouteCountResponse200")


@_attrs_define
class PostV1DeviceRoutingRibRouteCountResponse200:
    """
    Attributes:
        counts (Union[Unset, list['PostV1DeviceRoutingRibRouteCountResponse200CountsItem']]):
    """

    counts: Union[Unset, list["PostV1DeviceRoutingRibRouteCountResponse200CountsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = []
            for counts_item_data in self.counts:
                counts_item = counts_item_data.to_dict()
                counts.append(counts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_device_routing_rib_route_count_response_200_counts_item import (
            PostV1DeviceRoutingRibRouteCountResponse200CountsItem,
        )

        d = src_dict.copy()
        counts = []
        _counts = d.pop("counts", UNSET)
        for counts_item_data in _counts or []:
            counts_item = PostV1DeviceRoutingRibRouteCountResponse200CountsItem.from_dict(counts_item_data)

            counts.append(counts_item)

        post_v1_device_routing_rib_route_count_response_200 = cls(
            counts=counts,
        )

        post_v1_device_routing_rib_route_count_response_200.additional_properties = d
        return post_v1_device_routing_rib_route_count_response_200

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
