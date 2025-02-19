from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item_region import (
        GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem")


@_attrs_define
class GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        provider (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    region: Union[Unset, "GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        device_name = self.device_name

        provider = self.provider

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item_region import (
            GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        provider = d.pop("provider", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1BackboneHealthEtWanMatrixResponse200DeviceEtwanSummaryItemRegion.from_dict(_region)

        status = d.pop("status", UNSET)

        get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item = cls(
            device_id=device_id,
            device_name=device_name,
            provider=provider,
            region=region,
            status=status,
        )

        get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item.additional_properties = d
        return get_v1_backbone_health_et_wan_matrix_response_200_device_etwan_summary_item

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
