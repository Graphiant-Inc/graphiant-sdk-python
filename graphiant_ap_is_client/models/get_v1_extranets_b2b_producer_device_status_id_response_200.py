from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item import (
        GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsB2BProducerDeviceStatusIdResponse200")


@_attrs_define
class GetV1ExtranetsB2BProducerDeviceStatusIdResponse200:
    """
    Attributes:
        summary (Union[Unset, list['GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem']]):
    """

    summary: Union[Unset, list["GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = []
            for summary_item_data in self.summary:
                summary_item = summary_item_data.to_dict()
                summary.append(summary_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_b2b_producer_device_status_id_response_200_summary_item import (
            GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem,
        )

        d = src_dict.copy()
        summary = []
        _summary = d.pop("summary", UNSET)
        for summary_item_data in _summary or []:
            summary_item = GetV1ExtranetsB2BProducerDeviceStatusIdResponse200SummaryItem.from_dict(summary_item_data)

            summary.append(summary_item)

        get_v1_extranets_b2b_producer_device_status_id_response_200 = cls(
            summary=summary,
        )

        get_v1_extranets_b2b_producer_device_status_id_response_200.additional_properties = d
        return get_v1_extranets_b2b_producer_device_status_id_response_200

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
