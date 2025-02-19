from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_site_lists_id_response_200_entries_item_tag import (
        GetV1GlobalSiteListsIdResponse200EntriesItemTag,
    )


T = TypeVar("T", bound="GetV1GlobalSiteListsIdResponse200EntriesItem")


@_attrs_define
class GetV1GlobalSiteListsIdResponse200EntriesItem:
    """
    Attributes:
        regular (Union[Unset, str]):  Example: TYPE_INT64.
        tag (Union[Unset, GetV1GlobalSiteListsIdResponse200EntriesItemTag]):
    """

    regular: Union[Unset, str] = UNSET
    tag: Union[Unset, "GetV1GlobalSiteListsIdResponse200EntriesItemTag"] = UNSET
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
        from ..models.get_v1_global_site_lists_id_response_200_entries_item_tag import (
            GetV1GlobalSiteListsIdResponse200EntriesItemTag,
        )

        d = src_dict.copy()
        regular = d.pop("regular", UNSET)

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, GetV1GlobalSiteListsIdResponse200EntriesItemTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = GetV1GlobalSiteListsIdResponse200EntriesItemTag.from_dict(_tag)

        get_v1_global_site_lists_id_response_200_entries_item = cls(
            regular=regular,
            tag=tag,
        )

        get_v1_global_site_lists_id_response_200_entries_item.additional_properties = d
        return get_v1_global_site_lists_id_response_200_entries_item

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
