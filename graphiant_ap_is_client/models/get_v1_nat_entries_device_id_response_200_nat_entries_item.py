from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1NatEntriesDeviceIdResponse200NatEntriesItem")


@_attrs_define
class GetV1NatEntriesDeviceIdResponse200NatEntriesItem:
    """
    Attributes:
        destination_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        inside_global_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        inside_global_port (Union[Unset, str]):  Example: TYPE_UINT32.
        inside_local_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        inside_local_port (Union[Unset, str]):  Example: TYPE_UINT32.
        nat_type (Union[Unset, str]):  Example: TYPE_ENUM.
        outside_global_ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        outside_global_port (Union[Unset, str]):  Example: TYPE_UINT32.
        vrf_id (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    destination_ip_address: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    inside_global_ip_address: Union[Unset, str] = UNSET
    inside_global_port: Union[Unset, str] = UNSET
    inside_local_ip_address: Union[Unset, str] = UNSET
    inside_local_port: Union[Unset, str] = UNSET
    nat_type: Union[Unset, str] = UNSET
    outside_global_ip_address: Union[Unset, str] = UNSET
    outside_global_port: Union[Unset, str] = UNSET
    vrf_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_ip_address = self.destination_ip_address

        destination_port = self.destination_port

        inside_global_ip_address = self.inside_global_ip_address

        inside_global_port = self.inside_global_port

        inside_local_ip_address = self.inside_local_ip_address

        inside_local_port = self.inside_local_port

        nat_type = self.nat_type

        outside_global_ip_address = self.outside_global_ip_address

        outside_global_port = self.outside_global_port

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_ip_address is not UNSET:
            field_dict["destinationIpAddress"] = destination_ip_address
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if inside_global_ip_address is not UNSET:
            field_dict["insideGlobalIpAddress"] = inside_global_ip_address
        if inside_global_port is not UNSET:
            field_dict["insideGlobalPort"] = inside_global_port
        if inside_local_ip_address is not UNSET:
            field_dict["insideLocalIpAddress"] = inside_local_ip_address
        if inside_local_port is not UNSET:
            field_dict["insideLocalPort"] = inside_local_port
        if nat_type is not UNSET:
            field_dict["natType"] = nat_type
        if outside_global_ip_address is not UNSET:
            field_dict["outsideGlobalIpAddress"] = outside_global_ip_address
        if outside_global_port is not UNSET:
            field_dict["outsideGlobalPort"] = outside_global_port
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        destination_ip_address = d.pop("destinationIpAddress", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        inside_global_ip_address = d.pop("insideGlobalIpAddress", UNSET)

        inside_global_port = d.pop("insideGlobalPort", UNSET)

        inside_local_ip_address = d.pop("insideLocalIpAddress", UNSET)

        inside_local_port = d.pop("insideLocalPort", UNSET)

        nat_type = d.pop("natType", UNSET)

        outside_global_ip_address = d.pop("outsideGlobalIpAddress", UNSET)

        outside_global_port = d.pop("outsideGlobalPort", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        get_v1_nat_entries_device_id_response_200_nat_entries_item = cls(
            destination_ip_address=destination_ip_address,
            destination_port=destination_port,
            inside_global_ip_address=inside_global_ip_address,
            inside_global_port=inside_global_port,
            inside_local_ip_address=inside_local_ip_address,
            inside_local_port=inside_local_port,
            nat_type=nat_type,
            outside_global_ip_address=outside_global_ip_address,
            outside_global_port=outside_global_port,
            vrf_id=vrf_id,
        )

        get_v1_nat_entries_device_id_response_200_nat_entries_item.additional_properties = d
        return get_v1_nat_entries_device_id_response_200_nat_entries_item

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
