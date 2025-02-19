from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem")


@_attrs_define
class PostV2AssuranceUpdateclassifiedapplicationBodyClassifiedApplicationListItem:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        classification_entry_id (Union[Unset, str]):  Example: TYPE_STRING.
        ip_prefix_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        port_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        protocol_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    app_name: Union[Unset, str] = UNSET
    classification_entry_id: Union[Unset, str] = UNSET
    ip_prefix_list: Union[Unset, list[str]] = UNSET
    port_list: Union[Unset, list[str]] = UNSET
    protocol_list: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        classification_entry_id = self.classification_entry_id

        ip_prefix_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_prefix_list, Unset):
            ip_prefix_list = self.ip_prefix_list

        port_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        protocol_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.protocol_list, Unset):
            protocol_list = self.protocol_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if classification_entry_id is not UNSET:
            field_dict["classificationEntryId"] = classification_entry_id
        if ip_prefix_list is not UNSET:
            field_dict["ipPrefixList"] = ip_prefix_list
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if protocol_list is not UNSET:
            field_dict["protocolList"] = protocol_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        classification_entry_id = d.pop("classificationEntryId", UNSET)

        ip_prefix_list = cast(list[str], d.pop("ipPrefixList", UNSET))

        port_list = cast(list[str], d.pop("portList", UNSET))

        protocol_list = cast(list[str], d.pop("protocolList", UNSET))

        post_v2_assurance_updateclassifiedapplication_body_classified_application_list_item = cls(
            app_name=app_name,
            classification_entry_id=classification_entry_id,
            ip_prefix_list=ip_prefix_list,
            port_list=port_list,
            protocol_list=protocol_list,
        )

        post_v2_assurance_updateclassifiedapplication_body_classified_application_list_item.additional_properties = d
        return post_v2_assurance_updateclassifiedapplication_body_classified_application_list_item

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
