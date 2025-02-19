from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_lan_segments_response_200_entries_item_created_at import (
        GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1GlobalLanSegmentsResponse200EntriesItem")


@_attrs_define
class GetV1GlobalLanSegmentsResponse200EntriesItem:
    """
    Attributes:
        associated_interfaces (Union[Unset, str]):  Example: TYPE_INT32.
        created_at (Union[Unset, GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        edge_references (Union[Unset, str]):  Example: TYPE_INT32.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        site_list_references (Union[Unset, str]):  Example: TYPE_INT32.
    """

    associated_interfaces: Union[Unset, str] = UNSET
    created_at: Union[Unset, "GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt"] = UNSET
    description: Union[Unset, str] = UNSET
    edge_references: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    site_list_references: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associated_interfaces = self.associated_interfaces

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        description = self.description

        edge_references = self.edge_references

        id = self.id

        name = self.name

        site_list_references = self.site_list_references

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_interfaces is not UNSET:
            field_dict["associatedInterfaces"] = associated_interfaces
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
        if site_list_references is not UNSET:
            field_dict["siteListReferences"] = site_list_references

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_lan_segments_response_200_entries_item_created_at import (
            GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt,
        )

        d = src_dict.copy()
        associated_interfaces = d.pop("associatedInterfaces", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1GlobalLanSegmentsResponse200EntriesItemCreatedAt.from_dict(_created_at)

        description = d.pop("description", UNSET)

        edge_references = d.pop("edgeReferences", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        site_list_references = d.pop("siteListReferences", UNSET)

        get_v1_global_lan_segments_response_200_entries_item = cls(
            associated_interfaces=associated_interfaces,
            created_at=created_at,
            description=description,
            edge_references=edge_references,
            id=id,
            name=name,
            site_list_references=site_list_references,
        )

        get_v1_global_lan_segments_response_200_entries_item.additional_properties = d
        return get_v1_global_lan_segments_response_200_entries_item

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
