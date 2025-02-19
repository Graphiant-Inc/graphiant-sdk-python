from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_ipsec_profile_vpn_profile_id_site_to_site_response_200_site_to_site_vpn_item import (
        GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200SiteToSiteVpnItem,
    )


T = TypeVar("T", bound="GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200")


@_attrs_define
class GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200:
    """
    Attributes:
        site_to_site_vpn (Union[Unset,
            list['GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200SiteToSiteVpnItem']]):
    """

    site_to_site_vpn: Union[
        Unset, list["GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200SiteToSiteVpnItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_to_site_vpn: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_to_site_vpn, Unset):
            site_to_site_vpn = []
            for site_to_site_vpn_item_data in self.site_to_site_vpn:
                site_to_site_vpn_item = site_to_site_vpn_item_data.to_dict()
                site_to_site_vpn.append(site_to_site_vpn_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_to_site_vpn is not UNSET:
            field_dict["siteToSiteVpn"] = site_to_site_vpn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_ipsec_profile_vpn_profile_id_site_to_site_response_200_site_to_site_vpn_item import (
            GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200SiteToSiteVpnItem,
        )

        d = src_dict.copy()
        site_to_site_vpn = []
        _site_to_site_vpn = d.pop("siteToSiteVpn", UNSET)
        for site_to_site_vpn_item_data in _site_to_site_vpn or []:
            site_to_site_vpn_item = GetV1GlobalIpsecProfileVpnProfileIdSiteToSiteResponse200SiteToSiteVpnItem.from_dict(
                site_to_site_vpn_item_data
            )

            site_to_site_vpn.append(site_to_site_vpn_item)

        get_v1_global_ipsec_profile_vpn_profile_id_site_to_site_response_200 = cls(
            site_to_site_vpn=site_to_site_vpn,
        )

        get_v1_global_ipsec_profile_vpn_profile_id_site_to_site_response_200.additional_properties = d
        return get_v1_global_ipsec_profile_vpn_profile_id_site_to_site_response_200

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
