from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3_process import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3:
    """
    Attributes:
        process (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process]):
    """

    process: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process, Unset):
            process = self.process.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process is not UNSET:
            field_dict["process"] = process

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3_process import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process,
        )

        d = src_dict.copy()
        _process = d.pop("process", UNSET)
        process: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process]
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOspfv3Process.from_dict(_process)

        put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3 = cls(
            process=process,
        )

        put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3.additional_properties = d
        return put_v1_devices_device_id_config_body_core_core_vrf_ospfv_3

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
