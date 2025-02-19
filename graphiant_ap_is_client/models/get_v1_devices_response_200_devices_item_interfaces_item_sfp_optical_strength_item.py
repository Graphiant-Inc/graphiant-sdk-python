from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem")


@_attrs_define
class GetV1DevicesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem:
    """
    Attributes:
        index (Union[Unset, str]):  Example: TYPE_UINT32.
        rx_power (Union[Unset, str]):  Example: TYPE_FLOAT.
        tx_bias (Union[Unset, str]):  Example: TYPE_FLOAT.
        tx_power (Union[Unset, str]):  Example: TYPE_FLOAT.
        voltage (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    index: Union[Unset, str] = UNSET
    rx_power: Union[Unset, str] = UNSET
    tx_bias: Union[Unset, str] = UNSET
    tx_power: Union[Unset, str] = UNSET
    voltage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        rx_power = self.rx_power

        tx_bias = self.tx_bias

        tx_power = self.tx_power

        voltage = self.voltage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if rx_power is not UNSET:
            field_dict["rxPower"] = rx_power
        if tx_bias is not UNSET:
            field_dict["txBias"] = tx_bias
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if voltage is not UNSET:
            field_dict["voltage"] = voltage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        index = d.pop("index", UNSET)

        rx_power = d.pop("rxPower", UNSET)

        tx_bias = d.pop("txBias", UNSET)

        tx_power = d.pop("txPower", UNSET)

        voltage = d.pop("voltage", UNSET)

        get_v1_devices_response_200_devices_item_interfaces_item_sfp_optical_strength_item = cls(
            index=index,
            rx_power=rx_power,
            tx_bias=tx_bias,
            tx_power=tx_power,
            voltage=voltage,
        )

        get_v1_devices_response_200_devices_item_interfaces_item_sfp_optical_strength_item.additional_properties = d
        return get_v1_devices_response_200_devices_item_interfaces_item_sfp_optical_strength_item

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
