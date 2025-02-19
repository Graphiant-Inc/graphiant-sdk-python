from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_audit_logs_body_old_ts import PostV2AuditLogsBodyOldTs
    from ..models.post_v2_audit_logs_body_recent_ts import PostV2AuditLogsBodyRecentTs
    from ..models.post_v2_audit_logs_body_selector import PostV2AuditLogsBodySelector


T = TypeVar("T", bound="PostV2AuditLogsBody")


@_attrs_define
class PostV2AuditLogsBody:
    """
    Attributes:
        cursor_ref (Union[Unset, str]):  Example: TYPE_STRING.
        num_logs (Union[Unset, str]):  Example: TYPE_UINT32.
        old_ts (Union[Unset, PostV2AuditLogsBodyOldTs]):
        recent_ts (Union[Unset, PostV2AuditLogsBodyRecentTs]):
        selector (Union[Unset, PostV2AuditLogsBodySelector]):
    """

    cursor_ref: Union[Unset, str] = UNSET
    num_logs: Union[Unset, str] = UNSET
    old_ts: Union[Unset, "PostV2AuditLogsBodyOldTs"] = UNSET
    recent_ts: Union[Unset, "PostV2AuditLogsBodyRecentTs"] = UNSET
    selector: Union[Unset, "PostV2AuditLogsBodySelector"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref = self.cursor_ref

        num_logs = self.num_logs

        old_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.old_ts, Unset):
            old_ts = self.old_ts.to_dict()

        recent_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recent_ts, Unset):
            recent_ts = self.recent_ts.to_dict()

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if num_logs is not UNSET:
            field_dict["numLogs"] = num_logs
        if old_ts is not UNSET:
            field_dict["oldTs"] = old_ts
        if recent_ts is not UNSET:
            field_dict["recentTs"] = recent_ts
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_audit_logs_body_old_ts import PostV2AuditLogsBodyOldTs
        from ..models.post_v2_audit_logs_body_recent_ts import PostV2AuditLogsBodyRecentTs
        from ..models.post_v2_audit_logs_body_selector import PostV2AuditLogsBodySelector

        d = src_dict.copy()
        cursor_ref = d.pop("cursorRef", UNSET)

        num_logs = d.pop("numLogs", UNSET)

        _old_ts = d.pop("oldTs", UNSET)
        old_ts: Union[Unset, PostV2AuditLogsBodyOldTs]
        if isinstance(_old_ts, Unset):
            old_ts = UNSET
        else:
            old_ts = PostV2AuditLogsBodyOldTs.from_dict(_old_ts)

        _recent_ts = d.pop("recentTs", UNSET)
        recent_ts: Union[Unset, PostV2AuditLogsBodyRecentTs]
        if isinstance(_recent_ts, Unset):
            recent_ts = UNSET
        else:
            recent_ts = PostV2AuditLogsBodyRecentTs.from_dict(_recent_ts)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV2AuditLogsBodySelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV2AuditLogsBodySelector.from_dict(_selector)

        post_v2_audit_logs_body = cls(
            cursor_ref=cursor_ref,
            num_logs=num_logs,
            old_ts=old_ts,
            recent_ts=recent_ts,
            selector=selector,
        )

        post_v2_audit_logs_body.additional_properties = d
        return post_v2_audit_logs_body

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
