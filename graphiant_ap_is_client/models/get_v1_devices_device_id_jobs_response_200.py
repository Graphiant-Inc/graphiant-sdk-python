from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item import (
        GetV1DevicesDeviceIdJobsResponse200JobStatusListItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdJobsResponse200")


@_attrs_define
class GetV1DevicesDeviceIdJobsResponse200:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        job_status_list (Union[Unset, list['GetV1DevicesDeviceIdJobsResponse200JobStatusListItem']]):
    """

    device_id: Union[Unset, str] = UNSET
    job_status_list: Union[Unset, list["GetV1DevicesDeviceIdJobsResponse200JobStatusListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        job_status_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_status_list, Unset):
            job_status_list = []
            for job_status_list_item_data in self.job_status_list:
                job_status_list_item = job_status_list_item_data.to_dict()
                job_status_list.append(job_status_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if job_status_list is not UNSET:
            field_dict["jobStatusList"] = job_status_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_jobs_response_200_job_status_list_item import (
            GetV1DevicesDeviceIdJobsResponse200JobStatusListItem,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        job_status_list = []
        _job_status_list = d.pop("jobStatusList", UNSET)
        for job_status_list_item_data in _job_status_list or []:
            job_status_list_item = GetV1DevicesDeviceIdJobsResponse200JobStatusListItem.from_dict(
                job_status_list_item_data
            )

            job_status_list.append(job_status_list_item)

        get_v1_devices_device_id_jobs_response_200 = cls(
            device_id=device_id,
            job_status_list=job_status_list,
        )

        get_v1_devices_device_id_jobs_response_200.additional_properties = d
        return get_v1_devices_device_id_jobs_response_200

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
