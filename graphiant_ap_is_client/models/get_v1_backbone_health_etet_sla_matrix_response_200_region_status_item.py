from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item_peer_region import (
        GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion,
    )
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item_region import (
        GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem")


@_attrs_define
class GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItem:
    """
    Attributes:
        peer_region (Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion]):
        region (Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    peer_region: Union[Unset, "GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion"] = UNSET
    region: Union[Unset, "GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peer_region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.peer_region, Unset):
            peer_region = self.peer_region.to_dict()

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peer_region is not UNSET:
            field_dict["peerRegion"] = peer_region
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item_peer_region import (
            GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion,
        )
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item_region import (
            GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion,
        )

        d = src_dict.copy()
        _peer_region = d.pop("peerRegion", UNSET)
        peer_region: Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion]
        if isinstance(_peer_region, Unset):
            peer_region = UNSET
        else:
            peer_region = GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemPeerRegion.from_dict(_peer_region)

        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1BackboneHealthEtetSlaMatrixResponse200RegionStatusItemRegion.from_dict(_region)

        status = d.pop("status", UNSET)

        get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item = cls(
            peer_region=peer_region,
            region=region,
            status=status,
        )

        get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item.additional_properties = d
        return get_v1_backbone_health_etet_sla_matrix_response_200_region_status_item

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
