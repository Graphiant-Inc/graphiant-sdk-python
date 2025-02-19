from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200DeviceSegmentsItemOverlayFilters")


@_attrs_define
class GetV1DevicesDeviceIdResponse200DeviceSegmentsItemOverlayFilters:
    """
    Attributes:
        inbound_filter (Union[Unset, str]):  Example: TYPE_STRING.
        outbound_filter (Union[Unset, str]):  Example: TYPE_STRING.
    """

    inbound_filter: Union[Unset, str] = UNSET
    outbound_filter: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_filter = self.inbound_filter

        outbound_filter = self.outbound_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_filter is not UNSET:
            field_dict["inboundFilter"] = inbound_filter
        if outbound_filter is not UNSET:
            field_dict["outboundFilter"] = outbound_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        inbound_filter = d.pop("inboundFilter", UNSET)

        outbound_filter = d.pop("outboundFilter", UNSET)

        get_v1_devices_device_id_response_200_device_segments_item_overlay_filters = cls(
            inbound_filter=inbound_filter,
            outbound_filter=outbound_filter,
        )

        get_v1_devices_device_id_response_200_device_segments_item_overlay_filters.additional_properties = d
        return get_v1_devices_device_id_response_200_device_segments_item_overlay_filters

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
