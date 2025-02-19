from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem")


@_attrs_define
class GetV1GatewaysSummaryResponse200SummariesItemGatewayDeviceSummaryItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        interface_id (Union[Unset, str]):  Example: TYPE_INT64.
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    device_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    interface_id: Union[Unset, str] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        hostname = self.hostname

        interface_id = self.interface_id

        maintenance_mode = self.maintenance_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        hostname = d.pop("hostname", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        get_v1_gateways_summary_response_200_summaries_item_gateway_device_summary_item = cls(
            device_id=device_id,
            hostname=hostname,
            interface_id=interface_id,
            maintenance_mode=maintenance_mode,
        )

        get_v1_gateways_summary_response_200_summaries_item_gateway_device_summary_item.additional_properties = d
        return get_v1_gateways_summary_response_200_summaries_item_gateway_device_summary_item

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
