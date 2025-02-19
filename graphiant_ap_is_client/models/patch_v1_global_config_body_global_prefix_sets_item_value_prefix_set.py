from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set_entries_item import (
        PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSetEntriesItem,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet")


@_attrs_define
class PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSet:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        entries (Union[Unset, list['PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSetEntriesItem']]):
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_global_sync (Union[Unset, str]):  Example: TYPE_BOOL.
        mode (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    entries: Union[Unset, list["PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSetEntriesItem"]] = UNSET
    global_id: Union[Unset, str] = UNSET
    is_global_sync: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        global_id = self.global_id

        is_global_sync = self.is_global_sync

        mode = self.mode

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if is_global_sync is not UNSET:
            field_dict["isGlobalSync"] = is_global_sync
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set_entries_item import (
            PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSetEntriesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = PatchV1GlobalConfigBodyGlobalPrefixSetsItemValuePrefixSetEntriesItem.from_dict(
                entries_item_data
            )

            entries.append(entries_item)

        global_id = d.pop("globalId", UNSET)

        is_global_sync = d.pop("isGlobalSync", UNSET)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set = cls(
            description=description,
            entries=entries,
            global_id=global_id,
            is_global_sync=is_global_sync,
            mode=mode,
            name=name,
        )

        patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set.additional_properties = d
        return patch_v1_global_config_body_global_prefix_sets_item_value_prefix_set

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
