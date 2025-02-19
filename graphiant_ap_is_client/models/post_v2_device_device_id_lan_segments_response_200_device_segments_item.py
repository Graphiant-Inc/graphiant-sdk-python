from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item import (
        PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem")


@_attrs_define
class PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_routes (Union[Unset, list['PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem']]):
    """

    device_id: Union[Unset, str] = UNSET
    vrf_routes: Union[Unset, list["PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        vrf_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrf_routes, Unset):
            vrf_routes = []
            for vrf_routes_item_data in self.vrf_routes:
                vrf_routes_item = vrf_routes_item_data.to_dict()
                vrf_routes.append(vrf_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if vrf_routes is not UNSET:
            field_dict["vrfRoutes"] = vrf_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_lan_segments_response_200_device_segments_item_vrf_routes_item import (
            PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        vrf_routes = []
        _vrf_routes = d.pop("vrfRoutes", UNSET)
        for vrf_routes_item_data in _vrf_routes or []:
            vrf_routes_item = PostV2DeviceDeviceIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItem.from_dict(
                vrf_routes_item_data
            )

            vrf_routes.append(vrf_routes_item)

        post_v2_device_device_id_lan_segments_response_200_device_segments_item = cls(
            device_id=device_id,
            vrf_routes=vrf_routes,
        )

        post_v2_device_device_id_lan_segments_response_200_device_segments_item.additional_properties = d
        return post_v2_device_device_id_lan_segments_response_200_device_segments_item

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
