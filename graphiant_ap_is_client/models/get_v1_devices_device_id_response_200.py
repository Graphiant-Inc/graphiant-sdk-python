from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_response_200_device import GetV1DevicesDeviceIdResponse200Device


T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200")


@_attrs_define
class GetV1DevicesDeviceIdResponse200:
    """
    Attributes:
        device (Union[Unset, GetV1DevicesDeviceIdResponse200Device]):
    """

    device: Union[Unset, "GetV1DevicesDeviceIdResponse200Device"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device, Unset):
            device = self.device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_response_200_device import GetV1DevicesDeviceIdResponse200Device

        d = src_dict.copy()
        _device = d.pop("device", UNSET)
        device: Union[Unset, GetV1DevicesDeviceIdResponse200Device]
        if isinstance(_device, Unset):
            device = UNSET
        else:
            device = GetV1DevicesDeviceIdResponse200Device.from_dict(_device)

        get_v1_devices_device_id_response_200 = cls(
            device=device,
        )

        get_v1_devices_device_id_response_200.additional_properties = d
        return get_v1_devices_device_id_response_200

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
