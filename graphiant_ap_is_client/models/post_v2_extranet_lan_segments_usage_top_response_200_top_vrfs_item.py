from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem")


@_attrs_define
class PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        usage = d.pop("usage", UNSET)

        post_v2_extranet_lan_segments_usage_top_response_200_top_vrfs_item = cls(
            id=id,
            name=name,
            usage=usage,
        )

        post_v2_extranet_lan_segments_usage_top_response_200_top_vrfs_item.additional_properties = d
        return post_v2_extranet_lan_segments_usage_top_response_200_top_vrfs_item

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
