from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_site_lists_id_sites_response_200_entries_item_created_at import (
        GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt,
    )
    from ..models.get_v1_global_site_lists_id_sites_response_200_entries_item_tag_item import (
        GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem,
    )


T = TypeVar("T", bound="GetV1GlobalSiteListsIdSitesResponse200EntriesItem")


@_attrs_define
class GetV1GlobalSiteListsIdSitesResponse200EntriesItem:
    """
    Attributes:
        created_at (Union[Unset, GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt]):
        edge_references (Union[Unset, str]):  Example: TYPE_INT32.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        tag (Union[Unset, list['GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem']]):
    """

    created_at: Union[Unset, "GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt"] = UNSET
    edge_references: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    tag: Union[Unset, list["GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        edge_references = self.edge_references

        site_name = self.site_name

        tag: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = []
            for tag_item_data in self.tag:
                tag_item = tag_item_data.to_dict()
                tag.append(tag_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if edge_references is not UNSET:
            field_dict["edgeReferences"] = edge_references
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_site_lists_id_sites_response_200_entries_item_created_at import (
            GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt,
        )
        from ..models.get_v1_global_site_lists_id_sites_response_200_entries_item_tag_item import (
            GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem,
        )

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1GlobalSiteListsIdSitesResponse200EntriesItemCreatedAt.from_dict(_created_at)

        edge_references = d.pop("edgeReferences", UNSET)

        site_name = d.pop("siteName", UNSET)

        tag = []
        _tag = d.pop("tag", UNSET)
        for tag_item_data in _tag or []:
            tag_item = GetV1GlobalSiteListsIdSitesResponse200EntriesItemTagItem.from_dict(tag_item_data)

            tag.append(tag_item)

        get_v1_global_site_lists_id_sites_response_200_entries_item = cls(
            created_at=created_at,
            edge_references=edge_references,
            site_name=site_name,
            tag=tag,
        )

        get_v1_global_site_lists_id_sites_response_200_entries_item.additional_properties = d
        return get_v1_global_site_lists_id_sites_response_200_entries_item

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
