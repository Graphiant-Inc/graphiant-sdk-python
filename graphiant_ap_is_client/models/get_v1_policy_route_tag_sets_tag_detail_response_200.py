from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item import (
        GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem,
    )


T = TypeVar("T", bound="GetV1PolicyRouteTagSetsTagDetailResponse200")


@_attrs_define
class GetV1PolicyRouteTagSetsTagDetailResponse200:
    """
    Attributes:
        devices (Union[Unset, list['GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem']]):
    """

    devices: Union[Unset, list["GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item import (
            GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        get_v1_policy_route_tag_sets_tag_detail_response_200 = cls(
            devices=devices,
        )

        get_v1_policy_route_tag_sets_tag_detail_response_200.additional_properties = d
        return get_v1_policy_route_tag_sets_tag_detail_response_200

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
