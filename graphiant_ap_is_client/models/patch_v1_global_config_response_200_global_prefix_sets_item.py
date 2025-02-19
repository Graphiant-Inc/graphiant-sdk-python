from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1GlobalConfigResponse200GlobalPrefixSetsItem")


@_attrs_define
class PatchV1GlobalConfigResponse200GlobalPrefixSetsItem:
    """
    Attributes:
        key (Union[Unset, str]):  Example: TYPE_STRING.
        value (Union[Unset, str]):  Example: TYPE_INT64.
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        patch_v1_global_config_response_200_global_prefix_sets_item = cls(
            key=key,
            value=value,
        )

        patch_v1_global_config_response_200_global_prefix_sets_item.additional_properties = d
        return patch_v1_global_config_response_200_global_prefix_sets_item

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
