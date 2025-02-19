from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetV1DevicesDeviceIdVersionsVersionResponse200ConfigManaDeviceCircuitsItemBgpMultipath")


@_attrs_define
class GetV1DevicesDeviceIdVersionsVersionResponse200ConfigManaDeviceCircuitsItemBgpMultipath:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        get_v1_devices_device_id_versions_version_response_200_config_mana_device_circuits_item_bgp_multipath = cls()

        get_v1_devices_device_id_versions_version_response_200_config_mana_device_circuits_item_bgp_multipath.additional_properties = d
        return get_v1_devices_device_id_versions_version_response_200_config_mana_device_circuits_item_bgp_multipath

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
