from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2GatewaysIdMonitoringBgpResponse200DataItemSelector")


@_attrs_define
class PostV2GatewaysIdMonitoringBgpResponse200DataItemSelector:
    """
    Attributes:
        peer_address (Union[Unset, str]):  Example: TYPE_STRING.
        tunnel_name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
        vrf (Union[Unset, str]):  Example: TYPE_STRING.
    """

    peer_address: Union[Unset, str] = UNSET
    tunnel_name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peer_address = self.peer_address

        tunnel_name = self.tunnel_name

        type_ = self.type_

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peer_address is not UNSET:
            field_dict["peerAddress"] = peer_address
        if tunnel_name is not UNSET:
            field_dict["tunnelName"] = tunnel_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        peer_address = d.pop("peerAddress", UNSET)

        tunnel_name = d.pop("tunnelName", UNSET)

        type_ = d.pop("type", UNSET)

        vrf = d.pop("vrf", UNSET)

        post_v2_gateways_id_monitoring_bgp_response_200_data_item_selector = cls(
            peer_address=peer_address,
            tunnel_name=tunnel_name,
            type_=type_,
            vrf=vrf,
        )

        post_v2_gateways_id_monitoring_bgp_response_200_data_item_selector.additional_properties = d
        return post_v2_gateways_id_monitoring_bgp_response_200_data_item_selector

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
