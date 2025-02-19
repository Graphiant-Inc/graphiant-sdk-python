from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_logs_body_old_ts import PostV1AuditLogsBodyOldTs
    from ..models.post_v1_audit_logs_body_recent_ts import PostV1AuditLogsBodyRecentTs
    from ..models.post_v1_audit_logs_body_selectors_item import PostV1AuditLogsBodySelectorsItem


T = TypeVar("T", bound="PostV1AuditLogsBody")


@_attrs_define
class PostV1AuditLogsBody:
    """
    Attributes:
        cursor_ref (Union[Unset, str]):  Example: TYPE_STRING.
        histogram_bucket_size_sec (Union[Unset, str]):  Example: TYPE_UINT32.
        num_logs (Union[Unset, str]):  Example: TYPE_UINT32.
        old_ts (Union[Unset, PostV1AuditLogsBodyOldTs]):
        recent_ts (Union[Unset, PostV1AuditLogsBodyRecentTs]):
        selectors (Union[Unset, list['PostV1AuditLogsBodySelectorsItem']]):
    """

    cursor_ref: Union[Unset, str] = UNSET
    histogram_bucket_size_sec: Union[Unset, str] = UNSET
    num_logs: Union[Unset, str] = UNSET
    old_ts: Union[Unset, "PostV1AuditLogsBodyOldTs"] = UNSET
    recent_ts: Union[Unset, "PostV1AuditLogsBodyRecentTs"] = UNSET
    selectors: Union[Unset, list["PostV1AuditLogsBodySelectorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref = self.cursor_ref

        histogram_bucket_size_sec = self.histogram_bucket_size_sec

        num_logs = self.num_logs

        old_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.old_ts, Unset):
            old_ts = self.old_ts.to_dict()

        recent_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recent_ts, Unset):
            recent_ts = self.recent_ts.to_dict()

        selectors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if histogram_bucket_size_sec is not UNSET:
            field_dict["histogramBucketSizeSec"] = histogram_bucket_size_sec
        if num_logs is not UNSET:
            field_dict["numLogs"] = num_logs
        if old_ts is not UNSET:
            field_dict["oldTs"] = old_ts
        if recent_ts is not UNSET:
            field_dict["recentTs"] = recent_ts
        if selectors is not UNSET:
            field_dict["selectors"] = selectors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_logs_body_old_ts import PostV1AuditLogsBodyOldTs
        from ..models.post_v1_audit_logs_body_recent_ts import PostV1AuditLogsBodyRecentTs
        from ..models.post_v1_audit_logs_body_selectors_item import PostV1AuditLogsBodySelectorsItem

        d = src_dict.copy()
        cursor_ref = d.pop("cursorRef", UNSET)

        histogram_bucket_size_sec = d.pop("histogramBucketSizeSec", UNSET)

        num_logs = d.pop("numLogs", UNSET)

        _old_ts = d.pop("oldTs", UNSET)
        old_ts: Union[Unset, PostV1AuditLogsBodyOldTs]
        if isinstance(_old_ts, Unset):
            old_ts = UNSET
        else:
            old_ts = PostV1AuditLogsBodyOldTs.from_dict(_old_ts)

        _recent_ts = d.pop("recentTs", UNSET)
        recent_ts: Union[Unset, PostV1AuditLogsBodyRecentTs]
        if isinstance(_recent_ts, Unset):
            recent_ts = UNSET
        else:
            recent_ts = PostV1AuditLogsBodyRecentTs.from_dict(_recent_ts)

        selectors = []
        _selectors = d.pop("selectors", UNSET)
        for selectors_item_data in _selectors or []:
            selectors_item = PostV1AuditLogsBodySelectorsItem.from_dict(selectors_item_data)

            selectors.append(selectors_item)

        post_v1_audit_logs_body = cls(
            cursor_ref=cursor_ref,
            histogram_bucket_size_sec=histogram_bucket_size_sec,
            num_logs=num_logs,
            old_ts=old_ts,
            recent_ts=recent_ts,
            selectors=selectors,
        )

        post_v1_audit_logs_body.additional_properties = d
        return post_v1_audit_logs_body

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
