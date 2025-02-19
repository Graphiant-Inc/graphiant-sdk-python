from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_configuration_metadata import (
        PutV1DevicesDeviceIdConfigBodyConfigurationMetadata,
    )
    from ..models.put_v1_devices_device_id_config_body_core import PutV1DevicesDeviceIdConfigBodyCore
    from ..models.put_v1_devices_device_id_config_body_edge import PutV1DevicesDeviceIdConfigBodyEdge


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBody")


@_attrs_define
class PutV1DevicesDeviceIdConfigBody:
    """
    Attributes:
        configuration_metadata (Union[Unset, PutV1DevicesDeviceIdConfigBodyConfigurationMetadata]):
        core (Union[Unset, PutV1DevicesDeviceIdConfigBodyCore]):
        description (Union[Unset, str]):  Example: TYPE_STRING.
        edge (Union[Unset, PutV1DevicesDeviceIdConfigBodyEdge]):
        local_web_server_password (Union[Unset, str]):  Example: TYPE_STRING.
        replace (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    configuration_metadata: Union[Unset, "PutV1DevicesDeviceIdConfigBodyConfigurationMetadata"] = UNSET
    core: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCore"] = UNSET
    description: Union[Unset, str] = UNSET
    edge: Union[Unset, "PutV1DevicesDeviceIdConfigBodyEdge"] = UNSET
    local_web_server_password: Union[Unset, str] = UNSET
    replace: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration_metadata, Unset):
            configuration_metadata = self.configuration_metadata.to_dict()

        core: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.core, Unset):
            core = self.core.to_dict()

        description = self.description

        edge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edge, Unset):
            edge = self.edge.to_dict()

        local_web_server_password = self.local_web_server_password

        replace = self.replace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_metadata is not UNSET:
            field_dict["configurationMetadata"] = configuration_metadata
        if core is not UNSET:
            field_dict["core"] = core
        if description is not UNSET:
            field_dict["description"] = description
        if edge is not UNSET:
            field_dict["edge"] = edge
        if local_web_server_password is not UNSET:
            field_dict["localWebServerPassword"] = local_web_server_password
        if replace is not UNSET:
            field_dict["replace"] = replace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_configuration_metadata import (
            PutV1DevicesDeviceIdConfigBodyConfigurationMetadata,
        )
        from ..models.put_v1_devices_device_id_config_body_core import PutV1DevicesDeviceIdConfigBodyCore
        from ..models.put_v1_devices_device_id_config_body_edge import PutV1DevicesDeviceIdConfigBodyEdge

        d = src_dict.copy()
        _configuration_metadata = d.pop("configurationMetadata", UNSET)
        configuration_metadata: Union[Unset, PutV1DevicesDeviceIdConfigBodyConfigurationMetadata]
        if isinstance(_configuration_metadata, Unset):
            configuration_metadata = UNSET
        else:
            configuration_metadata = PutV1DevicesDeviceIdConfigBodyConfigurationMetadata.from_dict(
                _configuration_metadata
            )

        _core = d.pop("core", UNSET)
        core: Union[Unset, PutV1DevicesDeviceIdConfigBodyCore]
        if isinstance(_core, Unset):
            core = UNSET
        else:
            core = PutV1DevicesDeviceIdConfigBodyCore.from_dict(_core)

        description = d.pop("description", UNSET)

        _edge = d.pop("edge", UNSET)
        edge: Union[Unset, PutV1DevicesDeviceIdConfigBodyEdge]
        if isinstance(_edge, Unset):
            edge = UNSET
        else:
            edge = PutV1DevicesDeviceIdConfigBodyEdge.from_dict(_edge)

        local_web_server_password = d.pop("localWebServerPassword", UNSET)

        replace = d.pop("replace", UNSET)

        put_v1_devices_device_id_config_body = cls(
            configuration_metadata=configuration_metadata,
            core=core,
            description=description,
            edge=edge,
            local_web_server_password=local_web_server_password,
            replace=replace,
        )

        put_v1_devices_device_id_config_body.additional_properties = d
        return put_v1_devices_device_id_config_body

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
