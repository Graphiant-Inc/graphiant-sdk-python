from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_prometheus_sink_sink import (
        PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCorePrometheusSink")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCorePrometheusSink:
    """
    Attributes:
        sink (Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink]):
    """

    sink: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sink: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sink, Unset):
            sink = self.sink.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sink is not UNSET:
            field_dict["sink"] = sink

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_prometheus_sink_sink import (
            PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink,
        )

        d = src_dict.copy()
        _sink = d.pop("sink", UNSET)
        sink: Union[Unset, PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink]
        if isinstance(_sink, Unset):
            sink = UNSET
        else:
            sink = PutV1DevicesDeviceIdConfigBodyCorePrometheusSinkSink.from_dict(_sink)

        put_v1_devices_device_id_config_body_core_prometheus_sink = cls(
            sink=sink,
        )

        put_v1_devices_device_id_config_body_core_prometheus_sink.additional_properties = d
        return put_v1_devices_device_id_config_body_core_prometheus_sink

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
