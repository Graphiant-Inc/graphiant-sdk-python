from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_leases_item_ends_at import (
        GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItem")


@_attrs_define
class GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItem:
    """
    Attributes:
        ends_at (Union[Unset, GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        vrf (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ends_at: Union[Unset, "GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt"] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ends_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.to_dict()

        id = self.id

        ip_address = self.ip_address

        mac_address = self.mac_address

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ends_at is not UNSET:
            field_dict["endsAt"] = ends_at
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_leases_item_ends_at import (
            GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt,
        )

        d = src_dict.copy()
        _ends_at = d.pop("endsAt", UNSET)
        ends_at: Union[Unset, GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = GetV1DevicesDeviceIdDhcpServerLeasesResponse200PoolsItemLeasesItemEndsAt.from_dict(_ends_at)

        id = d.pop("id", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        vrf = d.pop("vrf", UNSET)

        get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_leases_item = cls(
            ends_at=ends_at,
            id=id,
            ip_address=ip_address,
            mac_address=mac_address,
            vrf=vrf,
        )

        get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_leases_item.additional_properties = d
        return get_v1_devices_device_id_dhcp_server_leases_response_200_pools_item_leases_item

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
