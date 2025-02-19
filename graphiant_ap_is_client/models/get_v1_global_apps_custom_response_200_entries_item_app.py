from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_apps_custom_response_200_entries_item_app_identifier import (
        GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier,
    )


T = TypeVar("T", bound="GetV1GlobalAppsCustomResponse200EntriesItemApp")


@_attrs_define
class GetV1GlobalAppsCustomResponse200EntriesItemApp:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        identifier (Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    identifier: Union[Unset, "GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        identifier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_apps_custom_response_200_entries_item_app_identifier import (
            GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: Union[Unset, GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier]
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = GetV1GlobalAppsCustomResponse200EntriesItemAppIdentifier.from_dict(_identifier)

        name = d.pop("name", UNSET)

        get_v1_global_apps_custom_response_200_entries_item_app = cls(
            description=description,
            identifier=identifier,
            name=name,
        )

        get_v1_global_apps_custom_response_200_entries_item_app.additional_properties = d
        return get_v1_global_apps_custom_response_200_entries_item_app

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
