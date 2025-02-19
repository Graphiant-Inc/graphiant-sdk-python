from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemRangesItem")


@_attrs_define
class GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemRangesItem:
    """
    Attributes:
        end (Union[Unset, str]):  Example: TYPE_STRING.
        start (Union[Unset, str]):  Example: TYPE_STRING.
    """

    end: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        end = d.pop("end", UNSET)

        start = d.pop("start", UNSET)

        get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_ranges_item = cls(
            end=end,
            start=start,
        )

        get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_ranges_item.additional_properties = d
        return get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_ranges_item

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
