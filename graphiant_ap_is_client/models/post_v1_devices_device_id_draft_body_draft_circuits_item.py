from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_aggregations_item import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpAggregationsItem,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_multipath import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_neighbors_item import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpNeighborsItem,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_redistributions import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_core_logical_interfaces_v2_item import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_profile import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_static_routes_item import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemStaticRoutesItem,
    )
    from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_wan_interface_v2 import (
        PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftCircuitsItem")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftCircuitsItem:
    """
    Attributes:
        bgp_aggregations (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpAggregationsItem']]):
        bgp_multipath (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath]):
        bgp_neighbors (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpNeighborsItem']]):
        bgp_redistributions (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions]):
        carrier (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_type (Union[Unset, str]):  Example: TYPE_ENUM.
        connection_type (Union[Unset, str]):  Example: TYPE_ENUM.
        core_logical_interfaces_v2 (Union[Unset,
            list['PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item']]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        dia_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        dia_snmp_index (Union[Unset, str]):  Example: TYPE_INT64.
        discovered_public_ip (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        label (Union[Unset, str]):  Example: TYPE_ENUM.
        last_resort (Union[Unset, str]):  Example: TYPE_BOOL.
        link_down_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        loopback (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        pat_addresses (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        private_ip (Union[Unset, str]):  Example: TYPE_STRING.
        profile (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile]):
        qos_profile (Union[Unset, str]):  Example: TYPE_ENUM.
        qos_profile_type (Union[Unset, str]):  Example: TYPE_ENUM.
        snmp_index (Union[Unset, str]):  Example: TYPE_INT64.
        static_routes (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemStaticRoutesItem']]):
        wan_interface_v2 (Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2]):
    """

    bgp_aggregations: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpAggregationsItem"]] = UNSET
    bgp_multipath: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath"] = UNSET
    bgp_neighbors: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpNeighborsItem"]] = UNSET
    bgp_redistributions: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions"] = UNSET
    carrier: Union[Unset, str] = UNSET
    circuit_type: Union[Unset, str] = UNSET
    connection_type: Union[Unset, str] = UNSET
    core_logical_interfaces_v2: Union[
        Unset, list["PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item"]
    ] = UNSET
    description: Union[Unset, str] = UNSET
    dia_enabled: Union[Unset, str] = UNSET
    dia_snmp_index: Union[Unset, str] = UNSET
    discovered_public_ip: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    last_resort: Union[Unset, str] = UNSET
    link_down_speed_mbps: Union[Unset, str] = UNSET
    link_up_speed_mbps: Union[Unset, str] = UNSET
    loopback: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pat_addresses: Union[Unset, list[str]] = UNSET
    private_ip: Union[Unset, str] = UNSET
    profile: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile"] = UNSET
    qos_profile: Union[Unset, str] = UNSET
    qos_profile_type: Union[Unset, str] = UNSET
    snmp_index: Union[Unset, str] = UNSET
    static_routes: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemStaticRoutesItem"]] = UNSET
    wan_interface_v2: Union[Unset, "PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_aggregations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_aggregations, Unset):
            bgp_aggregations = []
            for bgp_aggregations_item_data in self.bgp_aggregations:
                bgp_aggregations_item = bgp_aggregations_item_data.to_dict()
                bgp_aggregations.append(bgp_aggregations_item)

        bgp_multipath: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_multipath, Unset):
            bgp_multipath = self.bgp_multipath.to_dict()

        bgp_neighbors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_neighbors, Unset):
            bgp_neighbors = []
            for bgp_neighbors_item_data in self.bgp_neighbors:
                bgp_neighbors_item = bgp_neighbors_item_data.to_dict()
                bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistributions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bgp_redistributions, Unset):
            bgp_redistributions = self.bgp_redistributions.to_dict()

        carrier = self.carrier

        circuit_type = self.circuit_type

        connection_type = self.connection_type

        core_logical_interfaces_v2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.core_logical_interfaces_v2, Unset):
            core_logical_interfaces_v2 = []
            for core_logical_interfaces_v2_item_data in self.core_logical_interfaces_v2:
                core_logical_interfaces_v2_item = core_logical_interfaces_v2_item_data.to_dict()
                core_logical_interfaces_v2.append(core_logical_interfaces_v2_item)

        description = self.description

        dia_enabled = self.dia_enabled

        dia_snmp_index = self.dia_snmp_index

        discovered_public_ip = self.discovered_public_ip

        id = self.id

        interface_name = self.interface_name

        label = self.label

        last_resort = self.last_resort

        link_down_speed_mbps = self.link_down_speed_mbps

        link_up_speed_mbps = self.link_up_speed_mbps

        loopback = self.loopback

        name = self.name

        pat_addresses: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pat_addresses, Unset):
            pat_addresses = self.pat_addresses

        private_ip = self.private_ip

        profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        qos_profile = self.qos_profile

        qos_profile_type = self.qos_profile_type

        snmp_index = self.snmp_index

        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        wan_interface_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.wan_interface_v2, Unset):
            wan_interface_v2 = self.wan_interface_v2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_aggregations is not UNSET:
            field_dict["bgpAggregations"] = bgp_aggregations
        if bgp_multipath is not UNSET:
            field_dict["bgpMultipath"] = bgp_multipath
        if bgp_neighbors is not UNSET:
            field_dict["bgpNeighbors"] = bgp_neighbors
        if bgp_redistributions is not UNSET:
            field_dict["bgpRedistributions"] = bgp_redistributions
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if circuit_type is not UNSET:
            field_dict["circuitType"] = circuit_type
        if connection_type is not UNSET:
            field_dict["connectionType"] = connection_type
        if core_logical_interfaces_v2 is not UNSET:
            field_dict["coreLogicalInterfacesV2"] = core_logical_interfaces_v2
        if description is not UNSET:
            field_dict["description"] = description
        if dia_enabled is not UNSET:
            field_dict["diaEnabled"] = dia_enabled
        if dia_snmp_index is not UNSET:
            field_dict["diaSnmpIndex"] = dia_snmp_index
        if discovered_public_ip is not UNSET:
            field_dict["discoveredPublicIp"] = discovered_public_ip
        if id is not UNSET:
            field_dict["id"] = id
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if label is not UNSET:
            field_dict["label"] = label
        if last_resort is not UNSET:
            field_dict["lastResort"] = last_resort
        if link_down_speed_mbps is not UNSET:
            field_dict["linkDownSpeedMbps"] = link_down_speed_mbps
        if link_up_speed_mbps is not UNSET:
            field_dict["linkUpSpeedMbps"] = link_up_speed_mbps
        if loopback is not UNSET:
            field_dict["loopback"] = loopback
        if name is not UNSET:
            field_dict["name"] = name
        if pat_addresses is not UNSET:
            field_dict["patAddresses"] = pat_addresses
        if private_ip is not UNSET:
            field_dict["privateIp"] = private_ip
        if profile is not UNSET:
            field_dict["profile"] = profile
        if qos_profile is not UNSET:
            field_dict["qosProfile"] = qos_profile
        if qos_profile_type is not UNSET:
            field_dict["qosProfileType"] = qos_profile_type
        if snmp_index is not UNSET:
            field_dict["snmpIndex"] = snmp_index
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes
        if wan_interface_v2 is not UNSET:
            field_dict["wanInterfaceV2"] = wan_interface_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_aggregations_item import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpAggregationsItem,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_multipath import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_neighbors_item import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpNeighborsItem,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_bgp_redistributions import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_core_logical_interfaces_v2_item import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_profile import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_static_routes_item import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemStaticRoutesItem,
        )
        from ..models.post_v1_devices_device_id_draft_body_draft_circuits_item_wan_interface_v2 import (
            PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2,
        )

        d = src_dict.copy()
        bgp_aggregations = []
        _bgp_aggregations = d.pop("bgpAggregations", UNSET)
        for bgp_aggregations_item_data in _bgp_aggregations or []:
            bgp_aggregations_item = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpAggregationsItem.from_dict(
                bgp_aggregations_item_data
            )

            bgp_aggregations.append(bgp_aggregations_item)

        _bgp_multipath = d.pop("bgpMultipath", UNSET)
        bgp_multipath: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath]
        if isinstance(_bgp_multipath, Unset):
            bgp_multipath = UNSET
        else:
            bgp_multipath = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpMultipath.from_dict(_bgp_multipath)

        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgpNeighbors", UNSET)
        for bgp_neighbors_item_data in _bgp_neighbors or []:
            bgp_neighbors_item = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpNeighborsItem.from_dict(
                bgp_neighbors_item_data
            )

            bgp_neighbors.append(bgp_neighbors_item)

        _bgp_redistributions = d.pop("bgpRedistributions", UNSET)
        bgp_redistributions: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions]
        if isinstance(_bgp_redistributions, Unset):
            bgp_redistributions = UNSET
        else:
            bgp_redistributions = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemBgpRedistributions.from_dict(
                _bgp_redistributions
            )

        carrier = d.pop("carrier", UNSET)

        circuit_type = d.pop("circuitType", UNSET)

        connection_type = d.pop("connectionType", UNSET)

        core_logical_interfaces_v2 = []
        _core_logical_interfaces_v2 = d.pop("coreLogicalInterfacesV2", UNSET)
        for core_logical_interfaces_v2_item_data in _core_logical_interfaces_v2 or []:
            core_logical_interfaces_v2_item = (
                PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemCoreLogicalInterfacesV2Item.from_dict(
                    core_logical_interfaces_v2_item_data
                )
            )

            core_logical_interfaces_v2.append(core_logical_interfaces_v2_item)

        description = d.pop("description", UNSET)

        dia_enabled = d.pop("diaEnabled", UNSET)

        dia_snmp_index = d.pop("diaSnmpIndex", UNSET)

        discovered_public_ip = d.pop("discoveredPublicIp", UNSET)

        id = d.pop("id", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        label = d.pop("label", UNSET)

        last_resort = d.pop("lastResort", UNSET)

        link_down_speed_mbps = d.pop("linkDownSpeedMbps", UNSET)

        link_up_speed_mbps = d.pop("linkUpSpeedMbps", UNSET)

        loopback = d.pop("loopback", UNSET)

        name = d.pop("name", UNSET)

        pat_addresses = cast(list[str], d.pop("patAddresses", UNSET))

        private_ip = d.pop("privateIp", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemProfile.from_dict(_profile)

        qos_profile = d.pop("qosProfile", UNSET)

        qos_profile_type = d.pop("qosProfileType", UNSET)

        snmp_index = d.pop("snmpIndex", UNSET)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemStaticRoutesItem.from_dict(
                static_routes_item_data
            )

            static_routes.append(static_routes_item)

        _wan_interface_v2 = d.pop("wanInterfaceV2", UNSET)
        wan_interface_v2: Union[Unset, PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2]
        if isinstance(_wan_interface_v2, Unset):
            wan_interface_v2 = UNSET
        else:
            wan_interface_v2 = PostV1DevicesDeviceIdDraftBodyDraftCircuitsItemWanInterfaceV2.from_dict(
                _wan_interface_v2
            )

        post_v1_devices_device_id_draft_body_draft_circuits_item = cls(
            bgp_aggregations=bgp_aggregations,
            bgp_multipath=bgp_multipath,
            bgp_neighbors=bgp_neighbors,
            bgp_redistributions=bgp_redistributions,
            carrier=carrier,
            circuit_type=circuit_type,
            connection_type=connection_type,
            core_logical_interfaces_v2=core_logical_interfaces_v2,
            description=description,
            dia_enabled=dia_enabled,
            dia_snmp_index=dia_snmp_index,
            discovered_public_ip=discovered_public_ip,
            id=id,
            interface_name=interface_name,
            label=label,
            last_resort=last_resort,
            link_down_speed_mbps=link_down_speed_mbps,
            link_up_speed_mbps=link_up_speed_mbps,
            loopback=loopback,
            name=name,
            pat_addresses=pat_addresses,
            private_ip=private_ip,
            profile=profile,
            qos_profile=qos_profile,
            qos_profile_type=qos_profile_type,
            snmp_index=snmp_index,
            static_routes=static_routes,
            wan_interface_v2=wan_interface_v2,
        )

        post_v1_devices_device_id_draft_body_draft_circuits_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_circuits_item

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
