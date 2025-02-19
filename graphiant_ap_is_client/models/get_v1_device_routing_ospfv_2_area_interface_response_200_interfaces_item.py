from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem")


@_attrs_define
class GetV1DeviceRoutingOspfv2AreaInterfaceResponse200InterfacesItem:
    """
    Attributes:
        bdr_ip_addr (Union[Unset, str]):  Example: 131.34.23.11.
        bdr_router_id (Union[Unset, str]):  Example: 1.1.1.1.
        dr_ip_addr (Union[Unset, str]):  Example: 131.34.23.11.
        dr_router_id (Union[Unset, str]):  Example: 1.1.1.1.
        hello_interval (Union[Unset, str]):  Example: TYPE_STRING.
        hello_timer (Union[Unset, str]):  Example: 50.
        name (Union[Unset, str]):  Example: ethernet1/0.
        neighbors (Union[Unset, list[str]]):  Example: ['1.1.12.12'].
        state (Union[Unset, str]):  Example: Loopback.
        wait_timer (Union[Unset, str]):  Example: 50.
    """

    bdr_ip_addr: Union[Unset, str] = UNSET
    bdr_router_id: Union[Unset, str] = UNSET
    dr_ip_addr: Union[Unset, str] = UNSET
    dr_router_id: Union[Unset, str] = UNSET
    hello_interval: Union[Unset, str] = UNSET
    hello_timer: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    neighbors: Union[Unset, list[str]] = UNSET
    state: Union[Unset, str] = UNSET
    wait_timer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bdr_ip_addr = self.bdr_ip_addr

        bdr_router_id = self.bdr_router_id

        dr_ip_addr = self.dr_ip_addr

        dr_router_id = self.dr_router_id

        hello_interval = self.hello_interval

        hello_timer = self.hello_timer

        name = self.name

        neighbors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.neighbors, Unset):
            neighbors = self.neighbors

        state = self.state

        wait_timer = self.wait_timer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bdr_ip_addr is not UNSET:
            field_dict["bdrIpAddr"] = bdr_ip_addr
        if bdr_router_id is not UNSET:
            field_dict["bdrRouterId"] = bdr_router_id
        if dr_ip_addr is not UNSET:
            field_dict["drIpAddr"] = dr_ip_addr
        if dr_router_id is not UNSET:
            field_dict["drRouterId"] = dr_router_id
        if hello_interval is not UNSET:
            field_dict["helloInterval"] = hello_interval
        if hello_timer is not UNSET:
            field_dict["helloTimer"] = hello_timer
        if name is not UNSET:
            field_dict["name"] = name
        if neighbors is not UNSET:
            field_dict["neighbors"] = neighbors
        if state is not UNSET:
            field_dict["state"] = state
        if wait_timer is not UNSET:
            field_dict["waitTimer"] = wait_timer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bdr_ip_addr = d.pop("bdrIpAddr", UNSET)

        bdr_router_id = d.pop("bdrRouterId", UNSET)

        dr_ip_addr = d.pop("drIpAddr", UNSET)

        dr_router_id = d.pop("drRouterId", UNSET)

        hello_interval = d.pop("helloInterval", UNSET)

        hello_timer = d.pop("helloTimer", UNSET)

        name = d.pop("name", UNSET)

        neighbors = cast(list[str], d.pop("neighbors", UNSET))

        state = d.pop("state", UNSET)

        wait_timer = d.pop("waitTimer", UNSET)

        get_v1_device_routing_ospfv_2_area_interface_response_200_interfaces_item = cls(
            bdr_ip_addr=bdr_ip_addr,
            bdr_router_id=bdr_router_id,
            dr_ip_addr=dr_ip_addr,
            dr_router_id=dr_router_id,
            hello_interval=hello_interval,
            hello_timer=hello_timer,
            name=name,
            neighbors=neighbors,
            state=state,
            wait_timer=wait_timer,
        )

        get_v1_device_routing_ospfv_2_area_interface_response_200_interfaces_item.additional_properties = d
        return get_v1_device_routing_ospfv_2_area_interface_response_200_interfaces_item

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
