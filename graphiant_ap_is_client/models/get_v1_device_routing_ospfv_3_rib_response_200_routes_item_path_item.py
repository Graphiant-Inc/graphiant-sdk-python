from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_ospfv_3_rib_response_200_routes_item_path_item_last_modified import (
        GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItem")


@_attrs_define
class GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItem:
    """
    Attributes:
        egress_interface (Union[Unset, str]):  Example: ATTInterface.
        last_modified (Union[Unset, GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified]):
        metric (Union[Unset, str]):  Example: 120.
        next_hop (Union[Unset, str]):  Example: 10.1.1.1.
        tag (Union[Unset, str]):  Example: 12312.
        type_ (Union[Unset, str]):  Example: internal or external.
    """

    egress_interface: Union[Unset, str] = UNSET
    last_modified: Union[Unset, "GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified"] = UNSET
    metric: Union[Unset, str] = UNSET
    next_hop: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        egress_interface = self.egress_interface

        last_modified: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict()

        metric = self.metric

        next_hop = self.next_hop

        tag = self.tag

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if egress_interface is not UNSET:
            field_dict["egressInterface"] = egress_interface
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if metric is not UNSET:
            field_dict["metric"] = metric
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if tag is not UNSET:
            field_dict["tag"] = tag
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_ospfv_3_rib_response_200_routes_item_path_item_last_modified import (
            GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified,
        )

        d = src_dict.copy()
        egress_interface = d.pop("egressInterface", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = GetV1DeviceRoutingOspfv3RibResponse200RoutesItemPathItemLastModified.from_dict(
                _last_modified
            )

        metric = d.pop("metric", UNSET)

        next_hop = d.pop("nextHop", UNSET)

        tag = d.pop("tag", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_device_routing_ospfv_3_rib_response_200_routes_item_path_item = cls(
            egress_interface=egress_interface,
            last_modified=last_modified,
            metric=metric,
            next_hop=next_hop,
            tag=tag,
            type_=type_,
        )

        get_v1_device_routing_ospfv_3_rib_response_200_routes_item_path_item.additional_properties = d
        return get_v1_device_routing_ospfv_3_rib_response_200_routes_item_path_item

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
