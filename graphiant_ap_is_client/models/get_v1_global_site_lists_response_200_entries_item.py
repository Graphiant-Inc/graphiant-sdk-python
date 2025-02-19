from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_site_lists_response_200_entries_item_created_at import (
        GetV1GlobalSiteListsResponse200EntriesItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1GlobalSiteListsResponse200EntriesItem")


@_attrs_define
class GetV1GlobalSiteListsResponse200EntriesItem:
    """
    Attributes:
        created_at (Union[Unset, GetV1GlobalSiteListsResponse200EntriesItemCreatedAt]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        edge_references (Union[Unset, str]):  Example: TYPE_INT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        policy_references (Union[Unset, str]):  Example: TYPE_INT32.
        site_list_references (Union[Unset, str]):  Example: TYPE_INT32.
    """

    created_at: Union[Unset, "GetV1GlobalSiteListsResponse200EntriesItemCreatedAt"] = UNSET
    description: Union[Unset, str] = UNSET
    edge_references: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    policy_references: Union[Unset, str] = UNSET
    site_list_references: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        description = self.description

        edge_references = self.edge_references

        id = self.id

        name = self.name

        policy_references = self.policy_references

        site_list_references = self.site_list_references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if edge_references is not UNSET:
            field_dict["edgeReferences"] = edge_references
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if policy_references is not UNSET:
            field_dict["policyReferences"] = policy_references
        if site_list_references is not UNSET:
            field_dict["siteListReferences"] = site_list_references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_site_lists_response_200_entries_item_created_at import (
            GetV1GlobalSiteListsResponse200EntriesItemCreatedAt,
        )

        d = src_dict.copy()
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1GlobalSiteListsResponse200EntriesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1GlobalSiteListsResponse200EntriesItemCreatedAt.from_dict(_created_at)

        description = d.pop("description", UNSET)

        edge_references = d.pop("edgeReferences", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        policy_references = d.pop("policyReferences", UNSET)

        site_list_references = d.pop("siteListReferences", UNSET)

        get_v1_global_site_lists_response_200_entries_item = cls(
            created_at=created_at,
            description=description,
            edge_references=edge_references,
            id=id,
            name=name,
            policy_references=policy_references,
            site_list_references=site_list_references,
        )

        get_v1_global_site_lists_response_200_entries_item.additional_properties = d
        return get_v1_global_site_lists_response_200_entries_item

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
