from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemStaticRoutesItemNextHop")


@_attrs_define
class GetV1DevicesDeviceIdCircuitsResponse200CircuitsItemStaticRoutesItemNextHop:
    """
    Attributes:
        circuit (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        metric (Union[Unset, str]):  Example: TYPE_UINT32.
        next_hop_address (Union[Unset, str]):  Example: TYPE_STRING.
        nexthop (Union[Unset, str]):  Example: TYPE_STRING.
        outgoing_interface (Union[Unset, str]):  Example: TYPE_STRING.
        third_party_ipsec_tunnel (Union[Unset, str]):  Example: TYPE_STRING.
    """

    circuit: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    metric: Union[Unset, str] = UNSET
    next_hop_address: Union[Unset, str] = UNSET
    nexthop: Union[Unset, str] = UNSET
    outgoing_interface: Union[Unset, str] = UNSET
    third_party_ipsec_tunnel: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit = self.circuit

        id = self.id

        metric = self.metric

        next_hop_address = self.next_hop_address

        nexthop = self.nexthop

        outgoing_interface = self.outgoing_interface

        third_party_ipsec_tunnel = self.third_party_ipsec_tunnel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
        if id is not UNSET:
            field_dict["id"] = id
        if metric is not UNSET:
            field_dict["metric"] = metric
        if next_hop_address is not UNSET:
            field_dict["nextHopAddress"] = next_hop_address
        if nexthop is not UNSET:
            field_dict["nexthop"] = nexthop
        if outgoing_interface is not UNSET:
            field_dict["outgoingInterface"] = outgoing_interface
        if third_party_ipsec_tunnel is not UNSET:
            field_dict["thirdPartyIpsecTunnel"] = third_party_ipsec_tunnel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        circuit = d.pop("circuit", UNSET)

        id = d.pop("id", UNSET)

        metric = d.pop("metric", UNSET)

        next_hop_address = d.pop("nextHopAddress", UNSET)

        nexthop = d.pop("nexthop", UNSET)

        outgoing_interface = d.pop("outgoingInterface", UNSET)

        third_party_ipsec_tunnel = d.pop("thirdPartyIpsecTunnel", UNSET)

        get_v1_devices_device_id_circuits_response_200_circuits_item_static_routes_item_next_hop = cls(
            circuit=circuit,
            id=id,
            metric=metric,
            next_hop_address=next_hop_address,
            nexthop=nexthop,
            outgoing_interface=outgoing_interface,
            third_party_ipsec_tunnel=third_party_ipsec_tunnel,
        )

        get_v1_devices_device_id_circuits_response_200_circuits_item_static_routes_item_next_hop.additional_properties = d
        return get_v1_devices_device_id_circuits_response_200_circuits_item_static_routes_item_next_hop

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
