from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_ebgp_route_count import (
        GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount,
    )
    from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_graphiant_route_count import (
        GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount,
    )
    from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_ibgp_route_count import (
        GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount,
    )
    from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_local_sourced_route_count import (
        GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount,
    )
    from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_total_route_count import (
        GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount,
    )


T = TypeVar("T", bound="GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200")


@_attrs_define
class GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200:
    """
    Attributes:
        ebgp_route_count (Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount]):
        graphiant_route_count (Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount]):
        ibgp_route_count (Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount]):
        local_sourced_route_count (Union[Unset,
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount]):
        total_route_count (Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount]):
    """

    ebgp_route_count: Union[Unset, "GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount"] = UNSET
    graphiant_route_count: Union[Unset, "GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount"] = UNSET
    ibgp_route_count: Union[Unset, "GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount"] = UNSET
    local_sourced_route_count: Union[
        Unset, "GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount"
    ] = UNSET
    total_route_count: Union[Unset, "GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ebgp_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ebgp_route_count, Unset):
            ebgp_route_count = self.ebgp_route_count.to_dict()

        graphiant_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.graphiant_route_count, Unset):
            graphiant_route_count = self.graphiant_route_count.to_dict()

        ibgp_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ibgp_route_count, Unset):
            ibgp_route_count = self.ibgp_route_count.to_dict()

        local_sourced_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.local_sourced_route_count, Unset):
            local_sourced_route_count = self.local_sourced_route_count.to_dict()

        total_route_count: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.total_route_count, Unset):
            total_route_count = self.total_route_count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ebgp_route_count is not UNSET:
            field_dict["ebgpRouteCount"] = ebgp_route_count
        if graphiant_route_count is not UNSET:
            field_dict["graphiantRouteCount"] = graphiant_route_count
        if ibgp_route_count is not UNSET:
            field_dict["ibgpRouteCount"] = ibgp_route_count
        if local_sourced_route_count is not UNSET:
            field_dict["localSourcedRouteCount"] = local_sourced_route_count
        if total_route_count is not UNSET:
            field_dict["totalRouteCount"] = total_route_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_ebgp_route_count import (
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount,
        )
        from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_graphiant_route_count import (
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount,
        )
        from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_ibgp_route_count import (
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount,
        )
        from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_local_sourced_route_count import (
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount,
        )
        from ..models.get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200_total_route_count import (
            GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount,
        )

        d = src_dict.copy()
        _ebgp_route_count = d.pop("ebgpRouteCount", UNSET)
        ebgp_route_count: Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount]
        if isinstance(_ebgp_route_count, Unset):
            ebgp_route_count = UNSET
        else:
            ebgp_route_count = GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200EbgpRouteCount.from_dict(
                _ebgp_route_count
            )

        _graphiant_route_count = d.pop("graphiantRouteCount", UNSET)
        graphiant_route_count: Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount]
        if isinstance(_graphiant_route_count, Unset):
            graphiant_route_count = UNSET
        else:
            graphiant_route_count = GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200GraphiantRouteCount.from_dict(
                _graphiant_route_count
            )

        _ibgp_route_count = d.pop("ibgpRouteCount", UNSET)
        ibgp_route_count: Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount]
        if isinstance(_ibgp_route_count, Unset):
            ibgp_route_count = UNSET
        else:
            ibgp_route_count = GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200IbgpRouteCount.from_dict(
                _ibgp_route_count
            )

        _local_sourced_route_count = d.pop("localSourcedRouteCount", UNSET)
        local_sourced_route_count: Union[
            Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount
        ]
        if isinstance(_local_sourced_route_count, Unset):
            local_sourced_route_count = UNSET
        else:
            local_sourced_route_count = (
                GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200LocalSourcedRouteCount.from_dict(
                    _local_sourced_route_count
                )
            )

        _total_route_count = d.pop("totalRouteCount", UNSET)
        total_route_count: Union[Unset, GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount]
        if isinstance(_total_route_count, Unset):
            total_route_count = UNSET
        else:
            total_route_count = GetV1DeviceRoutingVrfBgpEibgpRouteCountResponse200TotalRouteCount.from_dict(
                _total_route_count
            )

        get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200 = cls(
            ebgp_route_count=ebgp_route_count,
            graphiant_route_count=graphiant_route_count,
            ibgp_route_count=ibgp_route_count,
            local_sourced_route_count=local_sourced_route_count,
            total_route_count=total_route_count,
        )

        get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200.additional_properties = d
        return get_v1_device_routing_vrf_bgp_eibgp_route_count_response_200

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
