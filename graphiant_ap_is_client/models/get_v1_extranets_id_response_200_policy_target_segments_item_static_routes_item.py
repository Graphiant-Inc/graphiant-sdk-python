from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item_next_hop import (
        GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop,
    )
    from ..models.get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item_next_hops_item import (
        GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHopsItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItem")


@_attrs_define
class GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItem:
    """
    Attributes:
        administrative_distance (Union[Unset, str]):  Example: TYPE_UINT32.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        next_hop (Union[Unset, GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop]):
        next_hops (Union[Unset,
            list['GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHopsItem']]):
        prefix (Union[Unset, str]):  Example: TYPE_STRING.
    """

    administrative_distance: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    next_hop: Union[Unset, "GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop"] = UNSET
    next_hops: Union[Unset, list["GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHopsItem"]] = (
        UNSET
    )
    prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        administrative_distance = self.administrative_distance

        description = self.description

        id = self.id

        next_hop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_hop, Unset):
            next_hop = self.next_hop.to_dict()

        next_hops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.next_hops, Unset):
            next_hops = []
            for next_hops_item_data in self.next_hops:
                next_hops_item = next_hops_item_data.to_dict()
                next_hops.append(next_hops_item)

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if administrative_distance is not UNSET:
            field_dict["administrativeDistance"] = administrative_distance
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if next_hop is not UNSET:
            field_dict["nextHop"] = next_hop
        if next_hops is not UNSET:
            field_dict["nextHops"] = next_hops
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item_next_hop import (
            GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop,
        )
        from ..models.get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item_next_hops_item import (
            GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHopsItem,
        )

        d = src_dict.copy()
        administrative_distance = d.pop("administrativeDistance", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _next_hop = d.pop("nextHop", UNSET)
        next_hop: Union[Unset, GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop]
        if isinstance(_next_hop, Unset):
            next_hop = UNSET
        else:
            next_hop = GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHop.from_dict(_next_hop)

        next_hops = []
        _next_hops = d.pop("nextHops", UNSET)
        for next_hops_item_data in _next_hops or []:
            next_hops_item = GetV1ExtranetsIdResponse200PolicyTargetSegmentsItemStaticRoutesItemNextHopsItem.from_dict(
                next_hops_item_data
            )

            next_hops.append(next_hops_item)

        prefix = d.pop("prefix", UNSET)

        get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item = cls(
            administrative_distance=administrative_distance,
            description=description,
            id=id,
            next_hop=next_hop,
            next_hops=next_hops,
            prefix=prefix,
        )

        get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item.additional_properties = d
        return get_v1_extranets_id_response_200_policy_target_segments_item_static_routes_item

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
