from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item_completed_at import (
        GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt,
    )
    from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item_created_at import (
        GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdJobsResponse200JobStatusListItem")


@_attrs_define
class GetV1DevicesDeviceIdJobsResponse200JobStatusListItem:
    """
    Attributes:
        completed_at (Union[Unset, GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt]):
        created_at (Union[Unset, GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt]):
        error (Union[Unset, str]):  Example: TYPE_STRING.
        error_count (Union[Unset, str]):  Example: TYPE_INT32.
        job_id (Union[Unset, str]):  Example: TYPE_INT64.
        job_state (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    completed_at: Union[Unset, "GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt"] = UNSET
    created_at: Union[Unset, "GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt"] = UNSET
    error: Union[Unset, str] = UNSET
    error_count: Union[Unset, str] = UNSET
    job_id: Union[Unset, str] = UNSET
    job_state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completed_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.to_dict()

        created_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.to_dict()

        error = self.error

        error_count = self.error_count

        job_id = self.job_id

        job_state = self.job_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if error_count is not UNSET:
            field_dict["errorCount"] = error_count
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if job_state is not UNSET:
            field_dict["jobState"] = job_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item_completed_at import (
            GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt,
        )
        from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item_created_at import (
            GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt,
        )

        d = src_dict.copy()
        _completed_at = d.pop("completedAt", UNSET)
        completed_at: Union[Unset, GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCompletedAt.from_dict(_completed_at)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = GetV1DevicesDeviceIdJobsResponse200JobStatusListItemCreatedAt.from_dict(_created_at)

        error = d.pop("error", UNSET)

        error_count = d.pop("errorCount", UNSET)

        job_id = d.pop("jobId", UNSET)

        job_state = d.pop("jobState", UNSET)

        get_v1_devices_device_id_jobs_response_200_job_status_list_item = cls(
            completed_at=completed_at,
            created_at=created_at,
            error=error,
            error_count=error_count,
            job_id=job_id,
            job_state=job_state,
        )

        get_v1_devices_device_id_jobs_response_200_job_status_list_item.additional_properties = d
        return get_v1_devices_device_id_jobs_response_200_job_status_list_item

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
