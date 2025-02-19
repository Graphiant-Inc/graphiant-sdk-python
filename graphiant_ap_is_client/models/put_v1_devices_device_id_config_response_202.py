from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigResponse202")


@_attrs_define
class PutV1DevicesDeviceIdConfigResponse202:
    """
    Attributes:
        job_id (Union[Unset, str]):  Example: TYPE_INT64.
        workflow_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    job_id: Union[Unset, str] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        put_v1_devices_device_id_config_response_202 = cls(
            job_id=job_id,
            workflow_id=workflow_id,
        )

        put_v1_devices_device_id_config_response_202.additional_properties = d
        return put_v1_devices_device_id_config_response_202

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
