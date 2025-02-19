from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1SoftwareReleaseNotesResponse200")


@_attrs_define
class GetV1SoftwareReleaseNotesResponse200:
    """
    Attributes:
        release_notes (Union[Unset, str]):  Example: TYPE_STRING.
    """

    release_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_notes = self.release_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if release_notes is not UNSET:
            field_dict["releaseNotes"] = release_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        release_notes = d.pop("releaseNotes", UNSET)

        get_v1_software_release_notes_response_200 = cls(
            release_notes=release_notes,
        )

        get_v1_software_release_notes_response_200.additional_properties = d
        return get_v1_software_release_notes_response_200

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
