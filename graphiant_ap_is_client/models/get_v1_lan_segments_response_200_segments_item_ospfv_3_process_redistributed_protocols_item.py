from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1LanSegmentsResponse200SegmentsItemOspfv3ProcessRedistributedProtocolsItem")


@_attrs_define
class GetV1LanSegmentsResponse200SegmentsItemOspfv3ProcessRedistributedProtocolsItem:
    """
    Attributes:
        metric (Union[Unset, str]):  Example: TYPE_UINT32.
        metric_type (Union[Unset, str]):  Example: TYPE_ENUM.
        redist_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    metric: Union[Unset, str] = UNSET
    metric_type: Union[Unset, str] = UNSET
    redist_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        metric_type = self.metric_type

        redist_type = self.redist_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metric is not UNSET:
            field_dict["metric"] = metric
        if metric_type is not UNSET:
            field_dict["metricType"] = metric_type
        if redist_type is not UNSET:
            field_dict["redistType"] = redist_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        metric = d.pop("metric", UNSET)

        metric_type = d.pop("metricType", UNSET)

        redist_type = d.pop("redistType", UNSET)

        get_v1_lan_segments_response_200_segments_item_ospfv_3_process_redistributed_protocols_item = cls(
            metric=metric,
            metric_type=metric_type,
            redist_type=redist_type,
        )

        get_v1_lan_segments_response_200_segments_item_ospfv_3_process_redistributed_protocols_item.additional_properties = d
        return get_v1_lan_segments_response_200_segments_item_ospfv_3_process_redistributed_protocols_item

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
