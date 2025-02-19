from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem")


@_attrs_define
class PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem:
    """
    Attributes:
        content (Union[Unset, str]):  Example: TYPE_STRING.
        title (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    content: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        title = d.pop("title", UNSET)

        post_v1_software_gcsrelease_upload_notes_body_details_category_item = cls(
            content=content,
            title=title,
        )

        post_v1_software_gcsrelease_upload_notes_body_details_category_item.additional_properties = d
        return post_v1_software_gcsrelease_upload_notes_body_details_category_item

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
