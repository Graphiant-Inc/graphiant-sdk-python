from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdCandidateCircuitsResponse200CircuitsItem")


@_attrs_define
class GetV1DevicesDeviceIdCandidateCircuitsResponse200CircuitsItem:
    """
    Attributes:
        circuit (Union[Unset, str]):  Example: TYPE_STRING.
        interface (Union[Unset, str]):  Example: TYPE_STRING.
        vrf (Union[Unset, str]):  Example: TYPE_STRING.
    """

    circuit: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit = self.circuit

        interface = self.interface

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
        if interface is not UNSET:
            field_dict["interface"] = interface
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit = d.pop("circuit", UNSET)

        interface = d.pop("interface", UNSET)

        vrf = d.pop("vrf", UNSET)

        get_v1_devices_device_id_candidate_circuits_response_200_circuits_item = cls(
            circuit=circuit,
            interface=interface,
            vrf=vrf,
        )

        get_v1_devices_device_id_candidate_circuits_response_200_circuits_item.additional_properties = d
        return get_v1_devices_device_id_candidate_circuits_response_200_circuits_item

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
