from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DiagnosticBgpResetDeviceIdBody")


@_attrs_define
class PutV1DiagnosticBgpResetDeviceIdBody:
    """
    Attributes:
        hard (Union[Unset, str]):  Example: true.
        lan_segment (Union[Unset, str]):  Example: isp.
        local_interface (Union[Unset, str]):  Example: GigabitEthernet0/0/1.
        neighbor (Union[Unset, str]):  Example: 1.1.1.1.
    """

    hard: Union[Unset, str] = UNSET
    lan_segment: Union[Unset, str] = UNSET
    local_interface: Union[Unset, str] = UNSET
    neighbor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hard = self.hard

        lan_segment = self.lan_segment

        local_interface = self.local_interface

        neighbor = self.neighbor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hard is not UNSET:
            field_dict["hard"] = hard
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if local_interface is not UNSET:
            field_dict["localInterface"] = local_interface
        if neighbor is not UNSET:
            field_dict["neighbor"] = neighbor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hard = d.pop("hard", UNSET)

        lan_segment = d.pop("lanSegment", UNSET)

        local_interface = d.pop("localInterface", UNSET)

        neighbor = d.pop("neighbor", UNSET)

        put_v1_diagnostic_bgp_reset_device_id_body = cls(
            hard=hard,
            lan_segment=lan_segment,
            local_interface=local_interface,
            neighbor=neighbor,
        )

        put_v1_diagnostic_bgp_reset_device_id_body.additional_properties = d
        return put_v1_diagnostic_bgp_reset_device_id_body

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
