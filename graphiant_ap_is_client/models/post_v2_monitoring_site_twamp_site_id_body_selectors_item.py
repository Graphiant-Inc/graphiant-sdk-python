from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringSiteTwampSiteIdBodySelectorsItem")


@_attrs_define
class PostV2MonitoringSiteTwampSiteIdBodySelectorsItem:
    """
    Attributes:
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    circuit_name: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_name = self.circuit_name

        device_id = self.device_id

        interface_name = self.interface_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit_name = d.pop("circuitName", UNSET)

        device_id = d.pop("deviceId", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        type_ = d.pop("type", UNSET)

        post_v2_monitoring_site_twamp_site_id_body_selectors_item = cls(
            circuit_name=circuit_name,
            device_id=device_id,
            interface_name=interface_name,
            type_=type_,
        )

        post_v2_monitoring_site_twamp_site_id_body_selectors_item.additional_properties = d
        return post_v2_monitoring_site_twamp_site_id_body_selectors_item

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
