from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_lan_segments_response_200_page_info import GetV1LanSegmentsResponse200PageInfo
    from ..models.get_v1_lan_segments_response_200_segments_item import GetV1LanSegmentsResponse200SegmentsItem


T = TypeVar("T", bound="GetV1LanSegmentsResponse200")


@_attrs_define
class GetV1LanSegmentsResponse200:
    """
    Attributes:
        page_info (Union[Unset, GetV1LanSegmentsResponse200PageInfo]):
        segments (Union[Unset, list['GetV1LanSegmentsResponse200SegmentsItem']]):
    """

    page_info: Union[Unset, "GetV1LanSegmentsResponse200PageInfo"] = UNSET
    segments: Union[Unset, list["GetV1LanSegmentsResponse200SegmentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        segments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_lan_segments_response_200_page_info import GetV1LanSegmentsResponse200PageInfo
        from ..models.get_v1_lan_segments_response_200_segments_item import GetV1LanSegmentsResponse200SegmentsItem

        d = src_dict.copy()
        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1LanSegmentsResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1LanSegmentsResponse200PageInfo.from_dict(_page_info)

        segments = []
        _segments = d.pop("segments", UNSET)
        for segments_item_data in _segments or []:
            segments_item = GetV1LanSegmentsResponse200SegmentsItem.from_dict(segments_item_data)

            segments.append(segments_item)

        get_v1_lan_segments_response_200 = cls(
            page_info=page_info,
            segments=segments,
        )

        get_v1_lan_segments_response_200.additional_properties = d
        return get_v1_lan_segments_response_200

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
