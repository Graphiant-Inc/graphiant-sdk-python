from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_routing_policies_site_response_200_routing_policies_item import (
        GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItem,
    )


T = TypeVar("T", bound="GetV1GlobalRoutingPoliciesSiteResponse200")


@_attrs_define
class GetV1GlobalRoutingPoliciesSiteResponse200:
    """
    Attributes:
        routing_policies (Union[Unset, list['GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItem']]):
    """

    routing_policies: Union[Unset, list["GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routing_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routing_policies, Unset):
            routing_policies = []
            for routing_policies_item_data in self.routing_policies:
                routing_policies_item = routing_policies_item_data.to_dict()
                routing_policies.append(routing_policies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routing_policies is not UNSET:
            field_dict["routingPolicies"] = routing_policies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_routing_policies_site_response_200_routing_policies_item import (
            GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItem,
        )

        d = src_dict.copy()
        routing_policies = []
        _routing_policies = d.pop("routingPolicies", UNSET)
        for routing_policies_item_data in _routing_policies or []:
            routing_policies_item = GetV1GlobalRoutingPoliciesSiteResponse200RoutingPoliciesItem.from_dict(
                routing_policies_item_data
            )

            routing_policies.append(routing_policies_item)

        get_v1_global_routing_policies_site_response_200 = cls(
            routing_policies=routing_policies,
        )

        get_v1_global_routing_policies_site_response_200.additional_properties = d
        return get_v1_global_routing_policies_site_response_200

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
