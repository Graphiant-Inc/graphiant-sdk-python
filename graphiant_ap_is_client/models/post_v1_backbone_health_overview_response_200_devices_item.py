from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_overview_response_200_devices_item_region import (
        PostV1BackboneHealthOverviewResponse200DevicesItemRegion,
    )


T = TypeVar("T", bound="PostV1BackboneHealthOverviewResponse200DevicesItem")


@_attrs_define
class PostV1BackboneHealthOverviewResponse200DevicesItem:
    """
    Attributes:
        control_status (Union[Unset, str]):  Example: TYPE_ENUM.
        data_status (Union[Unset, str]):  Example: TYPE_ENUM.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        device_name (Union[Unset, str]):  Example: TYPE_STRING.
        device_role (Union[Unset, str]):  Example: TYPE_ENUM.
        overall_status (Union[Unset, str]):  Example: TYPE_ENUM.
        region (Union[Unset, PostV1BackboneHealthOverviewResponse200DevicesItemRegion]):
        selected_status (Union[Unset, str]):  Example: TYPE_ENUM.
        system_status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    control_status: Union[Unset, str] = UNSET
    data_status: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    device_role: Union[Unset, str] = UNSET
    overall_status: Union[Unset, str] = UNSET
    region: Union[Unset, "PostV1BackboneHealthOverviewResponse200DevicesItemRegion"] = UNSET
    selected_status: Union[Unset, str] = UNSET
    system_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_status = self.control_status

        data_status = self.data_status

        device_id = self.device_id

        device_name = self.device_name

        device_role = self.device_role

        overall_status = self.overall_status

        region: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        selected_status = self.selected_status

        system_status = self.system_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_status is not UNSET:
            field_dict["controlStatus"] = control_status
        if data_status is not UNSET:
            field_dict["dataStatus"] = data_status
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_role is not UNSET:
            field_dict["deviceRole"] = device_role
        if overall_status is not UNSET:
            field_dict["overallStatus"] = overall_status
        if region is not UNSET:
            field_dict["region"] = region
        if selected_status is not UNSET:
            field_dict["selectedStatus"] = selected_status
        if system_status is not UNSET:
            field_dict["systemStatus"] = system_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_overview_response_200_devices_item_region import (
            PostV1BackboneHealthOverviewResponse200DevicesItemRegion,
        )

        d = src_dict.copy()
        control_status = d.pop("controlStatus", UNSET)

        data_status = d.pop("dataStatus", UNSET)

        device_id = d.pop("deviceId", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_role = d.pop("deviceRole", UNSET)

        overall_status = d.pop("overallStatus", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, PostV1BackboneHealthOverviewResponse200DevicesItemRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = PostV1BackboneHealthOverviewResponse200DevicesItemRegion.from_dict(_region)

        selected_status = d.pop("selectedStatus", UNSET)

        system_status = d.pop("systemStatus", UNSET)

        post_v1_backbone_health_overview_response_200_devices_item = cls(
            control_status=control_status,
            data_status=data_status,
            device_id=device_id,
            device_name=device_name,
            device_role=device_role,
            overall_status=overall_status,
            region=region,
            selected_status=selected_status,
            system_status=system_status,
        )

        post_v1_backbone_health_overview_response_200_devices_item.additional_properties = d
        return post_v1_backbone_health_overview_response_200_devices_item

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
