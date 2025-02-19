from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_monitoring_segment_route_counts_response_200_data_item_ipv_4_route_count import (
        PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount,
    )
    from ..models.post_v2_monitoring_segment_route_counts_response_200_data_item_ipv_6_route_count import (
        PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount,
    )


T = TypeVar("T", bound="PostV2MonitoringSegmentRouteCountsResponse200DataItem")


@_attrs_define
class PostV2MonitoringSegmentRouteCountsResponse200DataItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        ipv_4_route_count (Union[Unset, PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount]):
        ipv_6_route_count (Union[Unset, PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount]):
        segment_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_id: Union[Unset, str] = UNSET
    ipv_4_route_count: Union[Unset, "PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount"] = UNSET
    ipv_6_route_count: Union[Unset, "PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount"] = UNSET
    segment_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        ipv_4_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipv_4_route_count, Unset):
            ipv_4_route_count = self.ipv_4_route_count.to_dict()

        ipv_6_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipv_6_route_count, Unset):
            ipv_6_route_count = self.ipv_6_route_count.to_dict()

        segment_name = self.segment_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if ipv_4_route_count is not UNSET:
            field_dict["ipv4RouteCount"] = ipv_4_route_count
        if ipv_6_route_count is not UNSET:
            field_dict["ipv6RouteCount"] = ipv_6_route_count
        if segment_name is not UNSET:
            field_dict["segmentName"] = segment_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_monitoring_segment_route_counts_response_200_data_item_ipv_4_route_count import (
            PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount,
        )
        from ..models.post_v2_monitoring_segment_route_counts_response_200_data_item_ipv_6_route_count import (
            PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _ipv_4_route_count = d.pop("ipv4RouteCount", UNSET)
        ipv_4_route_count: Union[Unset, PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount]
        if isinstance(_ipv_4_route_count, Unset):
            ipv_4_route_count = UNSET
        else:
            ipv_4_route_count = PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv4RouteCount.from_dict(
                _ipv_4_route_count
            )

        _ipv_6_route_count = d.pop("ipv6RouteCount", UNSET)
        ipv_6_route_count: Union[Unset, PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount]
        if isinstance(_ipv_6_route_count, Unset):
            ipv_6_route_count = UNSET
        else:
            ipv_6_route_count = PostV2MonitoringSegmentRouteCountsResponse200DataItemIpv6RouteCount.from_dict(
                _ipv_6_route_count
            )

        segment_name = d.pop("segmentName", UNSET)

        post_v2_monitoring_segment_route_counts_response_200_data_item = cls(
            device_id=device_id,
            ipv_4_route_count=ipv_4_route_count,
            ipv_6_route_count=ipv_6_route_count,
            segment_name=segment_name,
        )

        post_v2_monitoring_segment_route_counts_response_200_data_item.additional_properties = d
        return post_v2_monitoring_segment_route_counts_response_200_data_item

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
