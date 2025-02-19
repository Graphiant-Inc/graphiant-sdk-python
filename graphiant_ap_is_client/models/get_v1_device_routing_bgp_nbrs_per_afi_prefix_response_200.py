from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200_prefixes_item import (
        GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200")


@_attrs_define
class GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200:
    """
    Attributes:
        prefixes (Union[Unset, list['GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem']]):
    """

    prefixes: Union[Unset, list["GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefixes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefixes, Unset):
            prefixes = []
            for prefixes_item_data in self.prefixes:
                prefixes_item = prefixes_item_data.to_dict()
                prefixes.append(prefixes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefixes is not UNSET:
            field_dict["prefixes"] = prefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200_prefixes_item import (
            GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem,
        )

        d = src_dict.copy()
        prefixes = []
        _prefixes = d.pop("prefixes", UNSET)
        for prefixes_item_data in _prefixes or []:
            prefixes_item = GetV1DeviceRoutingBgpNbrsPerAfiPrefixResponse200PrefixesItem.from_dict(prefixes_item_data)

            prefixes.append(prefixes_item)

        get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200 = cls(
            prefixes=prefixes,
        )

        get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200.additional_properties = d
        return get_v1_device_routing_bgp_nbrs_per_afi_prefix_response_200

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
