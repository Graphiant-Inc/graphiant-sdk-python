from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalSnmpsResponse200SnmpsItemEngineEndpointsItem")


@_attrs_define
class PostV1GlobalSnmpsResponse200SnmpsItemEngineEndpointsItem:
    """
    Attributes:
        addresses (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        auto_ipv_4 (Union[Unset, str]):  Example: TYPE_BOOL.
        auto_ipv_6 (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        lan_segment (Union[Unset, str]):  Example: TYPE_STRING.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    addresses: Union[Unset, list[str]] = UNSET
    auto_ipv_4: Union[Unset, str] = UNSET
    auto_ipv_6: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    lan_segment: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        auto_ipv_4 = self.auto_ipv_4

        auto_ipv_6 = self.auto_ipv_6

        id = self.id

        interface_name = self.interface_name

        lan_segment = self.lan_segment

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if auto_ipv_4 is not UNSET:
            field_dict["autoIpv4"] = auto_ipv_4
        if auto_ipv_6 is not UNSET:
            field_dict["autoIpv6"] = auto_ipv_6
        if id is not UNSET:
            field_dict["id"] = id
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        addresses = cast(list[str], d.pop("addresses", UNSET))

        auto_ipv_4 = d.pop("autoIpv4", UNSET)

        auto_ipv_6 = d.pop("autoIpv6", UNSET)

        id = d.pop("id", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        lan_segment = d.pop("lanSegment", UNSET)

        name = d.pop("name", UNSET)

        post_v1_global_snmps_response_200_snmps_item_engine_endpoints_item = cls(
            addresses=addresses,
            auto_ipv_4=auto_ipv_4,
            auto_ipv_6=auto_ipv_6,
            id=id,
            interface_name=interface_name,
            lan_segment=lan_segment,
            name=name,
        )

        post_v1_global_snmps_response_200_snmps_item_engine_endpoints_item.additional_properties = d
        return post_v1_global_snmps_response_200_snmps_item_engine_endpoints_item

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
