from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_primary_ipv_4_server import (
        GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server,
    )
    from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_primary_ipv_6_server import (
        GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server,
    )
    from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_secondary_ipv_4_server import (
        GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server,
    )
    from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_secondary_ipv_6_server import (
        GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2")


@_attrs_define
class GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2:
    """
    Attributes:
        primary_ipv_4_server (Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server]):
        primary_ipv_6_server (Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server]):
        secondary_ipv_4_server (Union[Unset,
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server]):
        secondary_ipv_6_server (Union[Unset,
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server]):
    """

    primary_ipv_4_server: Union[Unset, "GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server"] = (
        UNSET
    )
    primary_ipv_6_server: Union[Unset, "GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server"] = (
        UNSET
    )
    secondary_ipv_4_server: Union[
        Unset, "GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server"
    ] = UNSET
    secondary_ipv_6_server: Union[
        Unset, "GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_ipv_4_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_ipv_4_server, Unset):
            primary_ipv_4_server = self.primary_ipv_4_server.to_dict()

        primary_ipv_6_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_ipv_6_server, Unset):
            primary_ipv_6_server = self.primary_ipv_6_server.to_dict()

        secondary_ipv_4_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_ipv_4_server, Unset):
            secondary_ipv_4_server = self.secondary_ipv_4_server.to_dict()

        secondary_ipv_6_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_ipv_6_server, Unset):
            secondary_ipv_6_server = self.secondary_ipv_6_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_ipv_4_server is not UNSET:
            field_dict["primaryIpv4Server"] = primary_ipv_4_server
        if primary_ipv_6_server is not UNSET:
            field_dict["primaryIpv6Server"] = primary_ipv_6_server
        if secondary_ipv_4_server is not UNSET:
            field_dict["secondaryIpv4Server"] = secondary_ipv_4_server
        if secondary_ipv_6_server is not UNSET:
            field_dict["secondaryIpv6Server"] = secondary_ipv_6_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_primary_ipv_4_server import (
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server,
        )
        from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_primary_ipv_6_server import (
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server,
        )
        from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_secondary_ipv_4_server import (
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server,
        )
        from ..models.get_v1_devices_device_id_response_200_device_dns_static_servers_v2_secondary_ipv_6_server import (
            GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server,
        )

        d = src_dict.copy()
        _primary_ipv_4_server = d.pop("primaryIpv4Server", UNSET)
        primary_ipv_4_server: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server]
        if isinstance(_primary_ipv_4_server, Unset):
            primary_ipv_4_server = UNSET
        else:
            primary_ipv_4_server = GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv4Server.from_dict(
                _primary_ipv_4_server
            )

        _primary_ipv_6_server = d.pop("primaryIpv6Server", UNSET)
        primary_ipv_6_server: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server]
        if isinstance(_primary_ipv_6_server, Unset):
            primary_ipv_6_server = UNSET
        else:
            primary_ipv_6_server = GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2PrimaryIpv6Server.from_dict(
                _primary_ipv_6_server
            )

        _secondary_ipv_4_server = d.pop("secondaryIpv4Server", UNSET)
        secondary_ipv_4_server: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server]
        if isinstance(_secondary_ipv_4_server, Unset):
            secondary_ipv_4_server = UNSET
        else:
            secondary_ipv_4_server = (
                GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv4Server.from_dict(
                    _secondary_ipv_4_server
                )
            )

        _secondary_ipv_6_server = d.pop("secondaryIpv6Server", UNSET)
        secondary_ipv_6_server: Union[Unset, GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server]
        if isinstance(_secondary_ipv_6_server, Unset):
            secondary_ipv_6_server = UNSET
        else:
            secondary_ipv_6_server = (
                GetV1DevicesDeviceIdResponse200DeviceDnsStaticServersV2SecondaryIpv6Server.from_dict(
                    _secondary_ipv_6_server
                )
            )

        get_v1_devices_device_id_response_200_device_dns_static_servers_v2 = cls(
            primary_ipv_4_server=primary_ipv_4_server,
            primary_ipv_6_server=primary_ipv_6_server,
            secondary_ipv_4_server=secondary_ipv_4_server,
            secondary_ipv_6_server=secondary_ipv_6_server,
        )

        get_v1_devices_device_id_response_200_device_dns_static_servers_v2.additional_properties = d
        return get_v1_devices_device_id_response_200_device_dns_static_servers_v2

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
