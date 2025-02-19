from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_source_segments_response_200_vrfs_item import (
        PostV1ExtranetsSourceSegmentsResponse200VrfsItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsSourceSegmentsResponse200")


@_attrs_define
class PostV1ExtranetsSourceSegmentsResponse200:
    """
    Attributes:
        vrfs (Union[Unset, list['PostV1ExtranetsSourceSegmentsResponse200VrfsItem']]):
    """

    vrfs: Union[Unset, list["PostV1ExtranetsSourceSegmentsResponse200VrfsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vrfs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vrfs, Unset):
            vrfs = []
            for vrfs_item_data in self.vrfs:
                vrfs_item = vrfs_item_data.to_dict()
                vrfs.append(vrfs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vrfs is not UNSET:
            field_dict["vrfs"] = vrfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_source_segments_response_200_vrfs_item import (
            PostV1ExtranetsSourceSegmentsResponse200VrfsItem,
        )

        d = src_dict.copy()
        vrfs = []
        _vrfs = d.pop("vrfs", UNSET)
        for vrfs_item_data in _vrfs or []:
            vrfs_item = PostV1ExtranetsSourceSegmentsResponse200VrfsItem.from_dict(vrfs_item_data)

            vrfs.append(vrfs_item)

        post_v1_extranets_source_segments_response_200 = cls(
            vrfs=vrfs,
        )

        post_v1_extranets_source_segments_response_200.additional_properties = d
        return post_v1_extranets_source_segments_response_200

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
