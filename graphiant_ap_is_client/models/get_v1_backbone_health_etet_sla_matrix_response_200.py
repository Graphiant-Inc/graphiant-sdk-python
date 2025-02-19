from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_devices_item import (
        GetV1BackboneHealthEtetSlaMatrixResponse200DevicesItem,
    )
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item import (
        GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem,
    )
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item import (
        GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtetSlaMatrixResponse200")


@_attrs_define
class GetV1BackboneHealthEtetSlaMatrixResponse200:
    """
    Attributes:
        devices (Union[Unset, list['GetV1BackboneHealthEtetSlaMatrixResponse200DevicesItem']]):
        region_status (Union[Unset, list['GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem']]):
        sla_matrix (Union[Unset, list['GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem']]):
    """

    devices: Union[Unset, list["GetV1BackboneHealthEtetSlaMatrixResponse200DevicesItem"]] = UNSET
    region_status: Union[Unset, list["GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem"]] = UNSET
    sla_matrix: Union[Unset, list["GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        region_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.region_status, Unset):
            region_status = []
            for region_status_item_data in self.region_status:
                region_status_item = region_status_item_data.to_dict()
                region_status.append(region_status_item)

        sla_matrix: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sla_matrix, Unset):
            sla_matrix = []
            for sla_matrix_item_data in self.sla_matrix:
                sla_matrix_item = sla_matrix_item_data.to_dict()
                sla_matrix.append(sla_matrix_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices
        if region_status is not UNSET:
            field_dict["regionStatus"] = region_status
        if sla_matrix is not UNSET:
            field_dict["slaMatrix"] = sla_matrix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_devices_item import (
            GetV1BackboneHealthEtetSlaMatrixResponse200DevicesItem,
        )
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item import (
            GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem,
        )
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item import (
            GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem,
        )

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices", UNSET)
        for devices_item_data in _devices or []:
            devices_item = GetV1BackboneHealthEtetSlaMatrixResponse200DevicesItem.from_dict(devices_item_data)

            devices.append(devices_item)

        region_status = []
        _region_status = d.pop("regionStatus", UNSET)
        for region_status_item_data in _region_status or []:
            region_status_item = GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem.from_dict(
                region_status_item_data
            )

            region_status.append(region_status_item)

        sla_matrix = []
        _sla_matrix = d.pop("slaMatrix", UNSET)
        for sla_matrix_item_data in _sla_matrix or []:
            sla_matrix_item = GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem.from_dict(sla_matrix_item_data)

            sla_matrix.append(sla_matrix_item)

        get_v1_backbone_health_etet_sla_matrix_response_200 = cls(
            devices=devices,
            region_status=region_status,
            sla_matrix=sla_matrix,
        )

        get_v1_backbone_health_etet_sla_matrix_response_200.additional_properties = d
        return get_v1_backbone_health_etet_sla_matrix_response_200

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
