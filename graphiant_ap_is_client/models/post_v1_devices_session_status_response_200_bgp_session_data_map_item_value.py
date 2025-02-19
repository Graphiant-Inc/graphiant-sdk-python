from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DevicesSessionStatusResponse200BgpSessionDataMapItemValue")


@_attrs_define
class PostV1DevicesSessionStatusResponse200BgpSessionDataMapItemValue:
    """
    Attributes:
        core_bgp_neighbors_count (Union[Unset, str]):  Example: TYPE_INT32.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        odp_bgp_neighbors_count (Union[Unset, str]):  Example: TYPE_INT32.
        wan_interfaces_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    core_bgp_neighbors_count: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    odp_bgp_neighbors_count: Union[Unset, str] = UNSET
    wan_interfaces_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        core_bgp_neighbors_count = self.core_bgp_neighbors_count

        device_id = self.device_id

        odp_bgp_neighbors_count = self.odp_bgp_neighbors_count

        wan_interfaces_count = self.wan_interfaces_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if core_bgp_neighbors_count is not UNSET:
            field_dict["coreBgpNeighborsCount"] = core_bgp_neighbors_count
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if odp_bgp_neighbors_count is not UNSET:
            field_dict["odpBgpNeighborsCount"] = odp_bgp_neighbors_count
        if wan_interfaces_count is not UNSET:
            field_dict["wanInterfacesCount"] = wan_interfaces_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        core_bgp_neighbors_count = d.pop("coreBgpNeighborsCount", UNSET)

        device_id = d.pop("deviceId", UNSET)

        odp_bgp_neighbors_count = d.pop("odpBgpNeighborsCount", UNSET)

        wan_interfaces_count = d.pop("wanInterfacesCount", UNSET)

        post_v1_devices_session_status_response_200_bgp_session_data_map_item_value = cls(
            core_bgp_neighbors_count=core_bgp_neighbors_count,
            device_id=device_id,
            odp_bgp_neighbors_count=odp_bgp_neighbors_count,
            wan_interfaces_count=wan_interfaces_count,
        )

        post_v1_devices_session_status_response_200_bgp_session_data_map_item_value.additional_properties = d
        return post_v1_devices_session_status_response_200_bgp_session_data_map_item_value

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
