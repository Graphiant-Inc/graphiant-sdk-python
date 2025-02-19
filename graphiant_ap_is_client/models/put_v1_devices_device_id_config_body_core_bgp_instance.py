from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreBgpInstance")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreBgpInstance:
    """
    Attributes:
        address_families (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
        asn (Union[Unset, str]):  Example: TYPE_UINT32.
        route_server (Union[Unset, str]):  Example: TYPE_BOOL.
        router_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    address_families: Union[Unset, list[str]] = UNSET
    asn: Union[Unset, str] = UNSET
    route_server: Union[Unset, str] = UNSET
    router_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_families: Union[Unset, list[str]] = UNSET
        if not isinstance(self.address_families, Unset):
            address_families = self.address_families

        asn = self.asn

        route_server = self.route_server

        router_id = self.router_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_families is not UNSET:
            field_dict["addressFamilies"] = address_families
        if asn is not UNSET:
            field_dict["asn"] = asn
        if route_server is not UNSET:
            field_dict["routeServer"] = route_server
        if router_id is not UNSET:
            field_dict["routerId"] = router_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_families = cast(list[str], d.pop("addressFamilies", UNSET))

        asn = d.pop("asn", UNSET)

        route_server = d.pop("routeServer", UNSET)

        router_id = d.pop("routerId", UNSET)

        put_v1_devices_device_id_config_body_core_bgp_instance = cls(
            address_families=address_families,
            asn=asn,
            route_server=route_server,
            router_id=router_id,
        )

        put_v1_devices_device_id_config_body_core_bgp_instance.additional_properties = d
        return put_v1_devices_device_id_config_body_core_bgp_instance

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
