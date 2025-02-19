from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_site_global_prefix_set_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteGlobalPrefixSetOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_ipfix_exporter_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_ipfix_exporter_ops_v2_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsV2Item,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_location import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteLocation,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_prefix_set_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSitePrefixSetOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_route_tag import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_routing_policy_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteRoutingPolicyOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_snmp_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteSnmpOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_syslog_server_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_syslog_server_ops_v2_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsV2Item,
    )
    from ..models.put_v1_devices_device_id_config_body_core_site_traffic_policy_ops_item import (
        PutV1DevicesDeviceIdConfigBodyCoreSiteTrafficPolicyOpsItem,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreSite")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreSite:
    """
    Attributes:
        global_prefix_set_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteGlobalPrefixSetOpsItem']]):
        ipfix_exporter_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsItem']]):
        ipfix_exporter_ops_v2 (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsV2Item']]):
        location (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSiteLocation]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        prefix_set_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSitePrefixSetOpsItem']]):
        route_tag (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag]):
        routing_policy_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteRoutingPolicyOpsItem']]):
        snmp_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteSnmpOpsItem']]):
        syslog_server_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsItem']]):
        syslog_server_ops_v2 (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsV2Item']]):
        traffic_policy_ops (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyCoreSiteTrafficPolicyOpsItem']]):
    """

    global_prefix_set_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteGlobalPrefixSetOpsItem"]] = UNSET
    ipfix_exporter_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsItem"]] = UNSET
    ipfix_exporter_ops_v2: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsV2Item"]] = UNSET
    location: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreSiteLocation"] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    prefix_set_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSitePrefixSetOpsItem"]] = UNSET
    route_tag: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag"] = UNSET
    routing_policy_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteRoutingPolicyOpsItem"]] = UNSET
    snmp_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteSnmpOpsItem"]] = UNSET
    syslog_server_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsItem"]] = UNSET
    syslog_server_ops_v2: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsV2Item"]] = UNSET
    traffic_policy_ops: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyCoreSiteTrafficPolicyOpsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_prefix_set_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.global_prefix_set_ops, Unset):
            global_prefix_set_ops = []
            for global_prefix_set_ops_item_data in self.global_prefix_set_ops:
                global_prefix_set_ops_item = global_prefix_set_ops_item_data.to_dict()
                global_prefix_set_ops.append(global_prefix_set_ops_item)

        ipfix_exporter_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporter_ops, Unset):
            ipfix_exporter_ops = []
            for ipfix_exporter_ops_item_data in self.ipfix_exporter_ops:
                ipfix_exporter_ops_item = ipfix_exporter_ops_item_data.to_dict()
                ipfix_exporter_ops.append(ipfix_exporter_ops_item)

        ipfix_exporter_ops_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipfix_exporter_ops_v2, Unset):
            ipfix_exporter_ops_v2 = []
            for ipfix_exporter_ops_v2_item_data in self.ipfix_exporter_ops_v2:
                ipfix_exporter_ops_v2_item = ipfix_exporter_ops_v2_item_data.to_dict()
                ipfix_exporter_ops_v2.append(ipfix_exporter_ops_v2_item)

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        name = self.name

        notes = self.notes

        prefix_set_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prefix_set_ops, Unset):
            prefix_set_ops = []
            for prefix_set_ops_item_data in self.prefix_set_ops:
                prefix_set_ops_item = prefix_set_ops_item_data.to_dict()
                prefix_set_ops.append(prefix_set_ops_item)

        route_tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.route_tag, Unset):
            route_tag = self.route_tag.to_dict()

        routing_policy_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routing_policy_ops, Unset):
            routing_policy_ops = []
            for routing_policy_ops_item_data in self.routing_policy_ops:
                routing_policy_ops_item = routing_policy_ops_item_data.to_dict()
                routing_policy_ops.append(routing_policy_ops_item)

        snmp_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.snmp_ops, Unset):
            snmp_ops = []
            for snmp_ops_item_data in self.snmp_ops:
                snmp_ops_item = snmp_ops_item_data.to_dict()
                snmp_ops.append(snmp_ops_item)

        syslog_server_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_server_ops, Unset):
            syslog_server_ops = []
            for syslog_server_ops_item_data in self.syslog_server_ops:
                syslog_server_ops_item = syslog_server_ops_item_data.to_dict()
                syslog_server_ops.append(syslog_server_ops_item)

        syslog_server_ops_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.syslog_server_ops_v2, Unset):
            syslog_server_ops_v2 = []
            for syslog_server_ops_v2_item_data in self.syslog_server_ops_v2:
                syslog_server_ops_v2_item = syslog_server_ops_v2_item_data.to_dict()
                syslog_server_ops_v2.append(syslog_server_ops_v2_item)

        traffic_policy_ops: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.traffic_policy_ops, Unset):
            traffic_policy_ops = []
            for traffic_policy_ops_item_data in self.traffic_policy_ops:
                traffic_policy_ops_item = traffic_policy_ops_item_data.to_dict()
                traffic_policy_ops.append(traffic_policy_ops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_prefix_set_ops is not UNSET:
            field_dict["globalPrefixSetOps"] = global_prefix_set_ops
        if ipfix_exporter_ops is not UNSET:
            field_dict["ipfixExporterOps"] = ipfix_exporter_ops
        if ipfix_exporter_ops_v2 is not UNSET:
            field_dict["ipfixExporterOpsV2"] = ipfix_exporter_ops_v2
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if prefix_set_ops is not UNSET:
            field_dict["prefixSetOps"] = prefix_set_ops
        if route_tag is not UNSET:
            field_dict["routeTag"] = route_tag
        if routing_policy_ops is not UNSET:
            field_dict["routingPolicyOps"] = routing_policy_ops
        if snmp_ops is not UNSET:
            field_dict["snmpOps"] = snmp_ops
        if syslog_server_ops is not UNSET:
            field_dict["syslogServerOps"] = syslog_server_ops
        if syslog_server_ops_v2 is not UNSET:
            field_dict["syslogServerOpsV2"] = syslog_server_ops_v2
        if traffic_policy_ops is not UNSET:
            field_dict["trafficPolicyOps"] = traffic_policy_ops

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_site_global_prefix_set_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteGlobalPrefixSetOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_ipfix_exporter_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_ipfix_exporter_ops_v2_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsV2Item,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_location import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteLocation,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_prefix_set_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSitePrefixSetOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_route_tag import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_routing_policy_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteRoutingPolicyOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_snmp_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteSnmpOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_syslog_server_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_syslog_server_ops_v2_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsV2Item,
        )
        from ..models.put_v1_devices_device_id_config_body_core_site_traffic_policy_ops_item import (
            PutV1DevicesDeviceIdConfigBodyCoreSiteTrafficPolicyOpsItem,
        )

        d = src_dict.copy()
        global_prefix_set_ops = []
        _global_prefix_set_ops = d.pop("globalPrefixSetOps", UNSET)
        for global_prefix_set_ops_item_data in _global_prefix_set_ops or []:
            global_prefix_set_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteGlobalPrefixSetOpsItem.from_dict(
                global_prefix_set_ops_item_data
            )

            global_prefix_set_ops.append(global_prefix_set_ops_item)

        ipfix_exporter_ops = []
        _ipfix_exporter_ops = d.pop("ipfixExporterOps", UNSET)
        for ipfix_exporter_ops_item_data in _ipfix_exporter_ops or []:
            ipfix_exporter_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsItem.from_dict(
                ipfix_exporter_ops_item_data
            )

            ipfix_exporter_ops.append(ipfix_exporter_ops_item)

        ipfix_exporter_ops_v2 = []
        _ipfix_exporter_ops_v2 = d.pop("ipfixExporterOpsV2", UNSET)
        for ipfix_exporter_ops_v2_item_data in _ipfix_exporter_ops_v2 or []:
            ipfix_exporter_ops_v2_item = PutV1DevicesDeviceIdConfigBodyCoreSiteIpfixExporterOpsV2Item.from_dict(
                ipfix_exporter_ops_v2_item_data
            )

            ipfix_exporter_ops_v2.append(ipfix_exporter_ops_v2_item)

        _location = d.pop("location", UNSET)
        location: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSiteLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = PutV1DevicesDeviceIdConfigBodyCoreSiteLocation.from_dict(_location)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        prefix_set_ops = []
        _prefix_set_ops = d.pop("prefixSetOps", UNSET)
        for prefix_set_ops_item_data in _prefix_set_ops or []:
            prefix_set_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSitePrefixSetOpsItem.from_dict(
                prefix_set_ops_item_data
            )

            prefix_set_ops.append(prefix_set_ops_item)

        _route_tag = d.pop("routeTag", UNSET)
        route_tag: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag]
        if isinstance(_route_tag, Unset):
            route_tag = UNSET
        else:
            route_tag = PutV1DevicesDeviceIdConfigBodyCoreSiteRouteTag.from_dict(_route_tag)

        routing_policy_ops = []
        _routing_policy_ops = d.pop("routingPolicyOps", UNSET)
        for routing_policy_ops_item_data in _routing_policy_ops or []:
            routing_policy_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteRoutingPolicyOpsItem.from_dict(
                routing_policy_ops_item_data
            )

            routing_policy_ops.append(routing_policy_ops_item)

        snmp_ops = []
        _snmp_ops = d.pop("snmpOps", UNSET)
        for snmp_ops_item_data in _snmp_ops or []:
            snmp_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteSnmpOpsItem.from_dict(snmp_ops_item_data)

            snmp_ops.append(snmp_ops_item)

        syslog_server_ops = []
        _syslog_server_ops = d.pop("syslogServerOps", UNSET)
        for syslog_server_ops_item_data in _syslog_server_ops or []:
            syslog_server_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsItem.from_dict(
                syslog_server_ops_item_data
            )

            syslog_server_ops.append(syslog_server_ops_item)

        syslog_server_ops_v2 = []
        _syslog_server_ops_v2 = d.pop("syslogServerOpsV2", UNSET)
        for syslog_server_ops_v2_item_data in _syslog_server_ops_v2 or []:
            syslog_server_ops_v2_item = PutV1DevicesDeviceIdConfigBodyCoreSiteSyslogServerOpsV2Item.from_dict(
                syslog_server_ops_v2_item_data
            )

            syslog_server_ops_v2.append(syslog_server_ops_v2_item)

        traffic_policy_ops = []
        _traffic_policy_ops = d.pop("trafficPolicyOps", UNSET)
        for traffic_policy_ops_item_data in _traffic_policy_ops or []:
            traffic_policy_ops_item = PutV1DevicesDeviceIdConfigBodyCoreSiteTrafficPolicyOpsItem.from_dict(
                traffic_policy_ops_item_data
            )

            traffic_policy_ops.append(traffic_policy_ops_item)

        put_v1_devices_device_id_config_body_core_site = cls(
            global_prefix_set_ops=global_prefix_set_ops,
            ipfix_exporter_ops=ipfix_exporter_ops,
            ipfix_exporter_ops_v2=ipfix_exporter_ops_v2,
            location=location,
            name=name,
            notes=notes,
            prefix_set_ops=prefix_set_ops,
            route_tag=route_tag,
            routing_policy_ops=routing_policy_ops,
            snmp_ops=snmp_ops,
            syslog_server_ops=syslog_server_ops,
            syslog_server_ops_v2=syslog_server_ops_v2,
            traffic_policy_ops=traffic_policy_ops,
        )

        put_v1_devices_device_id_config_body_core_site.additional_properties = d
        return put_v1_devices_device_id_config_body_core_site

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
