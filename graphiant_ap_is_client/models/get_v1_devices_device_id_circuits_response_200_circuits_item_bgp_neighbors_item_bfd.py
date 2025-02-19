from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfd")


@_attrs_define
class GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemBgpNeighborsItemBfd:
    """
    Attributes:
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        minimum_interval (Union[Unset, str]):  Example: TYPE_UINT32.
        multiplier (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    enabled: Union[Unset, str] = UNSET
    minimum_interval: Union[Unset, str] = UNSET
    multiplier: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        minimum_interval = self.minimum_interval

        multiplier = self.multiplier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if minimum_interval is not UNSET:
            field_dict["minimumInterval"] = minimum_interval
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        minimum_interval = d.pop("minimumInterval", UNSET)

        multiplier = d.pop("multiplier", UNSET)

        get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd = cls(
            enabled=enabled,
            minimum_interval=minimum_interval,
            multiplier=multiplier,
        )

        get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd.additional_properties = d
        return get_v1_devices_device_id_circuits_response_200_circuits_item_bgp_neighbors_item_bfd

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
