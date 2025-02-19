from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set import (
        PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyGlobalPrefixSetsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodyGlobalPrefixSetsItemValue:
    """
    Attributes:
        prefix_set (Union[Unset, PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet]):
    """

    prefix_set: Union[Unset, "PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet"] = UNSET
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
        from ..models.patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set import (
            PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet,
        )

        d = src_dict.copy()
        _prefix_set = d.pop("prefixSet", UNSET)
        prefix_set: Union[Unset, PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet]
        if isinstance(_prefix_set, Unset):
            prefix_set = UNSET
        else:
            prefix_set = PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet.from_dict(_prefix_set)

        patch_v1_global_config_body_global_prefix_sets_item_value = cls(
            prefix_set=prefix_set,
        )

        patch_v1_global_config_body_global_prefix_sets_item_value.additional_properties = d
        return patch_v1_global_config_body_global_prefix_sets_item_value

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
