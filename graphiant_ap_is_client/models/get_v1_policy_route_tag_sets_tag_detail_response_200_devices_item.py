from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item_tag import (
        GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag,
    )


T = TypeVar("T", bound="GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem")


@_attrs_define
class GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        location_id (Union[Unset, str]):  Example: TYPE_INT64.
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        tag (Union[Unset, GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag]):
    """

    device_id: Union[Unset, str] = UNSET
    location_id: Union[Unset, str] = UNSET
    site_id: Union[Unset, str] = UNSET
    tag: Union[Unset, "GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        location_id = self.location_id

        site_id = self.site_id

        tag: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tag, Unset):
            tag = self.tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item_tag import (
            GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        location_id = d.pop("locationId", UNSET)

        site_id = d.pop("siteId", UNSET)

        _tag = d.pop("tag", UNSET)
        tag: Union[Unset, GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag]
        if isinstance(_tag, Unset):
            tag = UNSET
        else:
            tag = GetV1PolicyRouteTagSetsTagDetailResponse200DevicesItemTag.from_dict(_tag)

        get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item = cls(
            device_id=device_id,
            location_id=location_id,
            site_id=site_id,
            tag=tag,
        )

        get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item.additional_properties = d
        return get_v1_policy_route_tag_sets_tag_detail_response_200_devices_item

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
