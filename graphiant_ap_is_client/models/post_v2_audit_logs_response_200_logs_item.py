from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_audit_logs_response_200_logs_item_entity import PostV2AuditLogsResponse200LogsItemEntity
    from ..models.post_v2_audit_logs_response_200_logs_item_target import PostV2AuditLogsResponse200LogsItemTarget
    from ..models.post_v2_audit_logs_response_200_logs_item_ts import PostV2AuditLogsResponse200LogsItemTs


T = TypeVar("T", bound="PostV2AuditLogsResponse200LogsItem")


@_attrs_define
class PostV2AuditLogsResponse200LogsItem:
    """
    Attributes:
        action (Union[Unset, str]):  Example: TYPE_STRING.
        activity_id (Union[Unset, str]):  Example: TYPE_STRING.
        category (Union[Unset, str]):  Example: TYPE_ENUM.
        entity (Union[Unset, PostV2AuditLogsResponse200LogsItemEntity]):
        job_type (Union[Unset, str]):  Example: TYPE_ENUM.
        target (Union[Unset, PostV2AuditLogsResponse200LogsItemTarget]):
        ts (Union[Unset, PostV2AuditLogsResponse200LogsItemTs]):
        user (Union[Unset, str]):  Example: TYPE_STRING.
    """

    action: Union[Unset, str] = UNSET
    activity_id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    entity: Union[Unset, "PostV2AuditLogsResponse200LogsItemEntity"] = UNSET
    job_type: Union[Unset, str] = UNSET
    target: Union[Unset, "PostV2AuditLogsResponse200LogsItemTarget"] = UNSET
    ts: Union[Unset, "PostV2AuditLogsResponse200LogsItemTs"] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        activity_id = self.activity_id

        category = self.category

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        job_type = self.job_type

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if activity_id is not UNSET:
            field_dict["activityId"] = activity_id
        if category is not UNSET:
            field_dict["category"] = category
        if entity is not UNSET:
            field_dict["entity"] = entity
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if target is not UNSET:
            field_dict["target"] = target
        if ts is not UNSET:
            field_dict["ts"] = ts
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_audit_logs_response_200_logs_item_entity import PostV2AuditLogsResponse200LogsItemEntity
        from ..models.post_v2_audit_logs_response_200_logs_item_target import PostV2AuditLogsResponse200LogsItemTarget
        from ..models.post_v2_audit_logs_response_200_logs_item_ts import PostV2AuditLogsResponse200LogsItemTs

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        activity_id = d.pop("activityId", UNSET)

        category = d.pop("category", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, PostV2AuditLogsResponse200LogsItemEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = PostV2AuditLogsResponse200LogsItemEntity.from_dict(_entity)

        job_type = d.pop("jobType", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PostV2AuditLogsResponse200LogsItemTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PostV2AuditLogsResponse200LogsItemTarget.from_dict(_target)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, PostV2AuditLogsResponse200LogsItemTs]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = PostV2AuditLogsResponse200LogsItemTs.from_dict(_ts)

        user = d.pop("user", UNSET)

        post_v2_audit_logs_response_200_logs_item = cls(
            action=action,
            activity_id=activity_id,
            category=category,
            entity=entity,
            job_type=job_type,
            target=target,
            ts=ts,
            user=user,
        )

        post_v2_audit_logs_response_200_logs_item.additional_properties = d
        return post_v2_audit_logs_response_200_logs_item

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
