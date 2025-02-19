from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_diagnostic_archives_device_id_response_200_archives_item import (
        GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem,
    )


T = TypeVar("T", bound="GetV1DiagnosticArchivesDeviceIdResponse200")


@_attrs_define
class GetV1DiagnosticArchivesDeviceIdResponse200:
    """
    Attributes:
        archives (Union[Unset, list['GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem']]):
    """

    archives: Union[Unset, list["GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archives: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.archives, Unset):
            archives = []
            for archives_item_data in self.archives:
                archives_item = archives_item_data.to_dict()
                archives.append(archives_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archives is not UNSET:
            field_dict["archives"] = archives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_diagnostic_archives_device_id_response_200_archives_item import (
            GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem,
        )

        d = src_dict.copy()
        archives = []
        _archives = d.pop("archives", UNSET)
        for archives_item_data in _archives or []:
            archives_item = GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem.from_dict(archives_item_data)

            archives.append(archives_item)

        get_v1_diagnostic_archives_device_id_response_200 = cls(
            archives=archives,
        )

        get_v1_diagnostic_archives_device_id_response_200.additional_properties = d
        return get_v1_diagnostic_archives_device_id_response_200

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
