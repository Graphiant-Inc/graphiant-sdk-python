from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item_value_site_to_site_vpn import (
        PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValue:
    """
    Attributes:
        site_to_site_vpn (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn]):
    """

    site_to_site_vpn: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_to_site_vpn: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_to_site_vpn, Unset):
            site_to_site_vpn = self.site_to_site_vpn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_to_site_vpn is not UNSET:
            field_dict["siteToSiteVpn"] = site_to_site_vpn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item_value_site_to_site_vpn import (
            PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn,
        )

        d = src_dict.copy()
        _site_to_site_vpn = d.pop("siteToSiteVpn", UNSET)
        site_to_site_vpn: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn]
        if isinstance(_site_to_site_vpn, Unset):
            site_to_site_vpn = UNSET
        else:
            site_to_site_vpn = PutV1DevicesDeviceIdConfigBodyEdgeSiteToSiteVpnItemValueSiteToSiteVpn.from_dict(
                _site_to_site_vpn
            )

        put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item_value = cls(
            site_to_site_vpn=site_to_site_vpn,
        )

        put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_site_to_site_vpn_item_value

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
