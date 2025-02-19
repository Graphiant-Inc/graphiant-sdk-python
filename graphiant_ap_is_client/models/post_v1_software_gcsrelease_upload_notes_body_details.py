from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_software_gcsrelease_upload_notes_body_details_category_item import (
        PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem,
    )
    from ..models.post_v1_software_gcsrelease_upload_notes_body_details_release_ts import (
        PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs,
    )


T = TypeVar("T", bound="PostV1SoftwareGcsreleaseUploadNotesBodyDetails")


@_attrs_define
class PostV1SoftwareGcsreleaseUploadNotesBodyDetails:
    """
    Attributes:
        category (Union[Unset, list['PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem']]):
        major (Union[Unset, str]):  Example: TYPE_BOOL.
        release_ts (Union[Unset, PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs]):
    """

    category: Union[Unset, list["PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem"]] = UNSET
    major: Union[Unset, str] = UNSET
    release_ts: Union[Unset, "PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.to_dict()
                category.append(category_item)

        major = self.major

        release_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.release_ts, Unset):
            release_ts = self.release_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if major is not UNSET:
            field_dict["major"] = major
        if release_ts is not UNSET:
            field_dict["releaseTs"] = release_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_software_gcsrelease_upload_notes_body_details_category_item import (
            PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem,
        )
        from ..models.post_v1_software_gcsrelease_upload_notes_body_details_release_ts import (
            PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs,
        )

        d = src_dict.copy()
        category = []
        _category = d.pop("category", UNSET)
        for category_item_data in _category or []:
            category_item = PostV1SoftwareGcsreleaseUploadNotesBodyDetailsCategoryItem.from_dict(category_item_data)

            category.append(category_item)

        major = d.pop("major", UNSET)

        _release_ts = d.pop("releaseTs", UNSET)
        release_ts: Union[Unset, PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs]
        if isinstance(_release_ts, Unset):
            release_ts = UNSET
        else:
            release_ts = PostV1SoftwareGcsreleaseUploadNotesBodyDetailsReleaseTs.from_dict(_release_ts)

        post_v1_software_gcsrelease_upload_notes_body_details = cls(
            category=category,
            major=major,
            release_ts=release_ts,
        )

        post_v1_software_gcsrelease_upload_notes_body_details.additional_properties = d
        return post_v1_software_gcsrelease_upload_notes_body_details

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
