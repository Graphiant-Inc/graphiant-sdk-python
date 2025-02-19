from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_lan_segments_usage_top_response_200_top_vrfs_item import (
        PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem,
    )


T = TypeVar("T", bound="PostV2ExtranetLanSegmentsUsageTopResponse200")


@_attrs_define
class PostV2ExtranetLanSegmentsUsageTopResponse200:
    """
    Attributes:
        top_vrfs (Union[Unset, list['PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem']]):
    """

    top_vrfs: Union[Unset, list["PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_vrfs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_vrfs, Unset):
            top_vrfs = []
            for top_vrfs_item_data in self.top_vrfs:
                top_vrfs_item = top_vrfs_item_data.to_dict()
                top_vrfs.append(top_vrfs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_vrfs is not UNSET:
            field_dict["topVrfs"] = top_vrfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_lan_segments_usage_top_response_200_top_vrfs_item import (
            PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem,
        )

        d = src_dict.copy()
        top_vrfs = []
        _top_vrfs = d.pop("topVrfs", UNSET)
        for top_vrfs_item_data in _top_vrfs or []:
            top_vrfs_item = PostV2ExtranetLanSegmentsUsageTopResponse200TopVrfsItem.from_dict(top_vrfs_item_data)

            top_vrfs.append(top_vrfs_item)

        post_v2_extranet_lan_segments_usage_top_response_200 = cls(
            top_vrfs=top_vrfs,
        )

        post_v2_extranet_lan_segments_usage_top_response_200.additional_properties = d
        return post_v2_extranet_lan_segments_usage_top_response_200

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
