from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_cloudflare_servers_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsCloudflareServersItem,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_v2 import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_static_servers_item import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersItem,
    )
    from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_static_servers_v2 import (
        GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2,
    )


T = TypeVar("T", bound="GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDns")


@_attrs_define
class GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDns:
    """
    Attributes:
        cloudflare_servers (Union[Unset,
            list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsCloudflareServersItem']]):
        dynamic_servers (Union[Unset,
            list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem']]):
        dynamic_servers_v2 (Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2]):
        mode (Union[Unset, str]):  Example: TYPE_ENUM.
        static_servers (Union[Unset,
            list['GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersItem']]):
        static_servers_v2 (Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2]):
    """

    cloudflare_servers: Union[
        Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsCloudflareServersItem"]
    ] = UNSET
    dynamic_servers: Union[
        Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem"]
    ] = UNSET
    dynamic_servers_v2: Union[Unset, "GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2"] = (
        UNSET
    )
    mode: Union[Unset, str] = UNSET
    static_servers: Union[
        Unset, list["GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersItem"]
    ] = UNSET
    static_servers_v2: Union[Unset, "GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloudflare_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cloudflare_servers, Unset):
            cloudflare_servers = []
            for cloudflare_servers_item_data in self.cloudflare_servers:
                cloudflare_servers_item = cloudflare_servers_item_data.to_dict()
                cloudflare_servers.append(cloudflare_servers_item)

        dynamic_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dynamic_servers, Unset):
            dynamic_servers = []
            for dynamic_servers_item_data in self.dynamic_servers:
                dynamic_servers_item = dynamic_servers_item_data.to_dict()
                dynamic_servers.append(dynamic_servers_item)

        dynamic_servers_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dynamic_servers_v2, Unset):
            dynamic_servers_v2 = self.dynamic_servers_v2.to_dict()

        mode = self.mode

        static_servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_servers, Unset):
            static_servers = []
            for static_servers_item_data in self.static_servers:
                static_servers_item = static_servers_item_data.to_dict()
                static_servers.append(static_servers_item)

        static_servers_v2: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static_servers_v2, Unset):
            static_servers_v2 = self.static_servers_v2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloudflare_servers is not UNSET:
            field_dict["cloudflareServers"] = cloudflare_servers
        if dynamic_servers is not UNSET:
            field_dict["dynamicServers"] = dynamic_servers
        if dynamic_servers_v2 is not UNSET:
            field_dict["dynamicServersV2"] = dynamic_servers_v2
        if mode is not UNSET:
            field_dict["mode"] = mode
        if static_servers is not UNSET:
            field_dict["staticServers"] = static_servers
        if static_servers_v2 is not UNSET:
            field_dict["staticServersV2"] = static_servers_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_cloudflare_servers_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsCloudflareServersItem,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_dynamic_servers_v2 import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_static_servers_item import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersItem,
        )
        from ..models.get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns_static_servers_v2 import (
            GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2,
        )

        d = src_dict.copy()
        cloudflare_servers = []
        _cloudflare_servers = d.pop("cloudflareServers", UNSET)
        for cloudflare_servers_item_data in _cloudflare_servers or []:
            cloudflare_servers_item = (
                GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsCloudflareServersItem.from_dict(
                    cloudflare_servers_item_data
                )
            )

            cloudflare_servers.append(cloudflare_servers_item)

        dynamic_servers = []
        _dynamic_servers = d.pop("dynamicServers", UNSET)
        for dynamic_servers_item_data in _dynamic_servers or []:
            dynamic_servers_item = (
                GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersItem.from_dict(
                    dynamic_servers_item_data
                )
            )

            dynamic_servers.append(dynamic_servers_item)

        _dynamic_servers_v2 = d.pop("dynamicServersV2", UNSET)
        dynamic_servers_v2: Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2]
        if isinstance(_dynamic_servers_v2, Unset):
            dynamic_servers_v2 = UNSET
        else:
            dynamic_servers_v2 = GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsDynamicServersV2.from_dict(
                _dynamic_servers_v2
            )

        mode = d.pop("mode", UNSET)

        static_servers = []
        _static_servers = d.pop("staticServers", UNSET)
        for static_servers_item_data in _static_servers or []:
            static_servers_item = (
                GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersItem.from_dict(
                    static_servers_item_data
                )
            )

            static_servers.append(static_servers_item)

        _static_servers_v2 = d.pop("staticServersV2", UNSET)
        static_servers_v2: Union[Unset, GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2]
        if isinstance(_static_servers_v2, Unset):
            static_servers_v2 = UNSET
        else:
            static_servers_v2 = GetV1EnterpriseEnterpriseIdDevicesResponse200DevicesItemDnsStaticServersV2.from_dict(
                _static_servers_v2
            )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns = cls(
            cloudflare_servers=cloudflare_servers,
            dynamic_servers=dynamic_servers,
            dynamic_servers_v2=dynamic_servers_v2,
            mode=mode,
            static_servers=static_servers,
            static_servers_v2=static_servers_v2,
        )

        get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns.additional_properties = d
        return get_v1_enterprise_enterprise_id_devices_response_200_devices_item_dns

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
