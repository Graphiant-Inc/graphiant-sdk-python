from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItem,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_page_info import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo,
    )


T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200:
    """
    Attributes:
        devices (Union[Unset, list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItem']]):
        page_info (Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo]):
    """

    devices: Union[Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItem"]] = UNSET
    page_info: Union[Unset, "GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItem,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_page_info import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1EnterpriseEnterpriseIdDevicesResponse200PageInfo.from_dict(_page_info)

        get_v1_enterprise_enterprise_id_devices_response_200 = cls(
            devices=devices,
            page_info=page_info,
        )

        get_v1_enterprise_enterprise_id_devices_response_200.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200

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
