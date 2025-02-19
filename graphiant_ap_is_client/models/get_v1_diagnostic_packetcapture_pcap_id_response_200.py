from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DiagnosticPacketcapturePcapIdResponse200")


@_attrs_define
class GetV1DiagnosticPacketcapturePcapIdResponse200:
    """
    Attributes:
        failure_reason (Union[Unset, str]):  Example: failed to access the cloud.
        file_name (Union[Unset, str]):  Example: 12000.tar.zst.gpg.
        status (Union[Unset, str]):  Example: Uploaded.
        upload_progress (Union[Unset, str]):  Example: 60.
        url (Union[Unset, str]):  Example: graphiant.com/pcaps/134.
    """

    failure_reason: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    upload_progress: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_reason = self.failure_reason

        file_name = self.file_name

        status = self.status

        upload_progress = self.upload_progress

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if status is not UNSET:
            field_dict["status"] = status
        if upload_progress is not UNSET:
            field_dict["uploadProgress"] = upload_progress
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        failure_reason = d.pop("failureReason", UNSET)

        file_name = d.pop("fileName", UNSET)

        status = d.pop("status", UNSET)

        upload_progress = d.pop("uploadProgress", UNSET)

        url = d.pop("url", UNSET)

        get_v1_diagnostic_packetcapture_pcap_id_response_200 = cls(
            failure_reason=failure_reason,
            file_name=file_name,
            status=status,
            upload_progress=upload_progress,
            url=url,
        )

        get_v1_diagnostic_packetcapture_pcap_id_response_200.additional_properties = d
        return get_v1_diagnostic_packetcapture_pcap_id_response_200

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
