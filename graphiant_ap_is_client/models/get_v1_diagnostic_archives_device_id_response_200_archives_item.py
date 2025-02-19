from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_diagnostic_archives_device_id_response_200_archives_item_created import (
        GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated,
    )


T = TypeVar("T", bound="GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem")


@_attrs_define
class GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItem:
    """
    Attributes:
        archive_file_name (Union[Unset, str]):  Example: 12000.tar.zst.gpg.
        archive_id (Union[Unset, str]):  Example: 1000000.
        archive_url (Union[Unset, str]):  Example: graphiant.com/archives/134.
        created (Union[Unset, GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated]):
        creator (Union[Unset, str]):  Example: 8a2ec658-f25b-11ec-b939-0242ac120002.
        description (Union[Unset, str]):  Example: archive requested to debug tenant A problem in device B.
        progress (Union[Unset, str]):  Example: 80.
        status (Union[Unset, str]):  Example: Uploaded.
        type_ (Union[Unset, str]):  Example: Debug.
    """

    archive_file_name: Union[Unset, str] = UNSET
    archive_id: Union[Unset, str] = UNSET
    archive_url: Union[Unset, str] = UNSET
    created: Union[Unset, "GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated"] = UNSET
    creator: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    progress: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archive_file_name = self.archive_file_name

        archive_id = self.archive_id

        archive_url = self.archive_url

        created: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        creator = self.creator

        description = self.description

        progress = self.progress

        status = self.status

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archive_file_name is not UNSET:
            field_dict["archiveFileName"] = archive_file_name
        if archive_id is not UNSET:
            field_dict["archiveId"] = archive_id
        if archive_url is not UNSET:
            field_dict["archiveUrl"] = archive_url
        if created is not UNSET:
            field_dict["created"] = created
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_diagnostic_archives_device_id_response_200_archives_item_created import (
            GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated,
        )

        d = src_dict.copy()
        archive_file_name = d.pop("archiveFileName", UNSET)

        archive_id = d.pop("archiveId", UNSET)

        archive_url = d.pop("archiveUrl", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = GetV1DiagnosticArchivesDeviceIdResponse200ArchivesItemCreated.from_dict(_created)

        creator = d.pop("creator", UNSET)

        description = d.pop("description", UNSET)

        progress = d.pop("progress", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_diagnostic_archives_device_id_response_200_archives_item = cls(
            archive_file_name=archive_file_name,
            archive_id=archive_id,
            archive_url=archive_url,
            created=created,
            creator=creator,
            description=description,
            progress=progress,
            status=status,
            type_=type_,
        )

        get_v1_diagnostic_archives_device_id_response_200_archives_item.additional_properties = d
        return get_v1_diagnostic_archives_device_id_response_200_archives_item

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
