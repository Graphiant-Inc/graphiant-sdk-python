from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_dns_dns import PutV1DevicesDeviceIdConfigBodyEdgeDnsDns


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeDns")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeDns:
    """
    Attributes:
        dns (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDns]):
    """

    dns: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeDnsDns"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dns: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dns, Unset):
            dns = self.dns.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dns is not UNSET:
            field_dict["dns"] = dns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_dns_dns import PutV1DevicesDeviceIdConfigBodyEdgeDnsDns

        d = src_dict.copy()
        _dns = d.pop("dns", UNSET)
        dns: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDns]
        if isinstance(_dns, Unset):
            dns = UNSET
        else:
            dns = PutV1DevicesDeviceIdConfigBodyEdgeDnsDns.from_dict(_dns)

        put_v1_devices_device_id_config_body_edge_dns = cls(
            dns=dns,
        )

        put_v1_devices_device_id_config_body_edge_dns.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_dns

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
