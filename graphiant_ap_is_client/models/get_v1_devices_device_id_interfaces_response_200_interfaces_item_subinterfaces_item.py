from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_config_updated_at import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt,
    )
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_4 import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4,
    )
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_6 import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6,
    )
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_6_addresses_item import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6AddressesItem,
    )
    from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_oper_updated_at import (
        GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItem")


@_attrs_define
class GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItem:
    """
    Attributes:
        alias (Union[Unset, str]):  Example: TYPE_STRING.
        circuit (Union[Unset, str]):  Example: TYPE_STRING.
        config_updated_at (Union[Unset,
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        duplex (Union[Unset, str]):  Example: TYPE_STRING.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ipv4 (Union[Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4]):
        ipv6 (Union[Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6]):
        ipv_6_addresses (Union[Unset,
            list['GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6AddressesItem']]):
        lan (Union[Unset, str]):  Example: TYPE_STRING.
        mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        max_transmission_unit (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        oper_updated_at (Union[Unset,
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt]):
        parent_mac_address (Union[Unset, str]):  Example: TYPE_STRING.
        security_zone (Union[Unset, str]):  Example: TYPE_STRING.
        speed_mbps (Union[Unset, str]):  Example: TYPE_UINT32.
        tcp_mss (Union[Unset, str]):  Example: TYPE_UINT32.
        tcp_mss_v4 (Union[Unset, str]):  Example: TYPE_UINT32.
        tcp_mss_v6 (Union[Unset, str]):  Example: TYPE_UINT32.
        up (Union[Unset, str]):  Example: TYPE_BOOL.
        vlan (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    alias: Union[Unset, str] = UNSET
    circuit: Union[Unset, str] = UNSET
    config_updated_at: Union[
        Unset, "GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt"
    ] = UNSET
    description: Union[Unset, str] = UNSET
    duplex: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ipv4: Union[Unset, "GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4"] = UNSET
    ipv6: Union[Unset, "GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6"] = UNSET
    ipv_6_addresses: Union[
        Unset, list["GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6AddressesItem"]
    ] = UNSET
    lan: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    max_transmission_unit: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    oper_updated_at: Union[
        Unset, "GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt"
    ] = UNSET
    parent_mac_address: Union[Unset, str] = UNSET
    security_zone: Union[Unset, str] = UNSET
    speed_mbps: Union[Unset, str] = UNSET
    tcp_mss: Union[Unset, str] = UNSET
    tcp_mss_v4: Union[Unset, str] = UNSET
    tcp_mss_v6: Union[Unset, str] = UNSET
    up: Union[Unset, str] = UNSET
    vlan: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        circuit = self.circuit

        config_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config_updated_at, Unset):
            config_updated_at = self.config_updated_at.to_dict()

        description = self.description

        duplex = self.duplex

        enabled = self.enabled

        id = self.id

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

        mac_address = self.mac_address

        max_transmission_unit = self.max_transmission_unit

        name = self.name

        oper_updated_at: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oper_updated_at, Unset):
            oper_updated_at = self.oper_updated_at.to_dict()

        parent_mac_address = self.parent_mac_address

        security_zone = self.security_zone

        speed_mbps = self.speed_mbps

        tcp_mss = self.tcp_mss

        tcp_mss_v4 = self.tcp_mss_v4

        tcp_mss_v6 = self.tcp_mss_v6

        up = self.up

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
        if config_updated_at is not UNSET:
            field_dict["configUpdatedAt"] = config_updated_at
        if description is not UNSET:
            field_dict["description"] = description
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if ipv4 is not UNSET:
            field_dict["ipv4"] = ipv4
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if ipv_6_addresses is not UNSET:
            field_dict["ipv6Addresses"] = ipv_6_addresses
        if lan is not UNSET:
            field_dict["lan"] = lan
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if max_transmission_unit is not UNSET:
            field_dict["maxTransmissionUnit"] = max_transmission_unit
        if name is not UNSET:
            field_dict["name"] = name
        if oper_updated_at is not UNSET:
            field_dict["operUpdatedAt"] = oper_updated_at
        if parent_mac_address is not UNSET:
            field_dict["parentMacAddress"] = parent_mac_address
        if security_zone is not UNSET:
            field_dict["securityZone"] = security_zone
        if speed_mbps is not UNSET:
            field_dict["speedMbps"] = speed_mbps
        if tcp_mss is not UNSET:
            field_dict["tcpMss"] = tcp_mss
        if tcp_mss_v4 is not UNSET:
            field_dict["tcpMssV4"] = tcp_mss_v4
        if tcp_mss_v6 is not UNSET:
            field_dict["tcpMssV6"] = tcp_mss_v6
        if up is not UNSET:
            field_dict["up"] = up
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_config_updated_at import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt,
        )
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_4 import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4,
        )
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_6 import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6,
        )
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_ipv_6_addresses_item import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6AddressesItem,
        )
        from ..models.get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item_oper_updated_at import (
            GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt,
        )

        d = src_dict.copy()
        alias = d.pop("alias", UNSET)

        circuit = d.pop("circuit", UNSET)

        _config_updated_at = d.pop("configUpdatedAt", UNSET)
        config_updated_at: Union[
            Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt
        ]
        if isinstance(_config_updated_at, Unset):
            config_updated_at = UNSET
        else:
            config_updated_at = (
                GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemConfigUpdatedAt.from_dict(
                    _config_updated_at
                )
            )

        description = d.pop("description", UNSET)

        duplex = d.pop("duplex", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _ipv4 = d.pop("ipv4", UNSET)
        ipv4: Union[Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4]
        if isinstance(_ipv4, Unset):
            ipv4 = UNSET
        else:
            ipv4 = GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv4.from_dict(_ipv4)

        _ipv6 = d.pop("ipv6", UNSET)
        ipv6: Union[Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6]
        if isinstance(_ipv6, Unset):
            ipv6 = UNSET
        else:
            ipv6 = GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6.from_dict(_ipv6)

        ipv_6_addresses = []
        _ipv_6_addresses = d.pop("ipv6Addresses", UNSET)
        for ipv_6_addresses_item_data in _ipv_6_addresses or []:
            ipv_6_addresses_item = (
                GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemIpv6AddressesItem.from_dict(
                    ipv_6_addresses_item_data
                )
            )

            ipv_6_addresses.append(ipv_6_addresses_item)

        lan = d.pop("lan", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        max_transmission_unit = d.pop("maxTransmissionUnit", UNSET)

        name = d.pop("name", UNSET)

        _oper_updated_at = d.pop("operUpdatedAt", UNSET)
        oper_updated_at: Union[
            Unset, GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt
        ]
        if isinstance(_oper_updated_at, Unset):
            oper_updated_at = UNSET
        else:
            oper_updated_at = (
                GetV1DevicesDeviceIdInterfacesResponse200InterfacesItemSubinterfacesItemOperUpdatedAt.from_dict(
                    _oper_updated_at
                )
            )

        parent_mac_address = d.pop("parentMacAddress", UNSET)

        security_zone = d.pop("securityZone", UNSET)

        speed_mbps = d.pop("speedMbps", UNSET)

        tcp_mss = d.pop("tcpMss", UNSET)

        tcp_mss_v4 = d.pop("tcpMssV4", UNSET)

        tcp_mss_v6 = d.pop("tcpMssV6", UNSET)

        up = d.pop("up", UNSET)

        vlan = d.pop("vlan", UNSET)

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item = cls(
            alias=alias,
            circuit=circuit,
            config_updated_at=config_updated_at,
            description=description,
            duplex=duplex,
            enabled=enabled,
            id=id,
            ipv4=ipv4,
            ipv6=ipv6,
            ipv_6_addresses=ipv_6_addresses,
            lan=lan,
            mac_address=mac_address,
            max_transmission_unit=max_transmission_unit,
            name=name,
            oper_updated_at=oper_updated_at,
            parent_mac_address=parent_mac_address,
            security_zone=security_zone,
            speed_mbps=speed_mbps,
            tcp_mss=tcp_mss,
            tcp_mss_v4=tcp_mss_v4,
            tcp_mss_v6=tcp_mss_v6,
            up=up,
            vlan=vlan,
        )

        get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item.additional_properties = d
        return get_v1_devices_device_id_interfaces_response_200_interfaces_item_subinterfaces_item

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
