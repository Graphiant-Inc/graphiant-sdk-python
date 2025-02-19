from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200")


@_attrs_define
class GetV1GatewaysIpsecRegionsRegionIdVrfsVrfIdInsideSubnetResponse200:
    """
    Attributes:
        ipv_4_subnet (Union[Unset, str]):  Example: TYPE_STRING.
        ipv_6_subnet (Union[Unset, str]):  Example: TYPE_STRING.
    """

    ipv_4_subnet: Union[Unset, str] = UNSET
    ipv_6_subnet: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_4_subnet = self.ipv_4_subnet

        ipv_6_subnet = self.ipv_6_subnet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipv_4_subnet is not UNSET:
            field_dict["ipv4Subnet"] = ipv_4_subnet
        if ipv_6_subnet is not UNSET:
            field_dict["ipv6Subnet"] = ipv_6_subnet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ipv_4_subnet = d.pop("ipv4Subnet", UNSET)

        ipv_6_subnet = d.pop("ipv6Subnet", UNSET)

        get_v1_gateways_ipsec_regions_region_id_vrfs_vrf_id_inside_subnet_response_200 = cls(
            ipv_4_subnet=ipv_4_subnet,
            ipv_6_subnet=ipv_6_subnet,
        )

        get_v1_gateways_ipsec_regions_region_id_vrfs_vrf_id_inside_subnet_response_200.additional_properties = d
        return get_v1_gateways_ipsec_regions_region_id_vrfs_vrf_id_inside_subnet_response_200

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
