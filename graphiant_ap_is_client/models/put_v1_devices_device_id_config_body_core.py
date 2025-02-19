from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_bgp_instance import (
        PutV1DevicesDeviceIdConfigBodyCoreBgpInstance,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf import PutV1DevicesDeviceIdConfigBodyCoreCoreVrf
    from ..models.put_v1_devices_device_id_config_body_core_interfaces_item import (
        PutV1DevicesDeviceIdConfigBodyCoreInterfacesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_ipfix_exporters_item import (
        PutV1DevicesDeviceIdConfigBodyCoreIpfixExportersItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_isp_vrfs_item import (
        PutV1DevicesDeviceIdConfigBodyCoreIspVrfsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_prefix_sets_item import (
        PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_prometheus import (
        PutV1DevicesDeviceIdConfigBodyCorePrometheus,
    )
    from ..models.put_v1_devices_device_id_config_body_core_route_policies_item import (
        PutV1DevicesDeviceIdConfigBodyCoreRoutePoliciesItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site import PutV1DevicesDeviceIdConfigBodyCoreSite
    from ..models.put_v1_devices_device_id_config_body_core_traffic_policy import (
        PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy,
    )
    from ..models.put_v1_devices_device_id_config_body_core_vrfs_item import PutV1DevicesDeviceIdConfigBodyCoreVrfsItem


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCore")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCore:
    """
    Attributes:
        bgp_instance (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreBgpInstance]):
        core_vrf (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrf]):
        interfaces (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreInterfacesItem']]):
        ipfix_exporters (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreIpfixExportersItem']]):
        isp_vrfs (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreIspVrfsItem']]):
        maintenance_mode (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_sets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItem']]):
        prometheus (Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheus]):
        region (Union[Unset, str]):  Example: TYPE_ENUM.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
        route_policies (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreRoutePoliciesItem']]):
        site (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSite]):
        traffic_policy (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy]):
        vrfs (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreVrfsItem']]):
    """

    bgp_instance: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreBgpInstance"] = UNSET
    core_vrf: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrf"] = UNSET
    interfaces: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreInterfacesItem"]] = UNSET
    ipfix_exporters: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreIpfixExportersItem"]] = UNSET
    isp_vrfs: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreIspVrfsItem"]] = UNSET
    maintenance_mode: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    prefix_sets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItem"]] = UNSET
    prometheus: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCorePrometheus"] = UNSET
    region: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    route_policies: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreRoutePoliciesItem"]] = UNSET
    site: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreSite"] = UNSET
    traffic_policy: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy"] = UNSET
    vrfs: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreVrfsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_instance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_instance, Unset):
            bgp_instance = self.bgp_instance.to_dict()

        core_vrf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.core_vrf, Unset):
            core_vrf = self.core_vrf.to_dict()

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        ipfix_exporters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporters, Unset):
            ipfix_exporters = []
            for ipfix_exporters_item_data in self.ipfix_exporters:
                ipfix_exporters_item = ipfix_exporters_item_data.to_dict()
                ipfix_exporters.append(ipfix_exporters_item)

        isp_vrfs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.isp_vrfs, Unset):
            isp_vrfs = []
            for isp_vrfs_item_data in self.isp_vrfs:
                isp_vrfs_item = isp_vrfs_item_data.to_dict()
                isp_vrfs.append(isp_vrfs_item)

        maintenance_mode = self.maintenance_mode

        name = self.name

        prefix_sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_sets, Unset):
            prefix_sets = []
            for prefix_sets_item_data in self.prefix_sets:
                prefix_sets_item = prefix_sets_item_data.to_dict()
                prefix_sets.append(prefix_sets_item)

        prometheus: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prometheus, Unset):
            prometheus = self.prometheus.to_dict()

        region = self.region

        region_name = self.region_name

        route_policies: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.route_policies, Unset):
            route_policies = []
            for route_policies_item_data in self.route_policies:
                route_policies_item = route_policies_item_data.to_dict()
                route_policies.append(route_policies_item)

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        traffic_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.traffic_policy, Unset):
            traffic_policy = self.traffic_policy.to_dict()

        vrfs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrfs, Unset):
            vrfs = []
            for vrfs_item_data in self.vrfs:
                vrfs_item = vrfs_item_data.to_dict()
                vrfs.append(vrfs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_instance is not UNSET:
            field_dict["bgpInstance"] = bgp_instance
        if core_vrf is not UNSET:
            field_dict["coreVrf"] = core_vrf
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if ipfix_exporters is not UNSET:
            field_dict["ipfixExporters"] = ipfix_exporters
        if isp_vrfs is not UNSET:
            field_dict["ispVrfs"] = isp_vrfs
        if maintenance_mode is not UNSET:
            field_dict["maintenanceMode"] = maintenance_mode
        if name is not UNSET:
            field_dict["name"] = name
        if prefix_sets is not UNSET:
            field_dict["prefixSets"] = prefix_sets
        if prometheus is not UNSET:
            field_dict["prometheus"] = prometheus
        if region is not UNSET:
            field_dict["region"] = region
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if route_policies is not UNSET:
            field_dict["routePolicies"] = route_policies
        if site is not UNSET:
            field_dict["site"] = site
        if traffic_policy is not UNSET:
            field_dict["trafficPolicy"] = traffic_policy
        if vrfs is not UNSET:
            field_dict["vrfs"] = vrfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_bgp_instance import (
            PutV1DevicesDeviceIdConfigBodyCoreBgpInstance,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrf,
        )
        from ..models.put_v1_devices_device_id_config_body_core_interfaces_item import (
            PutV1DevicesDeviceIdConfigBodyCoreInterfacesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_ipfix_exporters_item import (
            PutV1DevicesDeviceIdConfigBodyCoreIpfixExportersItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_isp_vrfs_item import (
            PutV1DevicesDeviceIdConfigBodyCoreIspVrfsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_prefix_sets_item import (
            PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_prometheus import (
            PutV1DevicesDeviceIdConfigBodyCorePrometheus,
        )
        from ..models.put_v1_devices_device_id_config_body_core_route_policies_item import (
            PutV1DevicesDeviceIdConfigBodyCoreRoutePoliciesItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site import PutV1DevicesDeviceIdConfigBodyCoreSite
        from ..models.put_v1_devices_device_id_config_body_core_traffic_policy import (
            PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy,
        )
        from ..models.put_v1_devices_device_id_config_body_core_vrfs_item import (
            PutV1DevicesDeviceIdConfigBodyCoreVrfsItem,
        )

        d = src_dict.copy()
        _bgp_instance = d.pop("bgpInstance", UNSET)
        bgp_instance: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreBgpInstance]
        if isinstance(_bgp_instance, Unset):
            bgp_instance = UNSET
        else:
            bgp_instance = PutV1DevicesDeviceIdConfigBodyCoreBgpInstance.from_dict(_bgp_instance)

        _core_vrf = d.pop("coreVrf", UNSET)
        core_vrf: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrf]
        if isinstance(_core_vrf, Unset):
            core_vrf = UNSET
        else:
            core_vrf = PutV1DevicesDeviceIdConfigBodyCoreCoreVrf.from_dict(_core_vrf)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = PutV1DevicesDeviceIdConfigBodyCoreInterfacesItem.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        ipfix_exporters = []
        _ipfix_exporters = d.pop("ipfixExporters", UNSET)
        for ipfix_exporters_item_data in _ipfix_exporters or []:
            ipfix_exporters_item = PutV1DevicesDeviceIdConfigBodyCoreIpfixExportersItem.from_dict(
                ipfix_exporters_item_data
            )

            ipfix_exporters.append(ipfix_exporters_item)

        isp_vrfs = []
        _isp_vrfs = d.pop("ispVrfs", UNSET)
        for isp_vrfs_item_data in _isp_vrfs or []:
            isp_vrfs_item = PutV1DevicesDeviceIdConfigBodyCoreIspVrfsItem.from_dict(isp_vrfs_item_data)

            isp_vrfs.append(isp_vrfs_item)

        maintenance_mode = d.pop("maintenanceMode", UNSET)

        name = d.pop("name", UNSET)

        prefix_sets = []
        _prefix_sets = d.pop("prefixSets", UNSET)
        for prefix_sets_item_data in _prefix_sets or []:
            prefix_sets_item = PutV1DevicesDeviceIdConfigBodyCorePrefixSetsItem.from_dict(prefix_sets_item_data)

            prefix_sets.append(prefix_sets_item)

        _prometheus = d.pop("prometheus", UNSET)
        prometheus: Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheus]
        if isinstance(_prometheus, Unset):
            prometheus = UNSET
        else:
            prometheus = PutV1DevicesDeviceIdConfigBodyCorePrometheus.from_dict(_prometheus)

        region = d.pop("region", UNSET)

        region_name = d.pop("regionName", UNSET)

        route_policies = []
        _route_policies = d.pop("routePolicies", UNSET)
        for route_policies_item_data in _route_policies or []:
            route_policies_item = PutV1DevicesDeviceIdConfigBodyCoreRoutePoliciesItem.from_dict(
                route_policies_item_data
            )

            route_policies.append(route_policies_item)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PutV1DevicesDeviceIdConfigBodyCoreSite.from_dict(_site)

        _traffic_policy = d.pop("trafficPolicy", UNSET)
        traffic_policy: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy]
        if isinstance(_traffic_policy, Unset):
            traffic_policy = UNSET
        else:
            traffic_policy = PutV1DevicesDeviceIdConfigBodyCoreTrafficPolicy.from_dict(_traffic_policy)

        vrfs = []
        _vrfs = d.pop("vrfs", UNSET)
        for vrfs_item_data in _vrfs or []:
            vrfs_item = PutV1DevicesDeviceIdConfigBodyCoreVrfsItem.from_dict(vrfs_item_data)

            vrfs.append(vrfs_item)

        put_v1_devices_device_id_config_body_core = cls(
            bgp_instance=bgp_instance,
            core_vrf=core_vrf,
            interfaces=interfaces,
            ipfix_exporters=ipfix_exporters,
            isp_vrfs=isp_vrfs,
            maintenance_mode=maintenance_mode,
            name=name,
            prefix_sets=prefix_sets,
            prometheus=prometheus,
            region=region,
            region_name=region_name,
            route_policies=route_policies,
            site=site,
            traffic_policy=traffic_policy,
            vrfs=vrfs,
        )

        put_v1_devices_device_id_config_body_core.additional_properties = d
        return put_v1_devices_device_id_config_body_core

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
