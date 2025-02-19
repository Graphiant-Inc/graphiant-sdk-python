from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_id_apply_response_202_devices_item import (
        PostV1ExtranetsIdApplyResponse202DevicesItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsIdApplyResponse202")


@_attrs_define
class PostV1ExtranetsIdApplyResponse202:
    """
    Attributes:
        devices (Union[Unset, list['PostV1ExtranetsIdApplyResponse202DevicesItem']]):
        job_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    devices: Union[Unset, list["PostV1ExtranetsIdApplyResponse202DevicesItem"]] = UNSET
    job_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        job_id = self.job_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if job_id is not UNSET:
            field_dict["jobId"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_id_apply_response_202_devices_item import (
            PostV1ExtranetsIdApplyResponse202DevicesItem,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = PostV1ExtranetsIdApplyResponse202DevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        job_id = d.pop("jobId", UNSET)

        post_v1_extranets_id_apply_response_202 = cls(
            devices=devices,
            job_id=job_id,
        )

        post_v1_extranets_id_apply_response_202.additional_properties = d
        return post_v1_extranets_id_apply_response_202

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
