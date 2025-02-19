from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        ipv4 (Union[Unset, str]):  Example: TYPE_STRING.
        ipv6 (Union[Unset, str]):  Example: TYPE_STRING.
        source (Union[Unset, str]):  Example: TYPE_STRING.
        stale (Union[Unset, str]):  Example: TYPE_BOOL.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    circuit_name: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    ipv4: Union[Unset, str] = UNSET
    ipv6: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    stale: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        interface_name = self.interface_name

        ipv4 = self.ipv4

        ipv6 = self.ipv6

        source = self.source

        stale = self.stale

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if source is not UNSET:
            field_dict["source"] = source
        if stale is not UNSET:
            field_dict["stale"] = stale
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        ipv4 = d.pop("ipv4", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        source = d.pop("source", UNSET)

        stale = d.pop("stale", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_item = cls(
            circuit_name=circuit_name,
            interface_name=interface_name,
            ipv4=ipv4,
            ipv6=ipv6,
            source=source,
            stale=stale,
            type_=type_,
        )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_item.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_item

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
