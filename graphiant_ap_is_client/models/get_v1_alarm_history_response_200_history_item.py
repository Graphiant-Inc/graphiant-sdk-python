from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarm_history_response_200_history_item_time import GetV1AlarmHistoryResponse200HistoryItemTime


T = TypeVar("T", bound="GetV1AlarmHistoryResponse200HistoryItem")


@_attrs_define
class GetV1AlarmHistoryResponse200HistoryItem:
    """
    Attributes:
        boot_id (Union[Unset, str]):  Example: 8a2ec658-f25b-11ec-b939-0242ac120002.
        description (Union[Unset, str]):  Example: NTP service initiated. Synchronization state is unknown..
        is_cleared (Union[Unset, str]):  Example: false.
        perceived_severity (Union[Unset, str]):  Example: warning.
        sequence_number (Union[Unset, str]):  Example: 10.
        time (Union[Unset, GetV1AlarmHistoryResponse200HistoryItemTime]):
    """

    boot_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_cleared: Union[Unset, str] = UNSET
    perceived_severity: Union[Unset, str] = UNSET
    sequence_number: Union[Unset, str] = UNSET
    time: Union[Unset, "GetV1AlarmHistoryResponse200HistoryItemTime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boot_id = self.boot_id

        description = self.description

        is_cleared = self.is_cleared

        perceived_severity = self.perceived_severity

        sequence_number = self.sequence_number

        time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boot_id is not UNSET:
            field_dict["bootId"] = boot_id
        if description is not UNSET:
            field_dict["description"] = description
        if is_cleared is not UNSET:
            field_dict["isCleared"] = is_cleared
        if perceived_severity is not UNSET:
            field_dict["perceivedSeverity"] = perceived_severity
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarm_history_response_200_history_item_time import (
            GetV1AlarmHistoryResponse200HistoryItemTime,
        )

        d = src_dict.copy()
        boot_id = d.pop("bootId", UNSET)

        description = d.pop("description", UNSET)

        is_cleared = d.pop("isCleared", UNSET)

        perceived_severity = d.pop("perceivedSeverity", UNSET)

        sequence_number = d.pop("sequenceNumber", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, GetV1AlarmHistoryResponse200HistoryItemTime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = GetV1AlarmHistoryResponse200HistoryItemTime.from_dict(_time)

        get_v1_alarm_history_response_200_history_item = cls(
            boot_id=boot_id,
            description=description,
            is_cleared=is_cleared,
            perceived_severity=perceived_severity,
            sequence_number=sequence_number,
            time=time,
        )

        get_v1_alarm_history_response_200_history_item.additional_properties = d
        return get_v1_alarm_history_response_200_history_item

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
