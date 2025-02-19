from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_aggregations_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpAggregationsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_multipath import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_neighbors_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpNeighborsItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_redistribution_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpRedistributionItem,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_pat_addresses import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_static_routes_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueStaticRoutesItem,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValue:
    """
    Attributes:
        bgp_aggregations (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpAggregationsItem']]):
        bgp_multipath (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath]):
        bgp_neighbors (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpNeighborsItem']]):
        bgp_redistribution (Union[Unset,
            list['PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpRedistributionItem']]):
        carrier (Union[Unset, str]):  Example: TYPE_ENUM.
        circuit_type (Union[Unset, str]):  Example: TYPE_ENUM.
        connection_type (Union[Unset, str]):  Example: TYPE_ENUM.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        dia_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        label (Union[Unset, str]):  Example: TYPE_ENUM.
        last_resort (Union[Unset, str]):  Example: TYPE_BOOL.
        link_down_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        link_up_speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        loopback (Union[Unset, str]):  Example: TYPE_BOOL.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        pat_addresses (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses]):
        qos_profile (Union[Unset, str]):  Example: TYPE_ENUM.
        qos_profile_type (Union[Unset, str]):  Example: TYPE_ENUM.
        static_routes (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueStaticRoutesItem']]):
    """

    bgp_aggregations: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpAggregationsItem"]] = (
        UNSET
    )
    bgp_multipath: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath"] = UNSET
    bgp_neighbors: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpNeighborsItem"]] = UNSET
    bgp_redistribution: Union[
        Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpRedistributionItem"]
    ] = UNSET
    carrier: Union[Unset, str] = UNSET
    circuit_type: Union[Unset, str] = UNSET
    connection_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    dia_enabled: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    last_resort: Union[Unset, str] = UNSET
    link_down_speed_mbps: Union[Unset, str] = UNSET
    link_up_speed_mbps: Union[Unset, str] = UNSET
    loopback: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    pat_addresses: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses"] = UNSET
    qos_profile: Union[Unset, str] = UNSET
    qos_profile_type: Union[Unset, str] = UNSET
    static_routes: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueStaticRoutesItem"]] = UNSET
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

        bgp_redistribution: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_redistribution, Unset):
            bgp_redistribution = []
            for bgp_redistribution_item_data in self.bgp_redistribution:
                bgp_redistribution_item = bgp_redistribution_item_data.to_dict()
                bgp_redistribution.append(bgp_redistribution_item)

        carrier = self.carrier

        circuit_type = self.circuit_type

        connection_type = self.connection_type

        description = self.description

        dia_enabled = self.dia_enabled

        label = self.label

        last_resort = self.last_resort

        link_down_speed_mbps = self.link_down_speed_mbps

        link_up_speed_mbps = self.link_up_speed_mbps

        loopback = self.loopback

        name = self.name

        pat_addresses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pat_addresses, Unset):
            pat_addresses = self.pat_addresses.to_dict()

        qos_profile = self.qos_profile

        qos_profile_type = self.qos_profile_type

        static_routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_routes, Unset):
            static_routes = []
            for static_routes_item_data in self.static_routes:
                static_routes_item = static_routes_item_data.to_dict()
                static_routes.append(static_routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_aggregations is not UNSET:
            field_dict["bgpAggregations"] = bgp_aggregations
        if bgp_multipath is not UNSET:
            field_dict["bgpMultipath"] = bgp_multipath
        if bgp_neighbors is not UNSET:
            field_dict["bgpNeighbors"] = bgp_neighbors
        if bgp_redistribution is not UNSET:
            field_dict["bgpRedistribution"] = bgp_redistribution
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if circuit_type is not UNSET:
            field_dict["circuitType"] = circuit_type
        if connection_type is not UNSET:
            field_dict["connectionType"] = connection_type
        if description is not UNSET:
            field_dict["description"] = description
        if dia_enabled is not UNSET:
            field_dict["diaEnabled"] = dia_enabled
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
        if qos_profile is not UNSET:
            field_dict["qosProfile"] = qos_profile
        if qos_profile_type is not UNSET:
            field_dict["qosProfileType"] = qos_profile_type
        if static_routes is not UNSET:
            field_dict["staticRoutes"] = static_routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_aggregations_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpAggregationsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_multipath import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_neighbors_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpNeighborsItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_bgp_redistribution_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpRedistributionItem,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_pat_addresses import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_circuits_item_value_static_routes_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueStaticRoutesItem,
        )

        d = src_dict.copy()
        bgp_aggregations = []
        _bgp_aggregations = d.pop("bgpAggregations", UNSET)
        for bgp_aggregations_item_data in _bgp_aggregations or []:
            bgp_aggregations_item = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpAggregationsItem.from_dict(
                bgp_aggregations_item_data
            )

            bgp_aggregations.append(bgp_aggregations_item)

        _bgp_multipath = d.pop("bgpMultipath", UNSET)
        bgp_multipath: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath]
        if isinstance(_bgp_multipath, Unset):
            bgp_multipath = UNSET
        else:
            bgp_multipath = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpMultipath.from_dict(_bgp_multipath)

        bgp_neighbors = []
        _bgp_neighbors = d.pop("bgpNeighbors", UNSET)
        for bgp_neighbors_item_data in _bgp_neighbors or []:
            bgp_neighbors_item = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpNeighborsItem.from_dict(
                bgp_neighbors_item_data
            )

            bgp_neighbors.append(bgp_neighbors_item)

        bgp_redistribution = []
        _bgp_redistribution = d.pop("bgpRedistribution", UNSET)
        for bgp_redistribution_item_data in _bgp_redistribution or []:
            bgp_redistribution_item = (
                PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueBgpRedistributionItem.from_dict(
                    bgp_redistribution_item_data
                )
            )

            bgp_redistribution.append(bgp_redistribution_item)

        carrier = d.pop("carrier", UNSET)

        circuit_type = d.pop("circuitType", UNSET)

        connection_type = d.pop("connectionType", UNSET)

        description = d.pop("description", UNSET)

        dia_enabled = d.pop("diaEnabled", UNSET)

        label = d.pop("label", UNSET)

        last_resort = d.pop("lastResort", UNSET)

        link_down_speed_mbps = d.pop("linkDownSpeedMbps", UNSET)

        link_up_speed_mbps = d.pop("linkUpSpeedMbps", UNSET)

        loopback = d.pop("loopback", UNSET)

        name = d.pop("name", UNSET)

        _pat_addresses = d.pop("patAddresses", UNSET)
        pat_addresses: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses]
        if isinstance(_pat_addresses, Unset):
            pat_addresses = UNSET
        else:
            pat_addresses = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValuePatAddresses.from_dict(_pat_addresses)

        qos_profile = d.pop("qosProfile", UNSET)

        qos_profile_type = d.pop("qosProfileType", UNSET)

        static_routes = []
        _static_routes = d.pop("staticRoutes", UNSET)
        for static_routes_item_data in _static_routes or []:
            static_routes_item = PutV1DevicesDeviceIdConfigBodyEdgeCircuitsItemValueStaticRoutesItem.from_dict(
                static_routes_item_data
            )

            static_routes.append(static_routes_item)

        put_v1_devices_device_id_config_body_edge_circuits_item_value = cls(
            bgp_aggregations=bgp_aggregations,
            bgp_multipath=bgp_multipath,
            bgp_neighbors=bgp_neighbors,
            bgp_redistribution=bgp_redistribution,
            carrier=carrier,
            circuit_type=circuit_type,
            connection_type=connection_type,
            description=description,
            dia_enabled=dia_enabled,
            label=label,
            last_resort=last_resort,
            link_down_speed_mbps=link_down_speed_mbps,
            link_up_speed_mbps=link_up_speed_mbps,
            loopback=loopback,
            name=name,
            pat_addresses=pat_addresses,
            qos_profile=qos_profile,
            qos_profile_type=qos_profile_type,
            static_routes=static_routes,
        )

        put_v1_devices_device_id_config_body_edge_circuits_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_circuits_item_value

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
