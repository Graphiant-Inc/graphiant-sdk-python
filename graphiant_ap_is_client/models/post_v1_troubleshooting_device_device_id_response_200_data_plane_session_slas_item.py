from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item_values_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem,
    )


T = TypeVar("T", bound="PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem")


@_attrs_define
class PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        values (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem']]):
    """

    name: Union[Unset, str] = UNSET
    values: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item_values_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItemValuesItem.from_dict(
                values_item_data
            )

            values.append(values_item)

        post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item = cls(
            name=name,
            values=values,
        )

        post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item.additional_properties = d
        return post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item

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
