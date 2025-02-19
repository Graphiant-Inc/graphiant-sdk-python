from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item_peer_region import (
        GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion,
    )
    from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item_region import (
        GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion,
    )


T = TypeVar("T", bound="GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem")


@_attrs_define
class GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItem:
    """
    Attributes:
        delay_status (Union[Unset, str]):  Example: TYPE_ENUM.
        delay_value (Union[Unset, str]):  Example: TYPE_FLOAT.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        jitter_status (Union[Unset, str]):  Example: TYPE_ENUM.
        jitter_value (Union[Unset, str]):  Example: TYPE_FLOAT.
        loss_status (Union[Unset, str]):  Example: TYPE_ENUM.
        loss_value (Union[Unset, str]):  Example: TYPE_FLOAT.
        mos_value (Union[Unset, str]):  Example: TYPE_FLOAT.
        peer_device_id (Union[Unset, str]):  Example: TYPE_INT64.
        peer_device_name (Union[Unset, str]):  Example: TYPE_STRING.
        peer_region (Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion]):
        region (Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    delay_status: Union[Unset, str] = UNSET
    delay_value: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    jitter_status: Union[Unset, str] = UNSET
    jitter_value: Union[Unset, str] = UNSET
    loss_status: Union[Unset, str] = UNSET
    loss_value: Union[Unset, str] = UNSET
    mos_value: Union[Unset, str] = UNSET
    peer_device_id: Union[Unset, str] = UNSET
    peer_device_name: Union[Unset, str] = UNSET
    peer_region: Union[Unset, "GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion"] = UNSET
    region: Union[Unset, "GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion"] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_status = self.delay_status

        delay_value = self.delay_value

        device_id = self.device_id

        device_name = self.device_name

        jitter_status = self.jitter_status

        jitter_value = self.jitter_value

        loss_status = self.loss_status

        loss_value = self.loss_value

        mos_value = self.mos_value

        peer_device_id = self.peer_device_id

        peer_device_name = self.peer_device_name

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
        if delay_status is not UNSET:
            field_dict["delayStatus"] = delay_status
        if delay_value is not UNSET:
            field_dict["delayValue"] = delay_value
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if jitter_status is not UNSET:
            field_dict["jitterStatus"] = jitter_status
        if jitter_value is not UNSET:
            field_dict["jitterValue"] = jitter_value
        if loss_status is not UNSET:
            field_dict["lossStatus"] = loss_status
        if loss_value is not UNSET:
            field_dict["lossValue"] = loss_value
        if mos_value is not UNSET:
            field_dict["mosValue"] = mos_value
        if peer_device_id is not UNSET:
            field_dict["peerDeviceId"] = peer_device_id
        if peer_device_name is not UNSET:
            field_dict["peerDeviceName"] = peer_device_name
        if peer_region is not UNSET:
            field_dict["peerRegion"] = peer_region
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item_peer_region import (
            GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion,
        )
        from ..models.get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item_region import (
            GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion,
        )

        d = src_dict.copy()
        delay_status = d.pop("delayStatus", UNSET)

        delay_value = d.pop("delayValue", UNSET)

        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        jitter_status = d.pop("jitterStatus", UNSET)

        jitter_value = d.pop("jitterValue", UNSET)

        loss_status = d.pop("lossStatus", UNSET)

        loss_value = d.pop("lossValue", UNSET)

        mos_value = d.pop("mosValue", UNSET)

        peer_device_id = d.pop("peerDeviceId", UNSET)

        peer_device_name = d.pop("peerDeviceName", UNSET)

        _peer_region = d.pop("peerRegion", UNSET)
        peer_region: Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion]
        if isinstance(_peer_region, Unset):
            peer_region = UNSET
        else:
            peer_region = GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemPeerRegion.from_dict(_peer_region)

        _region = d.pop("region", UNSET)
        region: Union[Unset, GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetV1BackboneHealthEtetSlaMatrixResponse200SlaMatrixItemRegion.from_dict(_region)

        status = d.pop("status", UNSET)

        get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item = cls(
            delay_status=delay_status,
            delay_value=delay_value,
            device_id=device_id,
            device_name=device_name,
            jitter_status=jitter_status,
            jitter_value=jitter_value,
            loss_status=loss_status,
            loss_value=loss_value,
            mos_value=mos_value,
            peer_device_id=peer_device_id,
            peer_device_name=peer_device_name,
            peer_region=peer_region,
            region=region,
            status=status,
        )

        get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item.additional_properties = d
        return get_v1_backbone_health_etet_sla_matrix_response_200_sla_matrix_item

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
