from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem")


@_attrs_define
class GetV1DeviceRoutingRibVrfDefaultExistResponse200DefaultItem:
    """
    Attributes:
        afi_name (Union[Unset, str]):  Example: ipv4-unicast or ipv6-unicast.
        exist (Union[Unset, str]):  Example: true.
        vrf_name (Union[Unset, str]):  Example: segment-1.
    """

    afi_name: Union[Unset, str] = UNSET
    exist: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        afi_name = self.afi_name

        exist = self.exist

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if afi_name is not UNSET:
            field_dict["afiName"] = afi_name
        if exist is not UNSET:
            field_dict["exist"] = exist
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        afi_name = d.pop("afiName", UNSET)

        exist = d.pop("exist", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        get_v1_device_routing_rib_vrf_default_exist_response_200_default_item = cls(
            afi_name=afi_name,
            exist=exist,
            vrf_name=vrf_name,
        )

        get_v1_device_routing_rib_vrf_default_exist_response_200_default_item.additional_properties = d
        return get_v1_device_routing_rib_vrf_default_exist_response_200_default_item

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
