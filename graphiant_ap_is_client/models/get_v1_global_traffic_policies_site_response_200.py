from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy import (
        GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy,
    )


T = TypeVar("T", bound="GetV1GlobalTrafficPoliciesSiteResponse200")


@_attrs_define
class GetV1GlobalTrafficPoliciesSiteResponse200:
    """
    Attributes:
        traffic_policy (Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy]):
    """

    traffic_policy: Union[Unset, "GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        traffic_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_policy, Unset):
            traffic_policy = self.traffic_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if traffic_policy is not UNSET:
            field_dict["trafficPolicy"] = traffic_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_traffic_policies_site_response_200_traffic_policy import (
            GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy,
        )

        d = src_dict.copy()
        _traffic_policy = d.pop("trafficPolicy", UNSET)
        traffic_policy: Union[Unset, GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy]
        if isinstance(_traffic_policy, Unset):
            traffic_policy = UNSET
        else:
            traffic_policy = GetV1GlobalTrafficPoliciesSiteResponse200TrafficPolicy.from_dict(_traffic_policy)

        get_v1_global_traffic_policies_site_response_200 = cls(
            traffic_policy=traffic_policy,
        )

        get_v1_global_traffic_policies_site_response_200.additional_properties = d
        return get_v1_global_traffic_policies_site_response_200

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
