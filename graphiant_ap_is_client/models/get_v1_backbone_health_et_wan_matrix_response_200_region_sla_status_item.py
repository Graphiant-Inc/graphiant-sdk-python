from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item_region import (
        GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem")


@_attrs_define
class GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItem:
    """
    Attributes:
        region (Union[Unset, GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    region: Union[Unset, "GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item_region import (
            GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion,
        )

        d = src_dict.copy()
        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1BackboneHealthEtWanMatrixResponse200RegionSlaStatusItemRegion.from_dict(_region)

        status = d.pop("status", UNSET)

        get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item = cls(
            region=region,
            status=status,
        )

        get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item.additional_properties = d
        return get_v1_backbone_health_et_wan_matrix_response_200_region_sla_status_item

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
