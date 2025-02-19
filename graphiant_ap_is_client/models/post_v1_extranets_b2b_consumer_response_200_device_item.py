from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_consumer_response_200_device_item_last_updated import (
        PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerResponse200DeviceItem")


@_attrs_define
class PostV1ExtranetsB2BConsumerResponse200DeviceItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        last_updated (Union[Unset, PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated]):
        site (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    last_updated: Union[Unset, "PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated"] = UNSET
    site: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        last_updated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.to_dict()

        site = self.site

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if site is not UNSET:
            field_dict["site"] = site
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_consumer_response_200_device_item_last_updated import (
            PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = PostV1ExtranetsB2BConsumerResponse200DeviceItemLastUpdated.from_dict(_last_updated)

        site = d.pop("site", UNSET)

        status = d.pop("status", UNSET)

        post_v1_extranets_b2b_consumer_response_200_device_item = cls(
            device_id=device_id,
            last_updated=last_updated,
            site=site,
            status=status,
        )

        post_v1_extranets_b2b_consumer_response_200_device_item.additional_properties = d
        return post_v1_extranets_b2b_consumer_response_200_device_item

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
