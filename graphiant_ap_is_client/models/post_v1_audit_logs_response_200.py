from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_logs_response_200_histogram_item import PostV1AuditLogsResponse200HistogramItem
    from ..models.post_v1_audit_logs_response_200_logs_item import PostV1AuditLogsResponse200LogsItem


T = TypeVar("T", bound="PostV1AuditLogsResponse200")


@_attrs_define
class PostV1AuditLogsResponse200:
    """
    Attributes:
        cursor_ref (Union[Unset, str]):  Example: TYPE_STRING.
        histogram (Union[Unset, list['PostV1AuditLogsResponse200HistogramItem']]):
        logs (Union[Unset, list['PostV1AuditLogsResponse200LogsItem']]):
        total_logs (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    cursor_ref: Union[Unset, str] = UNSET
    histogram: Union[Unset, list["PostV1AuditLogsResponse200HistogramItem"]] = UNSET
    logs: Union[Unset, list["PostV1AuditLogsResponse200LogsItem"]] = UNSET
    total_logs: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref = self.cursor_ref

        histogram: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.histogram, Unset):
            histogram = []
            for histogram_item_data in self.histogram:
                histogram_item = histogram_item_data.to_dict()
                histogram.append(histogram_item)

        logs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        total_logs = self.total_logs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if histogram is not UNSET:
            field_dict["histogram"] = histogram
        if logs is not UNSET:
            field_dict["logs"] = logs
        if total_logs is not UNSET:
            field_dict["totalLogs"] = total_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_logs_response_200_histogram_item import PostV1AuditLogsResponse200HistogramItem
        from ..models.post_v1_audit_logs_response_200_logs_item import PostV1AuditLogsResponse200LogsItem

        d = src_dict.copy()
        cursor_ref = d.pop("cursorRef", UNSET)

        histogram = []
        _histogram = d.pop("histogram", UNSET)
        for histogram_item_data in _histogram or []:
            histogram_item = PostV1AuditLogsResponse200HistogramItem.from_dict(histogram_item_data)

            histogram.append(histogram_item)

        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = PostV1AuditLogsResponse200LogsItem.from_dict(logs_item_data)

            logs.append(logs_item)

        total_logs = d.pop("totalLogs", UNSET)

        post_v1_audit_logs_response_200 = cls(
            cursor_ref=cursor_ref,
            histogram=histogram,
            logs=logs,
            total_logs=total_logs,
        )

        post_v1_audit_logs_response_200.additional_properties = d
        return post_v1_audit_logs_response_200

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
