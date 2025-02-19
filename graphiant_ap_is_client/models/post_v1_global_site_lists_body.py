from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_site_lists_body_entries_item import PostV1GlobalSiteListsBodyEntriesItem


T = TypeVar("T", bound="PostV1GlobalSiteListsBody")


@_attrs_define
class PostV1GlobalSiteListsBody:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        entries (Union[Unset, list['PostV1GlobalSiteListsBodyEntriesItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    entries: Union[Unset, list["PostV1GlobalSiteListsBodyEntriesItem"]] = UNSET
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

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_site_lists_body_entries_item import PostV1GlobalSiteListsBodyEntriesItem

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = PostV1GlobalSiteListsBodyEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        name = d.pop("name", UNSET)

        post_v1_global_site_lists_body = cls(
            description=description,
            entries=entries,
            name=name,
        )

        post_v1_global_site_lists_body.additional_properties = d
        return post_v1_global_site_lists_body

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
