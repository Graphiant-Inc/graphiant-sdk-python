from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_version_response_200_updated_version import PostV1VersionResponse200UpdatedVersion


T = TypeVar("T", bound="PostV1VersionResponse200")


@_attrs_define
class PostV1VersionResponse200:
    """
    Attributes:
        updated_version (Union[Unset, PostV1VersionResponse200UpdatedVersion]):
    """

    updated_version: Union[Unset, "PostV1VersionResponse200UpdatedVersion"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_version: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.updated_version, Unset):
            updated_version = self.updated_version.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_version is not UNSET:
            field_dict["updatedVersion"] = updated_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_version_response_200_updated_version import PostV1VersionResponse200UpdatedVersion

        d = src_dict.copy()
        _updated_version = d.pop("updatedVersion", UNSET)
        updated_version: Union[Unset, PostV1VersionResponse200UpdatedVersion]
        if isinstance(_updated_version, Unset):
            updated_version = UNSET
        else:
            updated_version = PostV1VersionResponse200UpdatedVersion.from_dict(_updated_version)

        post_v1_version_response_200 = cls(
            updated_version=updated_version,
        )

        post_v1_version_response_200.additional_properties = d
        return post_v1_version_response_200

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
