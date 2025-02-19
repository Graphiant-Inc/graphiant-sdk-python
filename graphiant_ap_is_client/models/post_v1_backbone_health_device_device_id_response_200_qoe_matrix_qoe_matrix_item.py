from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_device_region import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion,
    )
    from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_peer_device_region import (
        PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItem:
    """
    Attributes:
        box (Union[Unset, list['PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem']]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_region (Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion]):
        peer_device_id (Union[Unset, str]):  Example: TYPE_INT64.
        peer_device_region (Union[Unset,
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion]):
        session_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    box: Union[Unset, list["PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem"]] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_region: Union[Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion"] = (
        UNSET
    )
    peer_device_id: Union[Unset, str] = UNSET
    peer_device_region: Union[
        Unset, "PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion"
    ] = UNSET
    session_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        box: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.box, Unset):
            box = []
            for box_item_data in self.box:
                box_item = box_item_data.to_dict()
                box.append(box_item)

        device_id = self.device_id

        device_region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.device_region, Unset):
            device_region = self.device_region.to_dict()

        peer_device_id = self.peer_device_id

        peer_device_region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.peer_device_region, Unset):
            peer_device_region = self.peer_device_region.to_dict()

        session_name = self.session_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if box is not UNSET:
            field_dict["box"] = box
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_region is not UNSET:
            field_dict["deviceRegion"] = device_region
        if peer_device_id is not UNSET:
            field_dict["peerDeviceId"] = peer_device_id
        if peer_device_region is not UNSET:
            field_dict["peerDeviceRegion"] = peer_device_region
        if session_name is not UNSET:
            field_dict["sessionName"] = session_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_box_item import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_device_region import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion,
        )
        from ..models.post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item_peer_device_region import (
            PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion,
        )

        d = src_dict.copy()
        box = []
        _box = d.pop("box", UNSET)
        for box_item_data in _box or []:
            box_item = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemBoxItem.from_dict(
                box_item_data
            )

            box.append(box_item)

        device_id = d.pop("deviceId", UNSET)

        _device_region = d.pop("deviceRegion", UNSET)
        device_region: Union[Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion]
        if isinstance(_device_region, Unset):
            device_region = UNSET
        else:
            device_region = PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemDeviceRegion.from_dict(
                _device_region
            )

        peer_device_id = d.pop("peerDeviceId", UNSET)

        _peer_device_region = d.pop("peerDeviceRegion", UNSET)
        peer_device_region: Union[
            Unset, PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion
        ]
        if isinstance(_peer_device_region, Unset):
            peer_device_region = UNSET
        else:
            peer_device_region = (
                PostV1BackboneHealthDeviceDeviceIdResponse200QoeMatrixQoeMatrixItemPeerDeviceRegion.from_dict(
                    _peer_device_region
                )
            )

        session_name = d.pop("sessionName", UNSET)

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item = cls(
            box=box,
            device_id=device_id,
            device_region=device_region,
            peer_device_id=peer_device_id,
            peer_device_region=peer_device_region,
            session_name=session_name,
        )

        post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_qoe_matrix_qoe_matrix_item

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
