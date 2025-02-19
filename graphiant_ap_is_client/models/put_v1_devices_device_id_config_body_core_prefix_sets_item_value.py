from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_prefix_sets_item_value_prefix_set import (
        PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValue:
    """
    Attributes:
        prefix_set (Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet]):
    """

    prefix_set: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prefix_set: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prefix_set, Unset):
            prefix_set = self.prefix_set.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prefix_set is not UNSET:
            field_dict["prefixSet"] = prefix_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_prefix_sets_item_value_prefix_set import (
            PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet,
        )

        d = src_dict.copy()
        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItemValuePrefixSet.from_dict(_prefix_set)

        put_v1_devices_device_id_config_body_core_prefix_sets_item_value = cls(
            prefix_set=prefix_set,
        )

        put_v1_devices_device_id_config_body_core_prefix_sets_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_core_prefix_sets_item_value

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
