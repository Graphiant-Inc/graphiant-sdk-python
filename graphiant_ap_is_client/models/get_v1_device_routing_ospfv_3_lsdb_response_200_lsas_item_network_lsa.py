from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3LsdbResponse200LsasItemNetworkLsa")


@_attrs_define
class GetV1DeviceRoutingOspfv3LsdbResponse200LsasItemNetworkLsa:
    """
    Attributes:
        attached_routers (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        network_mask (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    attached_routers: Union[Unset, list[str]] = UNSET
    network_mask: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attached_routers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.attached_routers, Unset):
            attached_routers = self.attached_routers

        network_mask = self.network_mask

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attached_routers is not UNSET:
            field_dict["attachedRouters"] = attached_routers
        if network_mask is not UNSET:
            field_dict["networkMask"] = network_mask

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        attached_routers = cast(list[str], d.pop("attachedRouters", UNSET))

        network_mask = d.pop("networkMask", UNSET)

        get_v1_device_routing_ospfv_3_lsdb_response_200_lsas_item_network_lsa = cls(
            attached_routers=attached_routers,
            network_mask=network_mask,
        )

        get_v1_device_routing_ospfv_3_lsdb_response_200_lsas_item_network_lsa.additional_properties = d
        return get_v1_device_routing_ospfv_3_lsdb_response_200_lsas_item_network_lsa

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
