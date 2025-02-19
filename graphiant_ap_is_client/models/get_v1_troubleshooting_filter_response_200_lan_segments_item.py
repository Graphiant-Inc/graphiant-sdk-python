from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1TroubleshootingFilterResponse200LanSegmentsItem")


@_attrs_define
class GetV1TroubleshootingFilterResponse200LanSegmentsItem:
    """
    Attributes:
        lan_segment (Union[Unset, str]):  Example: TYPE_STRING.
    """

    lan_segment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_segment = self.lan_segment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lan_segment = d.pop("lanSegment", UNSET)

        get_v1_troubleshooting_filter_response_200_lan_segments_item = cls(
            lan_segment=lan_segment,
        )

        get_v1_troubleshooting_filter_response_200_lan_segments_item.additional_properties = d
        return get_v1_troubleshooting_filter_response_200_lan_segments_item

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
