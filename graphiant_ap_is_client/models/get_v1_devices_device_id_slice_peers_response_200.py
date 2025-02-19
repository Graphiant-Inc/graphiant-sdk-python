from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdSlicePeersResponse200")


@_attrs_define
class GetV1DevicesDeviceIdSlicePeersResponse200:
    """
    Attributes:
        slices (Union[Unset, list['GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem']]):
    """

    slices: Union[Unset, list["GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.slices, Unset):
            slices = []
            for slices_item_data in self.slices:
                slices_item = slices_item_data.to_dict()
                slices.append(slices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slices is not UNSET:
            field_dict["slices"] = slices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem,
        )

        d = src_dict.copy()
        slices = []
        _slices = d.pop("slices", UNSET)
        for slices_item_data in _slices or []:
            slices_item = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem.from_dict(slices_item_data)

            slices.append(slices_item)

        get_v1_devices_device_id_slice_peers_response_200 = cls(
            slices=slices,
        )

        get_v1_devices_device_id_slice_peers_response_200.additional_properties = d
        return get_v1_devices_device_id_slice_peers_response_200

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
