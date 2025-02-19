from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_activity_logs_response_200_details_item_attributes_item import (
        PostV1ActivityLogsResponse200DetailsItemAttributesItem,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_end_ts import (
        PostV1ActivityLogsResponse200DetailsItemEndTs,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_job_entities_item import (
        PostV1ActivityLogsResponse200DetailsItemJobEntitiesItem,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_start_ts import (
        PostV1ActivityLogsResponse200DetailsItemStartTs,
    )
    from ..models.post_v1_activity_logs_response_200_details_item_targets_item import (
        PostV1ActivityLogsResponse200DetailsItemTargetsItem,
    )


T = TypeVar("T", bound="PostV1ActivityLogsResponse200DetailsItem")


@_attrs_define
class PostV1ActivityLogsResponse200DetailsItem:
    """
    Attributes:
        action (Union[Unset, str]):  Example: TYPE_STRING.
        attributes (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItemAttributesItem']]):
        category (Union[Unset, str]):  Example: TYPE_ENUM.
        end_ts (Union[Unset, PostV1ActivityLogsResponse200DetailsItemEndTs]):
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_STRING.
        job_entities (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItemJobEntitiesItem']]):
        job_type (Union[Unset, str]):  Example: TYPE_ENUM.
        original_enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        start_ts (Union[Unset, PostV1ActivityLogsResponse200DetailsItemStartTs]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        targets (Union[Unset, list['PostV1ActivityLogsResponse200DetailsItemTargetsItem']]):
        trace_session_id (Union[Unset, str]):  Example: TYPE_STRING.
        usage (Union[Unset, str]):  Example: TYPE_ENUM.
        user (Union[Unset, str]):  Example: TYPE_STRING.
        user_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    action: Union[Unset, str] = UNSET
    attributes: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItemAttributesItem"]] = UNSET
    category: Union[Unset, str] = UNSET
    end_ts: Union[Unset, "PostV1ActivityLogsResponse200DetailsItemEndTs"] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    job_entities: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItemJobEntitiesItem"]] = UNSET
    job_type: Union[Unset, str] = UNSET
    original_enterprise_id: Union[Unset, str] = UNSET
    start_ts: Union[Unset, "PostV1ActivityLogsResponse200DetailsItemStartTs"] = UNSET
    status: Union[Unset, str] = UNSET
    targets: Union[Unset, list["PostV1ActivityLogsResponse200DetailsItemTargetsItem"]] = UNSET
    trace_session_id: Union[Unset, str] = UNSET
    usage: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        category = self.category

        end_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.end_ts, Unset):
            end_ts = self.end_ts.to_dict()

        enterprise_id = self.enterprise_id

        id = self.id

        job_entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.job_entities, Unset):
            job_entities = []
            for job_entities_item_data in self.job_entities:
                job_entities_item = job_entities_item_data.to_dict()
                job_entities.append(job_entities_item)

        job_type = self.job_type

        original_enterprise_id = self.original_enterprise_id

        start_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.start_ts, Unset):
            start_ts = self.start_ts.to_dict()

        status = self.status

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        trace_session_id = self.trace_session_id

        usage = self.usage

        user = self.user

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if category is not UNSET:
            field_dict["category"] = category
        if end_ts is not UNSET:
            field_dict["endTs"] = end_ts
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if job_entities is not UNSET:
            field_dict["jobEntities"] = job_entities
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if original_enterprise_id is not UNSET:
            field_dict["originalEnterpriseId"] = original_enterprise_id
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if status is not UNSET:
            field_dict["status"] = status
        if targets is not UNSET:
            field_dict["targets"] = targets
        if trace_session_id is not UNSET:
            field_dict["traceSessionId"] = trace_session_id
        if usage is not UNSET:
            field_dict["usage"] = usage
        if user is not UNSET:
            field_dict["user"] = user
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_activity_logs_response_200_details_item_attributes_item import (
            PostV1ActivityLogsResponse200DetailsItemAttributesItem,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_end_ts import (
            PostV1ActivityLogsResponse200DetailsItemEndTs,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_job_entities_item import (
            PostV1ActivityLogsResponse200DetailsItemJobEntitiesItem,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_start_ts import (
            PostV1ActivityLogsResponse200DetailsItemStartTs,
        )
        from ..models.post_v1_activity_logs_response_200_details_item_targets_item import (
            PostV1ActivityLogsResponse200DetailsItemTargetsItem,
        )

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = PostV1ActivityLogsResponse200DetailsItemAttributesItem.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        category = d.pop("category", UNSET)

        _end_ts = d.pop("endTs", UNSET)
        end_ts: Union[Unset, PostV1ActivityLogsResponse200DetailsItemEndTs]
        if isinstance(_end_ts, Unset):
            end_ts = UNSET
        else:
            end_ts = PostV1ActivityLogsResponse200DetailsItemEndTs.from_dict(_end_ts)

        enterprise_id = d.pop("enterpriseId", UNSET)

        id = d.pop("id", UNSET)

        job_entities = []
        _job_entities = d.pop("jobEntities", UNSET)
        for job_entities_item_data in _job_entities or []:
            job_entities_item = PostV1ActivityLogsResponse200DetailsItemJobEntitiesItem.from_dict(
                job_entities_item_data
            )

            job_entities.append(job_entities_item)

        job_type = d.pop("jobType", UNSET)

        original_enterprise_id = d.pop("originalEnterpriseId", UNSET)

        _start_ts = d.pop("startTs", UNSET)
        start_ts: Union[Unset, PostV1ActivityLogsResponse200DetailsItemStartTs]
        if isinstance(_start_ts, Unset):
            start_ts = UNSET
        else:
            start_ts = PostV1ActivityLogsResponse200DetailsItemStartTs.from_dict(_start_ts)

        status = d.pop("status", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = PostV1ActivityLogsResponse200DetailsItemTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        trace_session_id = d.pop("traceSessionId", UNSET)

        usage = d.pop("usage", UNSET)

        user = d.pop("user", UNSET)

        user_id = d.pop("userId", UNSET)

        post_v1_activity_logs_response_200_details_item = cls(
            action=action,
            attributes=attributes,
            category=category,
            end_ts=end_ts,
            enterprise_id=enterprise_id,
            id=id,
            job_entities=job_entities,
            job_type=job_type,
            original_enterprise_id=original_enterprise_id,
            start_ts=start_ts,
            status=status,
            targets=targets,
            trace_session_id=trace_session_id,
            usage=usage,
            user=user,
            user_id=user_id,
        )

        post_v1_activity_logs_response_200_details_item.additional_properties = d
        return post_v1_activity_logs_response_200_details_item

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
