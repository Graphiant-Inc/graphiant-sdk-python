from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters_export_policy import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy,
    )
    from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters_import_policy import (
        PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFilters:
    """
    Attributes:
        export_policy (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy]):
        import_policy (Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy]):
    """

    export_policy: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy"] = UNSET
    import_policy: Union[Unset, "PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.export_policy, Unset):
            export_policy = self.export_policy.to_dict()

        import_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.import_policy, Unset):
            import_policy = self.import_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_policy is not UNSET:
            field_dict["exportPolicy"] = export_policy
        if import_policy is not UNSET:
            field_dict["importPolicy"] = import_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters_export_policy import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy,
        )
        from ..models.put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters_import_policy import (
            PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy,
        )

        d = src_dict.copy()
        _export_policy = d.pop("exportPolicy", UNSET)
        export_policy: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy]
        if isinstance(_export_policy, Unset):
            export_policy = UNSET
        else:
            export_policy = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersExportPolicy.from_dict(
                _export_policy
            )

        _import_policy = d.pop("importPolicy", UNSET)
        import_policy: Union[Unset, PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy]
        if isinstance(_import_policy, Unset):
            import_policy = UNSET
        else:
            import_policy = PutV1DevicesDeviceIdConfigBodyCoreCoreVrfOverlayFiltersImportPolicy.from_dict(
                _import_policy
            )

        put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters = cls(
            export_policy=export_policy,
            import_policy=import_policy,
        )

        put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters.additional_properties = d
        return put_v1_devices_device_id_config_body_core_core_vrf_overlay_filters

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
