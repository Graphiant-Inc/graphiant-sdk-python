from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_site_lists_body_entries_item_tag import PostV1GlobalSiteListsBodyEntriesItemTag


T = TypeVar("T", bound="PostV1GlobalSiteListsBodyEntriesItem")


@_attrs_define
class PostV1GlobalSiteListsBodyEntriesItem:
    """
    Attributes:
        regular (Union[Unset, str]):  Example: TYPE_INT64.
        tag (Union[Unset, PostV1GlobalSiteListsBodyEntriesItemTag]):
    """

    regular: Union[Unset, str] = UNSET
    tag: Union[Unset, "PostV1GlobalSiteListsBodyEntriesItemTag"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regular = self.regular

        tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regular is not UNSET:
            field_dict["regular"] = regular
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_site_lists_body_entries_item_tag import PostV1GlobalSiteListsBodyEntriesItemTag

        d = src_dict.copy()
        regular = d.pop("regular", UNSET)

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, PostV1GlobalSiteListsBodyEntriesItemTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = PostV1GlobalSiteListsBodyEntriesItemTag.from_dict(_tag)

        post_v1_global_site_lists_body_entries_item = cls(
            regular=regular,
            tag=tag,
        )

        post_v1_global_site_lists_body_entries_item.additional_properties = d
        return post_v1_global_site_lists_body_entries_item

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
