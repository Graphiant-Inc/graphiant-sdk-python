from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_jobs_job_id_response_200_job_status import (
        GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdJobsJobIdResponse200")


@_attrs_define
class GetV1DevicesDeviceIdJobsJobIdResponse200:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        job_status (Union[Unset, GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus]):
    """

    device_id: Union[Unset, str] = UNSET
    job_status: Union[Unset, "GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        job_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_jobs_job_id_response_200_job_status import (
            GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = GetV1DevicesDeviceIdJobsJobIdResponse200JobStatus.from_dict(_job_status)

        get_v1_devices_device_id_jobs_job_id_response_200 = cls(
            device_id=device_id,
            job_status=job_status,
        )

        get_v1_devices_device_id_jobs_job_id_response_200.additional_properties = d
        return get_v1_devices_device_id_jobs_job_id_response_200

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
