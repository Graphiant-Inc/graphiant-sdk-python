from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_rib_response_200_routes_item_last_modified import (
        GetV1DeviceRoutingRibResponse200RoutesItemLastModified,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingRibResponse200RoutesItem")


@_attrs_define
class GetV1DeviceRoutingRibResponse200RoutesItem:
    """
    Attributes:
        admin_distance (Union[Unset, str]):  Example: 20 for eBGP.
        egress_interface (Union[Unset, str]):  Example: ethernet1/0.
        ip_prefix (Union[Unset, str]):  Example: 1001:1::/32.
        ip_version (Union[Unset, str]):  Example: 4 or 6.
        last_modified (Union[Unset, GetV1DeviceRoutingRibResponse200RoutesItemLastModified]):
        metric (Union[Unset, str]):  Example: 100.
        next_hop (Union[Unset, str]):  Example: 1001:1:3:1231.
        preference (Union[Unset, str]):  Example: 120.
        source_protocol (Union[Unset, str]):  Example: BGP.
        status (Union[Unset, str]):  Example: true.
        type_ (Union[Unset, str]):  Example: odp or core or vpn etc.
        vrf (Union[Unset, str]):  Example: management.
    """

    admin_distance: Union[Unset, str] = UNSET
    egress_interface: Union[Unset, str] = UNSET
    ip_prefix: Union[Unset, str] = UNSET
    ip_version: Union[Unset, str] = UNSET
    last_modified: Union[Unset, "GetV1DeviceRoutingRibResponse200RoutesItemLastModified"] = UNSET
    metric: Union[Unset, str] = UNSET
    next_hop: Union[Unset, str] = UNSET
    preference: Union[Unset, str] = UNSET
    source_protocol: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    vrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_distance = self.admin_distance

        egress_interface = self.egress_interface

        ip_prefix = self.ip_prefix

        ip_version = self.ip_version

        last_modified: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict()

        metric = self.metric

        next_hop = self.next_hop

        preference = self.preference

        source_protocol = self.source_protocol

        status = self.status

        type_ = self.type_

        vrf = self.vrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_distance is not UNSET:
            field_dict["adminDistance"] = admin_distance
        if egress_interface is not UNSET:
            field_dict["egressInterface"] = egress_interface
        if ip_prefix is not UNSET:
            field_dict["ipPrefix"] = ip_prefix
        if ip_version is not UNSET:
            field_dict["ipVersion"] = ip_version
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if metric is not UNSET:
            field_dict["metric"] = metric
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if preference is not UNSET:
            field_dict["preference"] = preference
        if source_protocol is not UNSET:
            field_dict["sourceProtocol"] = source_protocol
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vrf is not UNSET:
            field_dict["vrf"] = vrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_rib_response_200_routes_item_last_modified import (
            GetV1DeviceRoutingRibResponse200RoutesItemLastModified,
        )

        d = src_dict.copy()
        admin_distance = d.pop("adminDistance", UNSET)

        egress_interface = d.pop("egressInterface", UNSET)

        ip_prefix = d.pop("ipPrefix", UNSET)

        ip_version = d.pop("ipVersion", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, GetV1DeviceRoutingRibResponse200RoutesItemLastModified]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = GetV1DeviceRoutingRibResponse200RoutesItemLastModified.from_dict(_last_modified)

        metric = d.pop("metric", UNSET)

        next_hop = d.pop("nextHop", UNSET)

        preference = d.pop("preference", UNSET)

        source_protocol = d.pop("sourceProtocol", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        vrf = d.pop("vrf", UNSET)

        get_v1_device_routing_rib_response_200_routes_item = cls(
            admin_distance=admin_distance,
            egress_interface=egress_interface,
            ip_prefix=ip_prefix,
            ip_version=ip_version,
            last_modified=last_modified,
            metric=metric,
            next_hop=next_hop,
            preference=preference,
            source_protocol=source_protocol,
            status=status,
            type_=type_,
            vrf=vrf,
        )

        get_v1_device_routing_rib_response_200_routes_item.additional_properties = d
        return get_v1_device_routing_rib_response_200_routes_item

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
