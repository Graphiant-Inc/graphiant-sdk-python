from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1SitesResponse200SitePolicyTagLevelZero")


@_attrs_define
class PostV1SitesResponse200SitePolicyTagLevelZero:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        tag (Union[Unset, str]):  Example: TYPE_STRING.
        tag_value (Union[Unset, str]):  Example: TYPE_INT32.
    """

    id: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tag_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tag = self.tag

        tag_value = self.tag_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tag_value is not UNSET:
            field_dict["tagValue"] = tag_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        tag = d.pop("tag", UNSET)

        tag_value = d.pop("tagValue", UNSET)

        post_v1_sites_response_200_site_policy_tag_level_zero = cls(
            id=id,
            tag=tag,
            tag_value=tag_value,
        )

        post_v1_sites_response_200_site_policy_tag_level_zero.additional_properties = d
        return post_v1_sites_response_200_site_policy_tag_level_zero

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
