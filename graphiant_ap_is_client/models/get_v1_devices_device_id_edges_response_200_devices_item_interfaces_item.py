from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_config_updated_at import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_4 import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_6 import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_6_addresses_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6AddressesItem,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_oper_updated_at import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_sfp_optical_strength_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_subinterfaces_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSubinterfacesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItem")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItem:
    """
    Attributes:
        alias (Union[Unset, str]):  Example: TYPE_STRING.
        circuit (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        config_updated_at (Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt]):
        configured_max_transmission_unit (Union[Unset, str]):  Example: TYPE_UINT32.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        duplex (Union[Unset, str]):  Example: TYPE_STRING.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_sec (Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec]):
        ipv4 (Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4]):
        ipv6 (Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6]):
        ipv_6_addresses (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6AddressesItem']]):
        lan (Union[Unset, str]):  Example: TYPE_STRING.
        lldp_enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        max_transmission_unit (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        oper_updated_at (Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt]):
        phy_address (Union[Unset, str]):  Example: TYPE_STRING.
        security_zone (Union[Unset, str]):  Example: TYPE_STRING.
        sfp_optical_strength (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem']]):
        speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        subinterfaces (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSubinterfacesItem']]):
        tcp_mss (Union[Unset, str]):  Example: TYPE_UINT32.
        tcp_mss_v4 (Union[Unset, str]):  Example: TYPE_UINT32.
        tcp_mss_v6 (Union[Unset, str]):  Example: TYPE_UINT32.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
        up (Union[Unset, str]):  Example: TYPE_BOOL.
        vrf_function_id (Union[Unset, str]):  Example: TYPE_UINT32.
        vrf_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    alias: Union[Unset, str] = UNSET
    circuit: Union[Unset, str] = UNSET
    circuit_name: Union[Unset, str] = UNSET
    config_updated_at: Union[Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt"] = (
        UNSET
    )
    configured_max_transmission_unit: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    duplex: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_sec: Union[Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec"] = UNSET
    ipv4: Union[Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4"] = UNSET
    ipv6: Union[Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6"] = UNSET
    ipv_6_addresses: Union[
        Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6AddressesItem"]
    ] = UNSET
    lan: Union[Unset, str] = UNSET
    lldp_enabled: Union[Unset, str] = UNSET
    max_transmission_unit: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    oper_updated_at: Union[Unset, "GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt"] = UNSET
    phy_address: Union[Unset, str] = UNSET
    security_zone: Union[Unset, str] = UNSET
    sfp_optical_strength: Union[
        Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem"]
    ] = UNSET
    speed_mbps: Union[Unset, str] = UNSET
    subinterfaces: Union[
        Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSubinterfacesItem"]
    ] = UNSET
    tcp_mss: Union[Unset, str] = UNSET
    tcp_mss_v4: Union[Unset, str] = UNSET
    tcp_mss_v6: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    up: Union[Unset, str] = UNSET
    vrf_function_id: Union[Unset, str] = UNSET
    vrf_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        circuit = self.circuit

        circuit_name = self.circuit_name

        config_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config_updated_at, Unset):
            config_updated_at = self.config_updated_at.to_dict()

        configured_max_transmission_unit = self.configured_max_transmission_unit

        description = self.description

        duplex = self.duplex

        enabled = self.enabled

        id = self.id

        ip_sec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ip_sec, Unset):
            ip_sec = self.ip_sec.to_dict()

        ipv4: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipv4, Unset):
            ipv4 = self.ipv4.to_dict()

        ipv6: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6.to_dict()

        ipv_6_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipv_6_addresses, Unset):
            ipv_6_addresses = []
            for ipv_6_addresses_item_data in self.ipv_6_addresses:
                ipv_6_addresses_item = ipv_6_addresses_item_data.to_dict()
                ipv_6_addresses.append(ipv_6_addresses_item)

        lan = self.lan

        lldp_enabled = self.lldp_enabled

        max_transmission_unit = self.max_transmission_unit

        name = self.name

        oper_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oper_updated_at, Unset):
            oper_updated_at = self.oper_updated_at.to_dict()

        phy_address = self.phy_address

        security_zone = self.security_zone

        sfp_optical_strength: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sfp_optical_strength, Unset):
            sfp_optical_strength = []
            for sfp_optical_strength_item_data in self.sfp_optical_strength:
                sfp_optical_strength_item = sfp_optical_strength_item_data.to_dict()
                sfp_optical_strength.append(sfp_optical_strength_item)

        speed_mbps = self.speed_mbps

        subinterfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.subinterfaces, Unset):
            subinterfaces = []
            for subinterfaces_item_data in self.subinterfaces:
                subinterfaces_item = subinterfaces_item_data.to_dict()
                subinterfaces.append(subinterfaces_item)

        tcp_mss = self.tcp_mss

        tcp_mss_v4 = self.tcp_mss_v4

        tcp_mss_v6 = self.tcp_mss_v6

        type_ = self.type_

        up = self.up

        vrf_function_id = self.vrf_function_id

        vrf_name = self.vrf_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if config_updated_at is not UNSET:
            field_dict["configUpdatedAt"] = config_updated_at
        if configured_max_transmission_unit is not UNSET:
            field_dict["configuredMaxTransmissionUnit"] = configured_max_transmission_unit
        if description is not UNSET:
            field_dict["description"] = description
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if ip_sec is not UNSET:
            field_dict["ipSec"] = ip_sec
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if lan is not UNSET:
            field_dict["lan"] = lan
        if lldp_enabled is not UNSET:
            field_dict["lldpEnabled"] = lldp_enabled
        if max_transmission_unit is not UNSET:
            field_dict["maxTransmissionUnit"] = max_transmission_unit
        if name is not UNSET:
            field_dict["name"] = name
        if oper_updated_at is not UNSET:
            field_dict["operUpdatedAt"] = oper_updated_at
        if phy_address is not UNSET:
            field_dict["phyAddress"] = phy_address
        if security_zone is not UNSET:
            field_dict["securityZone"] = security_zone
        if sfp_optical_strength is not UNSET:
            field_dict["sfpOpticalStrength"] = sfp_optical_strength
        if speed_mbps is not UNSET:
            field_dict["speedMbps"] = speed_mbps
        if subinterfaces is not UNSET:
            field_dict["subinterfaces"] = subinterfaces
        if tcp_mss is not UNSET:
            field_dict["tcpMss"] = tcp_mss
        if tcp_mss_v4 is not UNSET:
            field_dict["tcpMssV4"] = tcp_mss_v4
        if tcp_mss_v6 is not UNSET:
            field_dict["tcpMssV6"] = tcp_mss_v6
        if type_ is not UNSET:
            field_dict["type"] = type_
        if up is not UNSET:
            field_dict["up"] = up
        if vrf_function_id is not UNSET:
            field_dict["vrfFunctionId"] = vrf_function_id
        if vrf_name is not UNSET:
            field_dict["vrfName"] = vrf_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_config_updated_at import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ip_sec import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_4 import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_6 import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_ipv_6_addresses_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6AddressesItem,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_oper_updated_at import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_sfp_optical_strength_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item_subinterfaces_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSubinterfacesItem,
        )

        d = src_dict.copy()
        alias = d.pop("alias", UNSET)

        circuit = d.pop("circuit", UNSET)

        circuit_name = d.pop("circuitName", UNSET)

        _config_updated_at = d.pop("configUpdatedAt", UNSET)
        config_updated_at: Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt]
        if isinstance(_config_updated_at, Unset):
            config_updated_at = UNSET
        else:
            config_updated_at = GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemConfigUpdatedAt.from_dict(
                _config_updated_at
            )

        configured_max_transmission_unit = d.pop("configuredMaxTransmissionUnit", UNSET)

        description = d.pop("description", UNSET)

        duplex = d.pop("duplex", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _ip_sec = d.pop("ipSec", UNSET)
        ip_sec: Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec]
        if isinstance(_ip_sec, Unset):
            ip_sec = UNSET
        else:
            ip_sec = GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpSec.from_dict(_ip_sec)

        _ipv4 = d.pop("ipv4", UNSET)
        ipv4: Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4]
        if isinstance(_ipv4, Unset):
            ipv4 = UNSET
        else:
            ipv4 = GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv4.from_dict(_ipv4)

        _ipv6 = d.pop("ipv6", UNSET)
        ipv6: Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6]
        if isinstance(_ipv6, Unset):
            ipv6 = UNSET
        else:
            ipv6 = GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6.from_dict(_ipv6)

        ipv_6_addresses = []
        _ipv_6_addresses = d.pop("ipv6Addresses", UNSET)
        for ipv_6_addresses_item_data in _ipv_6_addresses or []:
            ipv_6_addresses_item = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemIpv6AddressesItem.from_dict(
                    ipv_6_addresses_item_data
                )
            )

            ipv_6_addresses.append(ipv_6_addresses_item)

        lan = d.pop("lan", UNSET)

        lldp_enabled = d.pop("lldpEnabled", UNSET)

        max_transmission_unit = d.pop("maxTransmissionUnit", UNSET)

        name = d.pop("name", UNSET)

        _oper_updated_at = d.pop("operUpdatedAt", UNSET)
        oper_updated_at: Union[Unset, GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt]
        if isinstance(_oper_updated_at, Unset):
            oper_updated_at = UNSET
        else:
            oper_updated_at = GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemOperUpdatedAt.from_dict(
                _oper_updated_at
            )

        phy_address = d.pop("phyAddress", UNSET)

        security_zone = d.pop("securityZone", UNSET)

        sfp_optical_strength = []
        _sfp_optical_strength = d.pop("sfpOpticalStrength", UNSET)
        for sfp_optical_strength_item_data in _sfp_optical_strength or []:
            sfp_optical_strength_item = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSfpOpticalStrengthItem.from_dict(
                    sfp_optical_strength_item_data
                )
            )

            sfp_optical_strength.append(sfp_optical_strength_item)

        speed_mbps = d.pop("speedMbps", UNSET)

        subinterfaces = []
        _subinterfaces = d.pop("subinterfaces", UNSET)
        for subinterfaces_item_data in _subinterfaces or []:
            subinterfaces_item = (
                GetV1DevicesDeviceIdEdgesResponse200DevicesItemInterfacesItemSubinterfacesItem.from_dict(
                    subinterfaces_item_data
                )
            )

            subinterfaces.append(subinterfaces_item)

        tcp_mss = d.pop("tcpMss", UNSET)

        tcp_mss_v4 = d.pop("tcpMssV4", UNSET)

        tcp_mss_v6 = d.pop("tcpMssV6", UNSET)

        type_ = d.pop("type", UNSET)

        up = d.pop("up", UNSET)

        vrf_function_id = d.pop("vrfFunctionId", UNSET)

        vrf_name = d.pop("vrfName", UNSET)

        get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item = cls(
            alias=alias,
            circuit=circuit,
            circuit_name=circuit_name,
            config_updated_at=config_updated_at,
            configured_max_transmission_unit=configured_max_transmission_unit,
            description=description,
            duplex=duplex,
            enabled=enabled,
            id=id,
            ip_sec=ip_sec,
            ipv4=ipv4,
            ipv6=ipv6,
            ipv_6_addresses=ipv_6_addresses,
            lan=lan,
            lldp_enabled=lldp_enabled,
            max_transmission_unit=max_transmission_unit,
            name=name,
            oper_updated_at=oper_updated_at,
            phy_address=phy_address,
            security_zone=security_zone,
            sfp_optical_strength=sfp_optical_strength,
            speed_mbps=speed_mbps,
            subinterfaces=subinterfaces,
            tcp_mss=tcp_mss,
            tcp_mss_v4=tcp_mss_v4,
            tcp_mss_v6=tcp_mss_v6,
            type_=type_,
            up=up,
            vrf_function_id=vrf_function_id,
            vrf_name=vrf_name,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_interfaces_item

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
