from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticArchiveCreateDeviceIdResponse201")


@_attrs_define
class PostV1DiagnosticArchiveCreateDeviceIdResponse201:
    """
    Attributes:
        archive_id (Union[Unset, str]):  Example: 1000000.
    """

    archive_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_id = self.archive_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archive_id is not UNSET:
            field_dict["archiveId"] = archive_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        archive_id = d.pop("archiveId", UNSET)

        post_v1_diagnostic_archive_create_device_id_response_201 = cls(
            archive_id=archive_id,
        )

        post_v1_diagnostic_archive_create_device_id_response_201.additional_properties = d
        return post_v1_diagnostic_archive_create_device_id_response_201

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
