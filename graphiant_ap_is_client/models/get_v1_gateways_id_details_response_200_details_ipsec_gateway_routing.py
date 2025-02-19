from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing_bgp import (
        GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp,
    )
    from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing_static import (
        GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic,
    )


T = TypeVar("T", bound="GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRouting")


@_attrs_define
class GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRouting:
    """
    Attributes:
        bgp (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp]):
        static (Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic]):
    """

    bgp: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp"] = UNSET
    static: Union[Unset, "GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp, Unset):
            bgp = self.bgp.to_dict()

        static: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static, Unset):
            static = self.static.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp is not UNSET:
            field_dict["bgp"] = bgp
        if static is not UNSET:
            field_dict["static"] = static

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing_bgp import (
            GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp,
        )
        from ..models.get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing_static import (
            GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic,
        )

        d = src_dict.copy()
        _bgp = d.pop("bgp", UNSET)
        bgp: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp]
        if isinstance(_bgp, Unset):
            bgp = UNSET
        else:
            bgp = GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingBgp.from_dict(_bgp)

        _static = d.pop("static", UNSET)
        static: Union[Unset, GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic]
        if isinstance(_static, Unset):
            static = UNSET
        else:
            static = GetV1GatewaysIdDetailsResponse200DetailsIpsecGatewayRoutingStatic.from_dict(_static)

        get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing = cls(
            bgp=bgp,
            static=static,
        )

        get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing.additional_properties = d
        return get_v1_gateways_id_details_response_200_details_ipsec_gateway_routing

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
