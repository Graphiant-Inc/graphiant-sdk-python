from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_community_item import (
        GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemCommunityItem,
    )
    from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_contributing_src import (
        GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc,
    )
    from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_ext_community_item import (
        GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemExtCommunityItem,
    )
    from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_last_modified import (
        GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItem")


@_attrs_define
class GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItem:
    """
    Attributes:
        as_path (Union[Unset, list[str]]):  Example: ['23212, 45432'].
        community (Union[Unset, list['GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemCommunityItem']]):
        contributing_src (Union[Unset, GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc]):
        egress_interface (Union[Unset, str]):  Example: ATTInterface.
        ext_community (Union[Unset, list['GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemExtCommunityItem']]):
        is_stale (Union[Unset, str]):  Example: true.
        last_modified (Union[Unset, GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified]):
        local_pref (Union[Unset, str]):  Example: 30.
        local_preference (Union[Unset, str]):  Example: 30.
        med (Union[Unset, str]):  Example: 120.
        mpls_label_stack (Union[Unset, list[str]]):  Example: ['[12001 13001]'].
        next_hop (Union[Unset, str]):  Example: 10.1.1.1.
        node_interface (Union[Unset, str]):  Example: Eth0/1.
        node_sid_label (Union[Unset, str]):  Example: 12300.
        node_type (Union[Unset, str]):  Example: local.
        odp_nexthop (Union[Unset, list[str]]):  Example: ['Eth0/1'].
        origin (Union[Unset, str]):  Example: IGP.
        originator_id (Union[Unset, str]):  Example: 12:1456.
        path_status (Union[Unset, str]):  Example: best.
        path_type (Union[Unset, str]):  Example: ebgp, vpn.
        weight (Union[Unset, str]):  Example: 100.
    """

    as_path: Union[Unset, list[str]] = UNSET
    community: Union[Unset, list["GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemCommunityItem"]] = UNSET
    contributing_src: Union[Unset, "GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc"] = UNSET
    egress_interface: Union[Unset, str] = UNSET
    ext_community: Union[Unset, list["GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemExtCommunityItem"]] = (
        UNSET
    )
    is_stale: Union[Unset, str] = UNSET
    last_modified: Union[Unset, "GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified"] = UNSET
    local_pref: Union[Unset, str] = UNSET
    local_preference: Union[Unset, str] = UNSET
    med: Union[Unset, str] = UNSET
    mpls_label_stack: Union[Unset, list[str]] = UNSET
    next_hop: Union[Unset, str] = UNSET
    node_interface: Union[Unset, str] = UNSET
    node_sid_label: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    odp_nexthop: Union[Unset, list[str]] = UNSET
    origin: Union[Unset, str] = UNSET
    originator_id: Union[Unset, str] = UNSET
    path_status: Union[Unset, str] = UNSET
    path_type: Union[Unset, str] = UNSET
    weight: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_path: Union[Unset, list[str]] = UNSET
        if not isinstance(self.as_path, Unset):
            as_path = self.as_path

        community: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.community, Unset):
            community = []
            for community_item_data in self.community:
                community_item = community_item_data.to_dict()
                community.append(community_item)

        contributing_src: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contributing_src, Unset):
            contributing_src = self.contributing_src.to_dict()

        egress_interface = self.egress_interface

        ext_community: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ext_community, Unset):
            ext_community = []
            for ext_community_item_data in self.ext_community:
                ext_community_item = ext_community_item_data.to_dict()
                ext_community.append(ext_community_item)

        is_stale = self.is_stale

        last_modified: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.to_dict()

        local_pref = self.local_pref

        local_preference = self.local_preference

        med = self.med

        mpls_label_stack: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mpls_label_stack, Unset):
            mpls_label_stack = self.mpls_label_stack

        next_hop = self.next_hop

        node_interface = self.node_interface

        node_sid_label = self.node_sid_label

        node_type = self.node_type

        odp_nexthop: Union[Unset, list[str]] = UNSET
        if not isinstance(self.odp_nexthop, Unset):
            odp_nexthop = self.odp_nexthop

        origin = self.origin

        originator_id = self.originator_id

        path_status = self.path_status

        path_type = self.path_type

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_path is not UNSET:
            field_dict["asPath"] = as_path
        if community is not UNSET:
            field_dict["community"] = community
        if contributing_src is not UNSET:
            field_dict["contributingSrc"] = contributing_src
        if egress_interface is not UNSET:
            field_dict["egressInterface"] = egress_interface
        if ext_community is not UNSET:
            field_dict["extCommunity"] = ext_community
        if is_stale is not UNSET:
            field_dict["isStale"] = is_stale
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if local_pref is not UNSET:
            field_dict["localPref"] = local_pref
        if local_preference is not UNSET:
            field_dict["localPreference"] = local_preference
        if med is not UNSET:
            field_dict["med"] = med
        if mpls_label_stack is not UNSET:
            field_dict["mplsLabelStack"] = mpls_label_stack
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if node_interface is not UNSET:
            field_dict["nodeInterface"] = node_interface
        if node_sid_label is not UNSET:
            field_dict["nodeSidLabel"] = node_sid_label
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if odp_nexthop is not UNSET:
            field_dict["odpNexthop"] = odp_nexthop
        if origin is not UNSET:
            field_dict["origin"] = origin
        if originator_id is not UNSET:
            field_dict["originatorId"] = originator_id
        if path_status is not UNSET:
            field_dict["pathStatus"] = path_status
        if path_type is not UNSET:
            field_dict["pathType"] = path_type
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_community_item import (
            GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemCommunityItem,
        )
        from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_contributing_src import (
            GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc,
        )
        from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_ext_community_item import (
            GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemExtCommunityItem,
        )
        from ..models.get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item_last_modified import (
            GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified,
        )

        d = src_dict.copy()
        as_path = cast(list[str], d.pop("asPath", UNSET))

        community = []
        _community = d.pop("community", UNSET)
        for community_item_data in _community or []:
            community_item = GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemCommunityItem.from_dict(
                community_item_data
            )

            community.append(community_item)

        _contributing_src = d.pop("contributingSrc", UNSET)
        contributing_src: Union[Unset, GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc]
        if isinstance(_contributing_src, Unset):
            contributing_src = UNSET
        else:
            contributing_src = GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemContributingSrc.from_dict(
                _contributing_src
            )

        egress_interface = d.pop("egressInterface", UNSET)

        ext_community = []
        _ext_community = d.pop("extCommunity", UNSET)
        for ext_community_item_data in _ext_community or []:
            ext_community_item = GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemExtCommunityItem.from_dict(
                ext_community_item_data
            )

            ext_community.append(ext_community_item)

        is_stale = d.pop("isStale", UNSET)

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = GetV1DeviceRoutingBgpNbrRibResponse200RoutesItemPathItemLastModified.from_dict(
                _last_modified
            )

        local_pref = d.pop("localPref", UNSET)

        local_preference = d.pop("localPreference", UNSET)

        med = d.pop("med", UNSET)

        mpls_label_stack = cast(list[str], d.pop("mplsLabelStack", UNSET))

        next_hop = d.pop("nextHop", UNSET)

        node_interface = d.pop("nodeInterface", UNSET)

        node_sid_label = d.pop("nodeSidLabel", UNSET)

        node_type = d.pop("nodeType", UNSET)

        odp_nexthop = cast(list[str], d.pop("odpNexthop", UNSET))

        origin = d.pop("origin", UNSET)

        originator_id = d.pop("originatorId", UNSET)

        path_status = d.pop("pathStatus", UNSET)

        path_type = d.pop("pathType", UNSET)

        weight = d.pop("weight", UNSET)

        get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item = cls(
            as_path=as_path,
            community=community,
            contributing_src=contributing_src,
            egress_interface=egress_interface,
            ext_community=ext_community,
            is_stale=is_stale,
            last_modified=last_modified,
            local_pref=local_pref,
            local_preference=local_preference,
            med=med,
            mpls_label_stack=mpls_label_stack,
            next_hop=next_hop,
            node_interface=node_interface,
            node_sid_label=node_sid_label,
            node_type=node_type,
            odp_nexthop=odp_nexthop,
            origin=origin,
            originator_id=originator_id,
            path_status=path_status,
            path_type=path_type,
            weight=weight,
        )

        get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item.additional_properties = d
        return get_v1_device_routing_bgp_nbr_rib_response_200_routes_item_path_item

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
