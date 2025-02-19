from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringSegmentRouteCountsBody")


@_attrs_define
class PostV2MonitoringSegmentRouteCountsBody:
    """
    Attributes:
        device_ids (Union[Unset, list[str]]):  Example: ['TYPE_UINT64'].
    """

    device_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_ids is not UNSET:
            field_dict["deviceIds"] = device_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_ids = cast(list[str], d.pop("deviceIds", UNSET))

        post_v2_monitoring_segment_route_counts_body = cls(
            device_ids=device_ids,
        )

        post_v2_monitoring_segment_route_counts_body.additional_properties = d
        return post_v2_monitoring_segment_route_counts_body

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
