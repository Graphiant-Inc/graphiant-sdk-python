from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_policy_prefix_sets_id_body_entries_item import PutV1PolicyPrefixSetsIdBodyEntriesItem
    from ..models.put_v1_policy_prefix_sets_id_body_prefix_set_entries_item import (
        PutV1PolicyPrefixSetsIdBodyPrefixSetEntriesItem,
    )


T = TypeVar("T", bound="PutV1PolicyPrefixSetsIdBody")


@_attrs_define
class PutV1PolicyPrefixSetsIdBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        entries (Union[Unset, list['PutV1PolicyPrefixSetsIdBodyEntriesItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_set_entries (Union[Unset, list['PutV1PolicyPrefixSetsIdBodyPrefixSetEntriesItem']]):
    """

    description: Union[Unset, str] = UNSET
    entries: Union[Unset, list["PutV1PolicyPrefixSetsIdBodyEntriesItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    prefix_set_entries: Union[Unset, list["PutV1PolicyPrefixSetsIdBodyPrefixSetEntriesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        name = self.name

        prefix_set_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_set_entries, Unset):
            prefix_set_entries = []
            for prefix_set_entries_item_data in self.prefix_set_entries:
                prefix_set_entries_item = prefix_set_entries_item_data.to_dict()
                prefix_set_entries.append(prefix_set_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if name is not UNSET:
            field_dict["name"] = name
        if prefix_set_entries is not UNSET:
            field_dict["prefixSetEntries"] = prefix_set_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_policy_prefix_sets_id_body_entries_item import PutV1PolicyPrefixSetsIdBodyEntriesItem
        from ..models.put_v1_policy_prefix_sets_id_body_prefix_set_entries_item import (
            PutV1PolicyPrefixSetsIdBodyPrefixSetEntriesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = PutV1PolicyPrefixSetsIdBodyEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        name = d.pop("name", UNSET)

        prefix_set_entries = []
        _prefix_set_entries = d.pop("prefixSetEntries", UNSET)
        for prefix_set_entries_item_data in _prefix_set_entries or []:
            prefix_set_entries_item = PutV1PolicyPrefixSetsIdBodyPrefixSetEntriesItem.from_dict(
                prefix_set_entries_item_data
            )

            prefix_set_entries.append(prefix_set_entries_item)

        put_v1_policy_prefix_sets_id_body = cls(
            description=description,
            entries=entries,
            name=name,
            prefix_set_entries=prefix_set_entries,
        )

        put_v1_policy_prefix_sets_id_body.additional_properties = d
        return put_v1_policy_prefix_sets_id_body

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
