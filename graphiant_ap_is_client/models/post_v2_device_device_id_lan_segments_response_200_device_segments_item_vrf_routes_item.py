from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item_ts import (
        PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs,
    )
    from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item_vrf_route_item import (
        PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem")


@_attrs_define
class PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem:
    """
    Attributes:
        ts (Union[Unset, PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs]):
        vrf_route (Union[Unset,
            list['PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem']]):
    """

    ts: Union[Unset, "PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs"] = UNSET
    vrf_route: Union[
        Unset, list["PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        vrf_route: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrf_route, Unset):
            vrf_route = []
            for vrf_route_item_data in self.vrf_route:
                vrf_route_item = vrf_route_item_data.to_dict()
                vrf_route.append(vrf_route_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ts is not UNSET:
            field_dict["ts"] = ts
        if vrf_route is not UNSET:
            field_dict["vrfRoute"] = vrf_route

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item_ts import (
            PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs,
        )
        from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item_vrf_route_item import (
            PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem,
        )

        d = src_dict.copy()
        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemTs.from_dict(_ts)

        vrf_route = []
        _vrf_route = d.pop("vrfRoute", UNSET)
        for vrf_route_item_data in _vrf_route or []:
            vrf_route_item = (
                PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem.from_dict(
                    vrf_route_item_data
                )
            )

            vrf_route.append(vrf_route_item)

        post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item = cls(
            ts=ts,
            vrf_route=vrf_route,
        )

        post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item.additional_properties = d
        return post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item

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
