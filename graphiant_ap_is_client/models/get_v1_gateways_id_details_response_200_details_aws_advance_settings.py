from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsAwsAdvanceSettings:
    """
    Attributes:
        address_family (Union[Unset, str]):  Example: TYPE_ENUM.
        allowed_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        amazon_bgp_router_ip (Union[Unset, str]):  Example: TYPE_STRING.
        bgp_auth_key (Union[Unset, str]):  Example: TYPE_STRING.
        customer_bgp_router_ip (Union[Unset, str]):  Example: TYPE_STRING.
        is_jumbo (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    address_family: Union[Unset, str] = UNSET
    allowed_prefixes: Union[Unset, list[str]] = UNSET
    amazon_bgp_router_ip: Union[Unset, str] = UNSET
    bgp_auth_key: Union[Unset, str] = UNSET
    customer_bgp_router_ip: Union[Unset, str] = UNSET
    is_jumbo: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_family = self.address_family

        allowed_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_prefixes, Unset):
            allowed_prefixes = self.allowed_prefixes

        amazon_bgp_router_ip = self.amazon_bgp_router_ip

        bgp_auth_key = self.bgp_auth_key

        customer_bgp_router_ip = self.customer_bgp_router_ip

        is_jumbo = self.is_jumbo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_family is not UNSET:
            field_dict["addressFamily"] = address_family
        if allowed_prefixes is not UNSET:
            field_dict["allowedPrefixes"] = allowed_prefixes
        if amazon_bgp_router_ip is not UNSET:
            field_dict["amazonBgpRouterIp"] = amazon_bgp_router_ip
        if bgp_auth_key is not UNSET:
            field_dict["bgpAuthKey"] = bgp_auth_key
        if customer_bgp_router_ip is not UNSET:
            field_dict["customerBgpRouterIp"] = customer_bgp_router_ip
        if is_jumbo is not UNSET:
            field_dict["isJumbo"] = is_jumbo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_family = d.pop("addressFamily", UNSET)

        allowed_prefixes = cast(list[str], d.pop("allowedPrefixes", UNSET))

        amazon_bgp_router_ip = d.pop("amazonBgpRouterIp", UNSET)

        bgp_auth_key = d.pop("bgpAuthKey", UNSET)

        customer_bgp_router_ip = d.pop("customerBgpRouterIp", UNSET)

        is_jumbo = d.pop("isJumbo", UNSET)

        get_v1_gateways_id_details_response_200_details_aws_advance_settings = cls(
            address_family=address_family,
            allowed_prefixes=allowed_prefixes,
            amazon_bgp_router_ip=amazon_bgp_router_ip,
            bgp_auth_key=bgp_auth_key,
            customer_bgp_router_ip=customer_bgp_router_ip,
            is_jumbo=is_jumbo,
        )

        get_v1_gateways_id_details_response_200_details_aws_advance_settings.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_aws_advance_settings

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
