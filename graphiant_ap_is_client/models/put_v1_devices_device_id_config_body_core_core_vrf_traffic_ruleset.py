from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreCoreVrfTrafficRuleset:
    """
    Attributes:
        ruleset (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ruleset: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ruleset = self.ruleset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ruleset is not UNSET:
            field_dict["ruleset"] = ruleset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ruleset = d.pop("ruleset", UNSET)

        put_v1_devices_device_id_config_body_core_core_vrf_traffic_ruleset = cls(
            ruleset=ruleset,
        )

        put_v1_devices_device_id_config_body_core_core_vrf_traffic_ruleset.additional_properties = d
        return put_v1_devices_device_id_config_body_core_core_vrf_traffic_ruleset

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
