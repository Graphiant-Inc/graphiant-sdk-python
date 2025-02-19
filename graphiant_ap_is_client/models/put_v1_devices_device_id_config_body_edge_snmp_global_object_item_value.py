from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_snmp_global_object_item_value_config import (
        PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValue")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValue:
    """
    Attributes:
        config (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig]):
    """

    config: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_snmp_global_object_item_value_config import (
            PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig,
        )

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PutV1DevicesDeviceIdConfigBodyEdgeSnmpGlobalObjectItemValueConfig.from_dict(_config)

        put_v1_devices_device_id_config_body_edge_snmp_global_object_item_value = cls(
            config=config,
        )

        put_v1_devices_device_id_config_body_edge_snmp_global_object_item_value.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_snmp_global_object_item_value

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
