from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_versions_version_response_200_config import (
        GetV1DevicesDeviceIdVersionsVersionResponse200Config,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdVersionsVersionResponse200")


@_attrs_define
class GetV1DevicesDeviceIdVersionsVersionResponse200:
    """
    Attributes:
        config (Union[Unset, GetV1DevicesDeviceIdVersionsVersionResponse200Config]):
    """

    config: Union[Unset, "GetV1DevicesDeviceIdVersionsVersionResponse200Config"] = UNSET
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
        from ..models.get_v1_devices_device_id_versions_version_response_200_config import (
            GetV1DevicesDeviceIdVersionsVersionResponse200Config,
        )

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, GetV1DevicesDeviceIdVersionsVersionResponse200Config]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = GetV1DevicesDeviceIdVersionsVersionResponse200Config.from_dict(_config)

        get_v1_devices_device_id_versions_version_response_200 = cls(
            config=config,
        )

        get_v1_devices_device_id_versions_version_response_200.additional_properties = d
        return get_v1_devices_device_id_versions_version_response_200

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
