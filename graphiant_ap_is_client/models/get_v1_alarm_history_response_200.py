from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_alarm_history_response_200_history_item import GetV1AlarmHistoryResponse200HistoryItem


T = TypeVar("T", bound="GetV1AlarmHistoryResponse200")


@_attrs_define
class GetV1AlarmHistoryResponse200:
    """
    Attributes:
        history (Union[Unset, list['GetV1AlarmHistoryResponse200HistoryItem']]):
    """

    history: Union[Unset, list["GetV1AlarmHistoryResponse200HistoryItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_alarm_history_response_200_history_item import GetV1AlarmHistoryResponse200HistoryItem

        d = src_dict.copy()
        history = []
        _history = d.pop("history", UNSET)
        for history_item_data in _history or []:
            history_item = GetV1AlarmHistoryResponse200HistoryItem.from_dict(history_item_data)

            history.append(history_item)

        get_v1_alarm_history_response_200 = cls(
            history=history,
        )

        get_v1_alarm_history_response_200.additional_properties = d
        return get_v1_alarm_history_response_200

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
