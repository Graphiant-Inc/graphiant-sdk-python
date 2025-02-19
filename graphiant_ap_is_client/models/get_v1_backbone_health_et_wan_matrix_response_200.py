from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item import (
        GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem,
    )
    from ..models.get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item import (
        GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtWanMatrixResponse200")


@_attrs_define
class GetV1BackboneHealthEtWanMatrixResponse200:
    """
    Attributes:
        device_etwan_summary (Union[Unset, list['GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem']]):
        region_sla_status (Union[Unset, list['GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem']]):
    """

    device_etwan_summary: Union[Unset, list["GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem"]] = UNSET
    region_sla_status: Union[Unset, list["GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_etwan_summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_etwan_summary, Unset):
            device_etwan_summary = []
            for device_etwan_summary_item_data in self.device_etwan_summary:
                device_etwan_summary_item = device_etwan_summary_item_data.to_dict()
                device_etwan_summary.append(device_etwan_summary_item)

        region_sla_status: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.region_sla_status, Unset):
            region_sla_status = []
            for region_sla_status_item_data in self.region_sla_status:
                region_sla_status_item = region_sla_status_item_data.to_dict()
                region_sla_status.append(region_sla_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_etwan_summary is not UNSET:
            field_dict["deviceEtwanSummary"] = device_etwan_summary
        if region_sla_status is not UNSET:
            field_dict["regionSlaStatus"] = region_sla_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item import (
            GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem,
        )
        from ..models.get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item import (
            GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem,
        )

        d = src_dict.copy()
        device_etwan_summary = []
        _device_etwan_summary = d.pop("deviceEtwanSummary", UNSET)
        for device_etwan_summary_item_data in _device_etwan_summary or []:
            device_etwan_summary_item = GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem.from_dict(
                device_etwan_summary_item_data
            )

            device_etwan_summary.append(device_etwan_summary_item)

        region_sla_status = []
        _region_sla_status = d.pop("regionSlaStatus", UNSET)
        for region_sla_status_item_data in _region_sla_status or []:
            region_sla_status_item = GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem.from_dict(
                region_sla_status_item_data
            )

            region_sla_status.append(region_sla_status_item)

        get_v1_backbone_health_et_wan_matrix_response_200 = cls(
            device_etwan_summary=device_etwan_summary,
            region_sla_status=region_sla_status,
        )

        get_v1_backbone_health_et_wan_matrix_response_200.additional_properties = d
        return get_v1_backbone_health_et_wan_matrix_response_200

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
