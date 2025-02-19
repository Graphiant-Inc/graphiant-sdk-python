from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_3_area_nbr_response_200_nbrs_item_last_state_change import (
        GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItem")


@_attrs_define
class GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItem:
    """
    Attributes:
        address (Union[Unset, str]):  Example: 1.1.1.1.
        cost (Union[Unset, str]):  Example: 230.
        dead_timer (Union[Unset, str]):  Example: 40.
        last_state_change (Union[Unset, GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange]):
        router_id (Union[Unset, str]):  Example: 1.1.1.1.
        state (Union[Unset, str]):  Example: up or down.
    """

    address: Union[Unset, str] = UNSET
    cost: Union[Unset, str] = UNSET
    dead_timer: Union[Unset, str] = UNSET
    last_state_change: Union[Unset, "GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange"] = UNSET
    router_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        cost = self.cost

        dead_timer = self.dead_timer

        last_state_change: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_state_change, Unset):
            last_state_change = self.last_state_change.to_dict()

        router_id = self.router_id

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if cost is not UNSET:
            field_dict["cost"] = cost
        if dead_timer is not UNSET:
            field_dict["deadTimer"] = dead_timer
        if last_state_change is not UNSET:
            field_dict["lastStateChange"] = last_state_change
        if router_id is not UNSET:
            field_dict["routerId"] = router_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_3_area_nbr_response_200_nbrs_item_last_state_change import (
            GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        cost = d.pop("cost", UNSET)

        dead_timer = d.pop("deadTimer", UNSET)

        _last_state_change = d.pop("lastStateChange", UNSET)
        last_state_change: Union[Unset, GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange]
        if isinstance(_last_state_change, Unset):
            last_state_change = UNSET
        else:
            last_state_change = GetV1DeviceRoutingOspfv3AreaNbrResponse200NbrsItemLastStateChange.from_dict(
                _last_state_change
            )

        router_id = d.pop("routerId", UNSET)

        state = d.pop("state", UNSET)

        get_v1_device_routing_ospfv_3_area_nbr_response_200_nbrs_item = cls(
            address=address,
            cost=cost,
            dead_timer=dead_timer,
            last_state_change=last_state_change,
            router_id=router_id,
            state=state,
        )

        get_v1_device_routing_ospfv_3_area_nbr_response_200_nbrs_item.additional_properties = d
        return get_v1_device_routing_ospfv_3_area_nbr_response_200_nbrs_item

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
