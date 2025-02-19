from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_routing_policies_device_response_200_routing_policies_item_statements_item_actions_item_community import (
        GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity,
    )


T = TypeVar("T", bound="GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItem")


@_attrs_define
class GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItem:
    """
    Attributes:
        administrative_distance (Union[Unset, str]):  Example: TYPE_UINT32.
        aspath_prepend (Union[Unset, str]):  Example: TYPE_UINT32.
        bgp_set_next_hop (Union[Unset, str]):  Example: TYPE_STRING.
        call_policy (Union[Unset, str]):  Example: TYPE_STRING.
        community (Union[Unset,
            GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        local_pref (Union[Unset, str]):  Example: TYPE_UINT32.
        metric_absolute (Union[Unset, str]):  Example: TYPE_UINT32.
        metric_modifier (Union[Unset, str]):  Example: TYPE_INT32.
        result (Union[Unset, str]):  Example: TYPE_ENUM.
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
        weight (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    administrative_distance: Union[Unset, str] = UNSET
    aspath_prepend: Union[Unset, str] = UNSET
    bgp_set_next_hop: Union[Unset, str] = UNSET
    call_policy: Union[Unset, str] = UNSET
    community: Union[
        Unset, "GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity"
    ] = UNSET
    id: Union[Unset, str] = UNSET
    local_pref: Union[Unset, str] = UNSET
    metric_absolute: Union[Unset, str] = UNSET
    metric_modifier: Union[Unset, str] = UNSET
    result: Union[Unset, str] = UNSET
    seq: Union[Unset, str] = UNSET
    weight: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administrative_distance = self.administrative_distance

        aspath_prepend = self.aspath_prepend

        bgp_set_next_hop = self.bgp_set_next_hop

        call_policy = self.call_policy

        community: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.community, Unset):
            community = self.community.to_dict()

        id = self.id

        local_pref = self.local_pref

        metric_absolute = self.metric_absolute

        metric_modifier = self.metric_modifier

        result = self.result

        seq = self.seq

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if administrative_distance is not UNSET:
            field_dict["administrativeDistance"] = administrative_distance
        if aspath_prepend is not UNSET:
            field_dict["aspathPrepend"] = aspath_prepend
        if bgp_set_next_hop is not UNSET:
            field_dict["bgpSetNextHop"] = bgp_set_next_hop
        if call_policy is not UNSET:
            field_dict["callPolicy"] = call_policy
        if community is not UNSET:
            field_dict["community"] = community
        if id is not UNSET:
            field_dict["id"] = id
        if local_pref is not UNSET:
            field_dict["localPref"] = local_pref
        if metric_absolute is not UNSET:
            field_dict["metricAbsolute"] = metric_absolute
        if metric_modifier is not UNSET:
            field_dict["metricModifier"] = metric_modifier
        if result is not UNSET:
            field_dict["result"] = result
        if seq is not UNSET:
            field_dict["seq"] = seq
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_routing_policies_device_response_200_routing_policies_item_statements_item_actions_item_community import (
            GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity,
        )

        d = src_dict.copy()
        administrative_distance = d.pop("administrativeDistance", UNSET)

        aspath_prepend = d.pop("aspathPrepend", UNSET)

        bgp_set_next_hop = d.pop("bgpSetNextHop", UNSET)

        call_policy = d.pop("callPolicy", UNSET)

        _community = d.pop("community", UNSET)
        community: Union[
            Unset, GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity
        ]
        if isinstance(_community, Unset):
            community = UNSET
        else:
            community = GetV1GlobalRoutingPoliciesDeviceResponse200RoutingPoliciesItemStatementsItemActionsItemCommunity.from_dict(
                _community
            )

        id = d.pop("id", UNSET)

        local_pref = d.pop("localPref", UNSET)

        metric_absolute = d.pop("metricAbsolute", UNSET)

        metric_modifier = d.pop("metricModifier", UNSET)

        result = d.pop("result", UNSET)

        seq = d.pop("seq", UNSET)

        weight = d.pop("weight", UNSET)

        get_v1_global_routing_policies_device_response_200_routing_policies_item_statements_item_actions_item = cls(
            administrative_distance=administrative_distance,
            aspath_prepend=aspath_prepend,
            bgp_set_next_hop=bgp_set_next_hop,
            call_policy=call_policy,
            community=community,
            id=id,
            local_pref=local_pref,
            metric_absolute=metric_absolute,
            metric_modifier=metric_modifier,
            result=result,
            seq=seq,
            weight=weight,
        )

        get_v1_global_routing_policies_device_response_200_routing_policies_item_statements_item_actions_item.additional_properties = d
        return get_v1_global_routing_policies_device_response_200_routing_policies_item_statements_item_actions_item

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
