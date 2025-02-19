from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_cloudflare import (
        PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_dynamic import (
        PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic,
    )
    from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_static import (
        PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeDnsDns")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeDnsDns:
    """
    Attributes:
        cloudflare (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare]):
        dynamic (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic]):
        static (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic]):
    """

    cloudflare: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare"] = UNSET
    dynamic: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic"] = UNSET
    static: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloudflare: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloudflare, Unset):
            cloudflare = self.cloudflare.to_dict()

        dynamic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dynamic, Unset):
            dynamic = self.dynamic.to_dict()

        static: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.static, Unset):
            static = self.static.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloudflare is not UNSET:
            field_dict["cloudflare"] = cloudflare
        if dynamic is not UNSET:
            field_dict["dynamic"] = dynamic
        if static is not UNSET:
            field_dict["static"] = static

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_cloudflare import (
            PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_dynamic import (
            PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic,
        )
        from ..models.put_v1_devices_device_id_config_body_edge_dns_dns_static import (
            PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic,
        )

        d = src_dict.copy()
        _cloudflare = d.pop("cloudflare", UNSET)
        cloudflare: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare]
        if isinstance(_cloudflare, Unset):
            cloudflare = UNSET
        else:
            cloudflare = PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsCloudflare.from_dict(_cloudflare)

        _dynamic = d.pop("dynamic", UNSET)
        dynamic: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic]
        if isinstance(_dynamic, Unset):
            dynamic = UNSET
        else:
            dynamic = PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsDynamic.from_dict(_dynamic)

        _static = d.pop("static", UNSET)
        static: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic]
        if isinstance(_static, Unset):
            static = UNSET
        else:
            static = PutV1DevicesDeviceIdConfigBodyEdgeDnsDnsStatic.from_dict(_static)

        put_v1_devices_device_id_config_body_edge_dns_dns = cls(
            cloudflare=cloudflare,
            dynamic=dynamic,
            static=static,
        )

        put_v1_devices_device_id_config_body_edge_dns_dns.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_dns_dns

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
