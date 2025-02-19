from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2SiteSiteIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem")


@_attrs_define
class PostV2SiteSiteIdLanSegmentsResponse200DeviceSegmentsItemVrfRoutesItemVrfRouteItem:
    """
    Attributes:
        ipv_4_routes (Union[Unset, str]):  Example: TYPE_INT64.
        ipv_6_routes (Union[Unset, str]):  Example: TYPE_INT64.
        total_routes (Union[Unset, str]):  Example: TYPE_INT64.
        vrf_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ipv_4_routes: Union[Unset, str] = UNSET
    ipv_6_routes: Union[Unset, str] = UNSET
    total_routes: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_4_routes = self.ipv_4_routes

        ipv_6_routes = self.ipv_6_routes

        total_routes = self.total_routes

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv_4_routes is not UNSET:
            field_dict["ipv4Routes"] = ipv_4_routes
        if ipv_6_routes is not UNSET:
            field_dict["ipv6Routes"] = ipv_6_routes
        if total_routes is not UNSET:
            field_dict["totalRoutes"] = total_routes
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipv_4_routes = d.pop("ipv4Routes", UNSET)

        ipv_6_routes = d.pop("ipv6Routes", UNSET)

        total_routes = d.pop("totalRoutes", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        post_v2_site_site_id_lan_segments_response_200_device_segments_item_vrf_routes_item_vrf_route_item = cls(
            ipv_4_routes=ipv_4_routes,
            ipv_6_routes=ipv_6_routes,
            total_routes=total_routes,
            vrf_name=vrf_name,
        )

        post_v2_site_site_id_lan_segments_response_200_device_segments_item_vrf_routes_item_vrf_route_item.additional_properties = d
        return post_v2_site_site_id_lan_segments_response_200_device_segments_item_vrf_routes_item_vrf_route_item

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
