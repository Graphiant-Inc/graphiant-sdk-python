from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1LldpInterfaceIdNeighborsResponse200NeighborsItem")


@_attrs_define
class GetV1LldpInterfaceIdNeighborsResponse200NeighborsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interface (Union[Unset, str]):  Example: TYPE_STRING.
        ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        port (Union[Unset, str]):  Example: TYPE_STRING.
        system_name (Union[Unset, str]):  Example: TYPE_STRING.
        vendor (Union[Unset, str]):  Example: TYPE_STRING.
    """

    id: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    port: Union[Unset, str] = UNSET
    system_name: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        interface = self.interface

        ip_address = self.ip_address

        mac_address = self.mac_address

        port = self.port

        system_name = self.system_name

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if port is not UNSET:
            field_dict["port"] = port
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        port = d.pop("port", UNSET)

        system_name = d.pop("systemName", UNSET)

        vendor = d.pop("vendor", UNSET)

        get_v1_lldp_interface_id_neighbors_response_200_neighbors_item = cls(
            id=id,
            interface=interface,
            ip_address=ip_address,
            mac_address=mac_address,
            port=port,
            system_name=system_name,
            vendor=vendor,
        )

        get_v1_lldp_interface_id_neighbors_response_200_neighbors_item.additional_properties = d
        return get_v1_lldp_interface_id_neighbors_response_200_neighbors_item

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
