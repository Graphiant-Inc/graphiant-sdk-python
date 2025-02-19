from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_activity_logs_body_selector_job_entity import PostV1ActivityLogsBodySelectorJobEntity
    from ..models.post_v1_activity_logs_body_selector_target_ids_item import PostV1ActivityLogsBodySelectorTargetIdsItem


T = TypeVar("T", bound="PostV1ActivityLogsBodySelector")


@_attrs_define
class PostV1ActivityLogsBodySelector:
    """
    Attributes:
        device_ids (Union[Unset, list[str]]):  Example: ['TYPE_INT64'].
        id (Union[Unset, str]):  Example: TYPE_STRING.
        in_progress (Union[Unset, str]):  Example: TYPE_BOOL.
        job_entity (Union[Unset, PostV1ActivityLogsBodySelectorJobEntity]):
        target_ids (Union[Unset, list['PostV1ActivityLogsBodySelectorTargetIdsItem']]):
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_ids: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    in_progress: Union[Unset, str] = UNSET
    job_entity: Union[Unset, "PostV1ActivityLogsBodySelectorJobEntity"] = UNSET
    target_ids: Union[Unset, list["PostV1ActivityLogsBodySelectorTargetIdsItem"]] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.device_ids, Unset):
            device_ids = self.device_ids

        id = self.id

        in_progress = self.in_progress

        job_entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.job_entity, Unset):
            job_entity = self.job_entity.to_dict()

        target_ids: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.target_ids, Unset):
            target_ids = []
            for target_ids_item_data in self.target_ids:
                target_ids_item = target_ids_item_data.to_dict()
                target_ids.append(target_ids_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_ids is not UNSET:
            field_dict["deviceIds"] = device_ids
        if id is not UNSET:
            field_dict["id"] = id
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if job_entity is not UNSET:
            field_dict["jobEntity"] = job_entity
        if target_ids is not UNSET:
            field_dict["targetIds"] = target_ids
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_activity_logs_body_selector_job_entity import PostV1ActivityLogsBodySelectorJobEntity
        from ..models.post_v1_activity_logs_body_selector_target_ids_item import (
            PostV1ActivityLogsBodySelectorTargetIdsItem,
        )

        d = src_dict.copy()
        device_ids = cast(list[str], d.pop("deviceIds", UNSET))

        id = d.pop("id", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        _job_entity = d.pop("jobEntity", UNSET)
        job_entity: Union[Unset, PostV1ActivityLogsBodySelectorJobEntity]
        if isinstance(_job_entity, Unset):
            job_entity = UNSET
        else:
            job_entity = PostV1ActivityLogsBodySelectorJobEntity.from_dict(_job_entity)

        target_ids = []
        _target_ids = d.pop("targetIds", UNSET)
        for target_ids_item_data in _target_ids or []:
            target_ids_item = PostV1ActivityLogsBodySelectorTargetIdsItem.from_dict(target_ids_item_data)

            target_ids.append(target_ids_item)

        type_ = d.pop("type", UNSET)

        post_v1_activity_logs_body_selector = cls(
            device_ids=device_ids,
            id=id,
            in_progress=in_progress,
            job_entity=job_entity,
            target_ids=target_ids,
            type_=type_,
        )

        post_v1_activity_logs_body_selector.additional_properties = d
        return post_v1_activity_logs_body_selector

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
