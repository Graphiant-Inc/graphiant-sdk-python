from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_logs_response_200_logs_item_end import PostV1AuditLogsResponse200LogsItemEnd
    from ..models.post_v1_audit_logs_response_200_logs_item_failed_target_results_item import (
        PostV1AuditLogsResponse200LogsItemFailedTargetResultsItem,
    )
    from ..models.post_v1_audit_logs_response_200_logs_item_start import PostV1AuditLogsResponse200LogsItemStart
    from ..models.post_v1_audit_logs_response_200_logs_item_targets_item import (
        PostV1AuditLogsResponse200LogsItemTargetsItem,
    )


T = TypeVar("T", bound="PostV1AuditLogsResponse200LogsItem")


@_attrs_define
class PostV1AuditLogsResponse200LogsItem:
    """
    Attributes:
        activity (Union[Unset, str]):  Example: TYPE_STRING.
        actor (Union[Unset, str]):  Example: TYPE_STRING.
        category (Union[Unset, str]):  Example: TYPE_ENUM.
        end (Union[Unset, PostV1AuditLogsResponse200LogsItemEnd]):
        failed_target_results (Union[Unset, list['PostV1AuditLogsResponse200LogsItemFailedTargetResultsItem']]):
        info (Union[Unset, str]):  Example: TYPE_STRING.
        reason (Union[Unset, str]):  Example: TYPE_STRING.
        service (Union[Unset, str]):  Example: TYPE_ENUM.
        start (Union[Unset, PostV1AuditLogsResponse200LogsItemStart]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        targets (Union[Unset, list['PostV1AuditLogsResponse200LogsItemTargetsItem']]):
    """

    activity: Union[Unset, str] = UNSET
    actor: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    end: Union[Unset, "PostV1AuditLogsResponse200LogsItemEnd"] = UNSET
    failed_target_results: Union[Unset, list["PostV1AuditLogsResponse200LogsItemFailedTargetResultsItem"]] = UNSET
    info: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    start: Union[Unset, "PostV1AuditLogsResponse200LogsItemStart"] = UNSET
    status: Union[Unset, str] = UNSET
    targets: Union[Unset, list["PostV1AuditLogsResponse200LogsItemTargetsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity = self.activity

        actor = self.actor

        category = self.category

        end: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        failed_target_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.failed_target_results, Unset):
            failed_target_results = []
            for failed_target_results_item_data in self.failed_target_results:
                failed_target_results_item = failed_target_results_item_data.to_dict()
                failed_target_results.append(failed_target_results_item)

        info = self.info

        reason = self.reason

        service = self.service

        start: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        status = self.status

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity is not UNSET:
            field_dict["activity"] = activity
        if actor is not UNSET:
            field_dict["actor"] = actor
        if category is not UNSET:
            field_dict["category"] = category
        if end is not UNSET:
            field_dict["end"] = end
        if failed_target_results is not UNSET:
            field_dict["failedTargetResults"] = failed_target_results
        if info is not UNSET:
            field_dict["info"] = info
        if reason is not UNSET:
            field_dict["reason"] = reason
        if service is not UNSET:
            field_dict["service"] = service
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_logs_response_200_logs_item_end import PostV1AuditLogsResponse200LogsItemEnd
        from ..models.post_v1_audit_logs_response_200_logs_item_failed_target_results_item import (
            PostV1AuditLogsResponse200LogsItemFailedTargetResultsItem,
        )
        from ..models.post_v1_audit_logs_response_200_logs_item_start import PostV1AuditLogsResponse200LogsItemStart
        from ..models.post_v1_audit_logs_response_200_logs_item_targets_item import (
            PostV1AuditLogsResponse200LogsItemTargetsItem,
        )

        d = src_dict.copy()
        activity = d.pop("activity", UNSET)

        actor = d.pop("actor", UNSET)

        category = d.pop("category", UNSET)

        _end = d.pop("end", UNSET)
        end: Union[Unset, PostV1AuditLogsResponse200LogsItemEnd]
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = PostV1AuditLogsResponse200LogsItemEnd.from_dict(_end)

        failed_target_results = []
        _failed_target_results = d.pop("failedTargetResults", UNSET)
        for failed_target_results_item_data in _failed_target_results or []:
            failed_target_results_item = PostV1AuditLogsResponse200LogsItemFailedTargetResultsItem.from_dict(
                failed_target_results_item_data
            )

            failed_target_results.append(failed_target_results_item)

        info = d.pop("info", UNSET)

        reason = d.pop("reason", UNSET)

        service = d.pop("service", UNSET)

        _start = d.pop("start", UNSET)
        start: Union[Unset, PostV1AuditLogsResponse200LogsItemStart]
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = PostV1AuditLogsResponse200LogsItemStart.from_dict(_start)

        status = d.pop("status", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = PostV1AuditLogsResponse200LogsItemTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        post_v1_audit_logs_response_200_logs_item = cls(
            activity=activity,
            actor=actor,
            category=category,
            end=end,
            failed_target_results=failed_target_results,
            info=info,
            reason=reason,
            service=service,
            start=start,
            status=status,
            targets=targets,
        )

        post_v1_audit_logs_response_200_logs_item.additional_properties = d
        return post_v1_audit_logs_response_200_logs_item

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
