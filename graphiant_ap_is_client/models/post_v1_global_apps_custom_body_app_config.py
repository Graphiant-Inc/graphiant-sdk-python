from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_global_apps_custom_body_app_config_port_ranges_item import (
        PostV1GlobalAppsCustomBodyAppConfigPortRangesItem,
    )


T = TypeVar("T", bound="PostV1GlobalAppsCustomBodyAppConfig")


@_attrs_define
class PostV1GlobalAppsCustomBodyAppConfig:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        ip_lists (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ip_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        ip_protocol (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        port_ranges (Union[Unset, list['PostV1GlobalAppsCustomBodyAppConfigPortRangesItem']]):
        url (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    ip_lists: Union[Unset, list[str]] = UNSET
    ip_prefixes: Union[Unset, list[str]] = UNSET
    ip_protocol: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    port_ranges: Union[Unset, list["PostV1GlobalAppsCustomBodyAppConfigPortRangesItem"]] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        ip_lists: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_lists, Unset):
            ip_lists = self.ip_lists

        ip_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ip_prefixes, Unset):
            ip_prefixes = self.ip_prefixes

        ip_protocol = self.ip_protocol

        name = self.name

        port_ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.port_ranges, Unset):
            port_ranges = []
            for port_ranges_item_data in self.port_ranges:
                port_ranges_item = port_ranges_item_data.to_dict()
                port_ranges.append(port_ranges_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if ip_lists is not UNSET:
            field_dict["ipLists"] = ip_lists
        if ip_prefixes is not UNSET:
            field_dict["ipPrefixes"] = ip_prefixes
        if ip_protocol is not UNSET:
            field_dict["ipProtocol"] = ip_protocol
        if name is not UNSET:
            field_dict["name"] = name
        if port_ranges is not UNSET:
            field_dict["portRanges"] = port_ranges
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_global_apps_custom_body_app_config_port_ranges_item import (
            PostV1GlobalAppsCustomBodyAppConfigPortRangesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        ip_lists = cast(list[str], d.pop("ipLists", UNSET))

        ip_prefixes = cast(list[str], d.pop("ipPrefixes", UNSET))

        ip_protocol = d.pop("ipProtocol", UNSET)

        name = d.pop("name", UNSET)

        port_ranges = []
        _port_ranges = d.pop("portRanges", UNSET)
        for port_ranges_item_data in _port_ranges or []:
            port_ranges_item = PostV1GlobalAppsCustomBodyAppConfigPortRangesItem.from_dict(port_ranges_item_data)

            port_ranges.append(port_ranges_item)

        url = d.pop("url", UNSET)

        post_v1_global_apps_custom_body_app_config = cls(
            description=description,
            ip_lists=ip_lists,
            ip_prefixes=ip_prefixes,
            ip_protocol=ip_protocol,
            name=name,
            port_ranges=port_ranges,
            url=url,
        )

        post_v1_global_apps_custom_body_app_config.additional_properties = d
        return post_v1_global_apps_custom_body_app_config

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
