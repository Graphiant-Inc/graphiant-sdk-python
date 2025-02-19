from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion:
    """
    Attributes:
        region_id (Union[Unset, str]):  Example: TYPE_INT32.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region_id = self.region_id

        region_name = self.region_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_peer_device_region = cls(
            region_id=region_id,
            region_name=region_name,
        )

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_peer_device_region.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_peer_device_region

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
