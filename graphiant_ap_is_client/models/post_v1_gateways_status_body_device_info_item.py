from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GatewaysStatusBodyDeviceInfoItem")


@_attrs_define
class PostV1GatewaysStatusBodyDeviceInfoItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        interface_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    device_id: Union[Unset, str] = UNSET
    interface_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        interface_id = self.interface_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        post_v1_gateways_status_body_device_info_item = cls(
            device_id=device_id,
            interface_id=interface_id,
        )

        post_v1_gateways_status_body_device_info_item.additional_properties = d
        return post_v1_gateways_status_body_device_info_item

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
