from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_audit_logs_response_200_logs_item import PostV2AuditLogsResponse200LogsItem


T = TypeVar("T", bound="PostV2AuditLogsResponse200")


@_attrs_define
class PostV2AuditLogsResponse200:
    """
    Attributes:
        cursor_ref (Union[Unset, str]):  Example: TYPE_STRING.
        logs (Union[Unset, list['PostV2AuditLogsResponse200LogsItem']]):
        total_logs (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    cursor_ref: Union[Unset, str] = UNSET
    logs: Union[Unset, list["PostV2AuditLogsResponse200LogsItem"]] = UNSET
    total_logs: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref = self.cursor_ref

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
        if logs is not UNSET:
            field_dict["logs"] = logs
        if total_logs is not UNSET:
            field_dict["totalLogs"] = total_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_audit_logs_response_200_logs_item import PostV2AuditLogsResponse200LogsItem

        d = src_dict.copy()
        cursor_ref = d.pop("cursorRef", UNSET)

        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = PostV2AuditLogsResponse200LogsItem.from_dict(logs_item_data)

            logs.append(logs_item)

        total_logs = d.pop("totalLogs", UNSET)

        post_v2_audit_logs_response_200 = cls(
            cursor_ref=cursor_ref,
            logs=logs,
            total_logs=total_logs,
        )

        post_v2_audit_logs_response_200.additional_properties = d
        return post_v2_audit_logs_response_200

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
