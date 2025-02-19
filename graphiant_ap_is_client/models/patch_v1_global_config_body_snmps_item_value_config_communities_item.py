from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PatchV1GlobalConfigBodySnmpsItemValueConfigCommunitiesItem")


@_attrs_define
class PatchV1GlobalConfigBodySnmpsItemValueConfigCommunitiesItem:
    """ """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        patch_v1_global_config_body_snmps_item_value_config_communities_item = cls()

        patch_v1_global_config_body_snmps_item_value_config_communities_item.additional_properties = d
        return patch_v1_global_config_body_snmps_item_value_config_communities_item

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
