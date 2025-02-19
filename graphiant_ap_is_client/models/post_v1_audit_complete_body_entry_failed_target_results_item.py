from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_audit_complete_body_entry_failed_target_results_item_target import (
        PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget,
    )


T = TypeVar("T", bound="PostV1AuditCompleteBodyEntryFailedTargetResultsItem")


@_attrs_define
class PostV1AuditCompleteBodyEntryFailedTargetResultsItem:
    """
    Attributes:
        reason (Union[Unset, str]):  Example: Permission denied..
        status (Union[Unset, str]):  Example: Failure.
        target (Union[Unset, PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget]):
    """

    reason: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    target: Union[Unset, "PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        status = self.status

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_audit_complete_body_entry_failed_target_results_item_target import (
            PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget,
        )

        d = src_dict.copy()
        reason = d.pop("reason", UNSET)

        status = d.pop("status", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PostV1AuditCompleteBodyEntryFailedTargetResultsItemTarget.from_dict(_target)

        post_v1_audit_complete_body_entry_failed_target_results_item = cls(
            reason=reason,
            status=status,
            target=target,
        )

        post_v1_audit_complete_body_entry_failed_target_results_item.additional_properties = d
        return post_v1_audit_complete_body_entry_failed_target_results_item

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
