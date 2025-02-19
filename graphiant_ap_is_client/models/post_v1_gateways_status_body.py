from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_gateways_status_body_device_info_item import PostV1GatewaysStatusBodyDeviceInfoItem


T = TypeVar("T", bound="PostV1GatewaysStatusBody")


@_attrs_define
class PostV1GatewaysStatusBody:
    """
    Attributes:
        device_info (Union[Unset, list['PostV1GatewaysStatusBodyDeviceInfoItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        support_status (Union[Unset, str]):  Example: TYPE_STRING.
    """

    device_info: Union[Unset, list["PostV1GatewaysStatusBodyDeviceInfoItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    support_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_info: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_info, Unset):
            device_info = []
            for device_info_item_data in self.device_info:
                device_info_item = device_info_item_data.to_dict()
                device_info.append(device_info_item)

        id = self.id

        status = self.status

        support_status = self.support_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_info is not UNSET:
            field_dict["deviceInfo"] = device_info
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if support_status is not UNSET:
            field_dict["supportStatus"] = support_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_gateways_status_body_device_info_item import PostV1GatewaysStatusBodyDeviceInfoItem

        d = src_dict.copy()
        device_info = []
        _device_info = d.pop("deviceInfo", UNSET)
        for device_info_item_data in _device_info or []:
            device_info_item = PostV1GatewaysStatusBodyDeviceInfoItem.from_dict(device_info_item_data)

            device_info.append(device_info_item)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        support_status = d.pop("supportStatus", UNSET)

        post_v1_gateways_status_body = cls(
            device_info=device_info,
            id=id,
            status=status,
            support_status=support_status,
        )

        post_v1_gateways_status_body.additional_properties = d
        return post_v1_gateways_status_body

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
