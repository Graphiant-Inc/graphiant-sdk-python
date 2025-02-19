from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemBgp")


@_attrs_define
class GetV1DevicesResponse200DevicesItemBgp:
    """
    Attributes:
        asn (Union[Unset, str]):  Example: TYPE_UINT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        router_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    asn: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    router_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asn = self.asn

        id = self.id

        router_id = self.router_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asn is not UNSET:
            field_dict["asn"] = asn
        if id is not UNSET:
            field_dict["id"] = id
        if router_id is not UNSET:
            field_dict["routerId"] = router_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        asn = d.pop("asn", UNSET)

        id = d.pop("id", UNSET)

        router_id = d.pop("routerId", UNSET)

        get_v1_devices_response_200_devices_item_bgp = cls(
            asn=asn,
            id=id,
            router_id=router_id,
        )

        get_v1_devices_response_200_devices_item_bgp.additional_properties = d
        return get_v1_devices_response_200_devices_item_bgp

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
