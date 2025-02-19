from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_routing_policies_site_response_200_routing_policies_item_statements_item_matches_item_route_tag import (
        GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag,
    )


T = TypeVar("T", bound="GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItem")


@_attrs_define
class GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItem:
    """
    Attributes:
        community (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        id (Union[Unset, str]):  Example: TYPE_INT64.
        prefix_set (Union[Unset, str]):  Example: TYPE_STRING.
        protocol_route_type (Union[Unset, str]):  Example: TYPE_ENUM.
        route_tag (Union[Unset,
            GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag]):
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
        source_interface (Union[Unset, str]):  Example: TYPE_STRING.
        source_protocol (Union[Unset, str]):  Example: TYPE_ENUM.
        stale_purge (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    community: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    prefix_set: Union[Unset, str] = UNSET
    protocol_route_type: Union[Unset, str] = UNSET
    route_tag: Union[
        Unset, "GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag"
    ] = UNSET
    seq: Union[Unset, str] = UNSET
    source_interface: Union[Unset, str] = UNSET
    source_protocol: Union[Unset, str] = UNSET
    stale_purge: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        community: Union[Unset, list[str]] = UNSET
        if not isinstance(self.community, Unset):
            community = self.community

        id = self.id

        prefix_set = self.prefix_set

        protocol_route_type = self.protocol_route_type

        route_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.route_tag, Unset):
            route_tag = self.route_tag.to_dict()

        seq = self.seq

        source_interface = self.source_interface

        source_protocol = self.source_protocol

        stale_purge = self.stale_purge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if community is not UNSET:
            field_dict["community"] = community
        if id is not UNSET:
            field_dict["id"] = id
        if prefix_set is not UNSET:
            field_dict["prefixSet"] = prefix_set
        if protocol_route_type is not UNSET:
            field_dict["protocolRouteType"] = protocol_route_type
        if route_tag is not UNSET:
            field_dict["routeTag"] = route_tag
        if seq is not UNSET:
            field_dict["seq"] = seq
        if source_interface is not UNSET:
            field_dict["sourceInterface"] = source_interface
        if source_protocol is not UNSET:
            field_dict["sourceProtocol"] = source_protocol
        if stale_purge is not UNSET:
            field_dict["stalePurge"] = stale_purge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_routing_policies_site_response_200_routing_policies_item_statements_item_matches_item_route_tag import (
            GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag,
        )

        d = src_dict.copy()
        community = cast(list[str], d.pop("community", UNSET))

        id = d.pop("id", UNSET)

        prefix_set = d.pop("prefixSet", UNSET)

        protocol_route_type = d.pop("protocolRouteType", UNSET)

        _route_tag = d.pop("routeTag", UNSET)
        route_tag: Union[
            Unset, GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag
        ]
        if isinstance(_route_tag, Unset):
            route_tag = UNSET
        else:
            route_tag = (
                GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItemStatementsItemMatchesItemRouteTag.from_dict(
                    _route_tag
                )
            )

        seq = d.pop("seq", UNSET)

        source_interface = d.pop("sourceInterface", UNSET)

        source_protocol = d.pop("sourceProtocol", UNSET)

        stale_purge = d.pop("stalePurge", UNSET)

        get_v1_global_routing_policies_site_response_200_routing_policies_item_statements_item_matches_item = cls(
            community=community,
            id=id,
            prefix_set=prefix_set,
            protocol_route_type=protocol_route_type,
            route_tag=route_tag,
            seq=seq,
            source_interface=source_interface,
            source_protocol=source_protocol,
            stale_purge=stale_purge,
        )

        get_v1_global_routing_policies_site_response_200_routing_policies_item_statements_item_matches_item.additional_properties = d
        return get_v1_global_routing_policies_site_response_200_routing_policies_item_statements_item_matches_item

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
