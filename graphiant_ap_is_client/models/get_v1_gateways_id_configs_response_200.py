from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_gateways_id_configs_response_200_ipsec_tunnel_config_item import (
        GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem,
    )


T = TypeVar("T", bound="GetV1GatewaysIdConfigsResponse200")


@_attrs_define
class GetV1GatewaysIdConfigsResponse200:
    """
    Attributes:
        ipsec_tunnel_config (Union[Unset, list['GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem']]):
    """

    ipsec_tunnel_config: Union[Unset, list["GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipsec_tunnel_config: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipsec_tunnel_config, Unset):
            ipsec_tunnel_config = []
            for ipsec_tunnel_config_item_data in self.ipsec_tunnel_config:
                ipsec_tunnel_config_item = ipsec_tunnel_config_item_data.to_dict()
                ipsec_tunnel_config.append(ipsec_tunnel_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipsec_tunnel_config is not UNSET:
            field_dict["ipsecTunnelConfig"] = ipsec_tunnel_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_gateways_id_configs_response_200_ipsec_tunnel_config_item import (
            GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem,
        )

        d = src_dict.copy()
        ipsec_tunnel_config = []
        _ipsec_tunnel_config = d.pop("ipsecTunnelConfig", UNSET)
        for ipsec_tunnel_config_item_data in _ipsec_tunnel_config or []:
            ipsec_tunnel_config_item = GetV1GatewaysIdConfigsResponse200IpsecTunnelConfigItem.from_dict(
                ipsec_tunnel_config_item_data
            )

            ipsec_tunnel_config.append(ipsec_tunnel_config_item)

        get_v1_gateways_id_configs_response_200 = cls(
            ipsec_tunnel_config=ipsec_tunnel_config,
        )

        get_v1_gateways_id_configs_response_200.additional_properties = d
        return get_v1_gateways_id_configs_response_200

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
