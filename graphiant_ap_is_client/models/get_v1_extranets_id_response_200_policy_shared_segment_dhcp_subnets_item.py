from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_leases_item import (
        GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemLeasesItem,
    )
    from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_nameservers import (
        GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers,
    )
    from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_ranges_item import (
        GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemRangesItem,
    )
    from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_static_leases_item import (
        GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemStaticLeasesItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItem")


@_attrs_define
class GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItem:
    """
    Attributes:
        default_lease_time_secs (Union[Unset, str]):  Example: TYPE_UINT32.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        domain_name (Union[Unset, str]):  Example: TYPE_STRING.
        gateway (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interface (Union[Unset, str]):  Example: TYPE_STRING.
        ip_prefix (Union[Unset, str]):  Example: TYPE_STRING.
        ip_version (Union[Unset, str]):  Example: TYPE_UINT32.
        leases (Union[Unset, list['GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemLeasesItem']]):
        max_lease_time_secs (Union[Unset, str]):  Example: TYPE_UINT32.
        min_lease_time_secs (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        nameservers (Union[Unset, GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers]):
        ranges (Union[Unset, list['GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemRangesItem']]):
        static_leases (Union[Unset,
            list['GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemStaticLeasesItem']]):
        total_addresses (Union[Unset, str]):  Example: TYPE_UINT64.
        utilization (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    default_lease_time_secs: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    domain_name: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interface: Union[Unset, str] = UNSET
    ip_prefix: Union[Unset, str] = UNSET
    ip_version: Union[Unset, str] = UNSET
    leases: Union[Unset, list["GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemLeasesItem"]] = UNSET
    max_lease_time_secs: Union[Unset, str] = UNSET
    min_lease_time_secs: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    nameservers: Union[Unset, "GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers"] = UNSET
    ranges: Union[Unset, list["GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemRangesItem"]] = UNSET
    static_leases: Union[
        Unset, list["GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemStaticLeasesItem"]
    ] = UNSET
    total_addresses: Union[Unset, str] = UNSET
    utilization: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_lease_time_secs = self.default_lease_time_secs

        description = self.description

        domain_name = self.domain_name

        gateway = self.gateway

        id = self.id

        interface = self.interface

        ip_prefix = self.ip_prefix

        ip_version = self.ip_version

        leases: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.leases, Unset):
            leases = []
            for leases_item_data in self.leases:
                leases_item = leases_item_data.to_dict()
                leases.append(leases_item)

        max_lease_time_secs = self.max_lease_time_secs

        min_lease_time_secs = self.min_lease_time_secs

        name = self.name

        nameservers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nameservers, Unset):
            nameservers = self.nameservers.to_dict()

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        static_leases: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_leases, Unset):
            static_leases = []
            for static_leases_item_data in self.static_leases:
                static_leases_item = static_leases_item_data.to_dict()
                static_leases.append(static_leases_item)

        total_addresses = self.total_addresses

        utilization = self.utilization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_lease_time_secs is not UNSET:
            field_dict["defaultLeaseTimeSecs"] = default_lease_time_secs
        if description is not UNSET:
            field_dict["description"] = description
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if id is not UNSET:
            field_dict["id"] = id
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ip_prefix is not UNSET:
            field_dict["ipPrefix"] = ip_prefix
        if ip_version is not UNSET:
            field_dict["ipVersion"] = ip_version
        if leases is not UNSET:
            field_dict["leases"] = leases
        if max_lease_time_secs is not UNSET:
            field_dict["maxLeaseTimeSecs"] = max_lease_time_secs
        if min_lease_time_secs is not UNSET:
            field_dict["minLeaseTimeSecs"] = min_lease_time_secs
        if name is not UNSET:
            field_dict["name"] = name
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if static_leases is not UNSET:
            field_dict["staticLeases"] = static_leases
        if total_addresses is not UNSET:
            field_dict["totalAddresses"] = total_addresses
        if utilization is not UNSET:
            field_dict["utilization"] = utilization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_leases_item import (
            GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemLeasesItem,
        )
        from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_nameservers import (
            GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers,
        )
        from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_ranges_item import (
            GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemRangesItem,
        )
        from ..models.get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item_static_leases_item import (
            GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemStaticLeasesItem,
        )

        d = src_dict.copy()
        default_lease_time_secs = d.pop("defaultLeaseTimeSecs", UNSET)

        description = d.pop("description", UNSET)

        domain_name = d.pop("domainName", UNSET)

        gateway = d.pop("gateway", UNSET)

        id = d.pop("id", UNSET)

        interface = d.pop("interface", UNSET)

        ip_prefix = d.pop("ipPrefix", UNSET)

        ip_version = d.pop("ipVersion", UNSET)

        leases = []
        _leases = d.pop("leases", UNSET)
        for leases_item_data in _leases or []:
            leases_item = GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemLeasesItem.from_dict(
                leases_item_data
            )

            leases.append(leases_item)

        max_lease_time_secs = d.pop("maxLeaseTimeSecs", UNSET)

        min_lease_time_secs = d.pop("minLeaseTimeSecs", UNSET)

        name = d.pop("name", UNSET)

        _nameservers = d.pop("nameservers", UNSET)
        nameservers: Union[Unset, GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers]
        if isinstance(_nameservers, Unset):
            nameservers = UNSET
        else:
            nameservers = GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemNameservers.from_dict(
                _nameservers
            )

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemRangesItem.from_dict(
                ranges_item_data
            )

            ranges.append(ranges_item)

        static_leases = []
        _static_leases = d.pop("staticLeases", UNSET)
        for static_leases_item_data in _static_leases or []:
            static_leases_item = (
                GetV1ExtranetsIdResponse200PolicySharedSegmentDhcpSubnetsItemStaticLeasesItem.from_dict(
                    static_leases_item_data
                )
            )

            static_leases.append(static_leases_item)

        total_addresses = d.pop("totalAddresses", UNSET)

        utilization = d.pop("utilization", UNSET)

        get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item = cls(
            default_lease_time_secs=default_lease_time_secs,
            description=description,
            domain_name=domain_name,
            gateway=gateway,
            id=id,
            interface=interface,
            ip_prefix=ip_prefix,
            ip_version=ip_version,
            leases=leases,
            max_lease_time_secs=max_lease_time_secs,
            min_lease_time_secs=min_lease_time_secs,
            name=name,
            nameservers=nameservers,
            ranges=ranges,
            static_leases=static_leases,
            total_addresses=total_addresses,
            utilization=utilization,
        )

        get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item.additional_properties = d
        return get_v1_extranets_id_response_200_policy_shared_segment_dhcp_subnets_item

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
