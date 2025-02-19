from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_audit_logs_body_selector_entities_item import PostV2AuditLogsBodySelectorEntitiesItem
    from ..models.post_v2_audit_logs_body_selector_targets_item import PostV2AuditLogsBodySelectorTargetsItem


T = TypeVar("T", bound="PostV2AuditLogsBodySelector")


@_attrs_define
class PostV2AuditLogsBodySelector:
    """
    Attributes:
        categories (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
        entities (Union[Unset, list['PostV2AuditLogsBodySelectorEntitiesItem']]):
        job_types (Union[Unset, list[str]]):  Example: ['TYPE_ENUM'].
        targets (Union[Unset, list['PostV2AuditLogsBodySelectorTargetsItem']]):
        users (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    categories: Union[Unset, list[str]] = UNSET
    entities: Union[Unset, list["PostV2AuditLogsBodySelectorEntitiesItem"]] = UNSET
    job_types: Union[Unset, list[str]] = UNSET
    targets: Union[Unset, list["PostV2AuditLogsBodySelectorTargetsItem"]] = UNSET
    users: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        entities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        job_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.job_types, Unset):
            job_types = self.job_types

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        users: Union[Unset, list[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if entities is not UNSET:
            field_dict["entities"] = entities
        if job_types is not UNSET:
            field_dict["jobTypes"] = job_types
        if targets is not UNSET:
            field_dict["targets"] = targets
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_audit_logs_body_selector_entities_item import PostV2AuditLogsBodySelectorEntitiesItem
        from ..models.post_v2_audit_logs_body_selector_targets_item import PostV2AuditLogsBodySelectorTargetsItem

        d = src_dict.copy()
        categories = cast(list[str], d.pop("categories", UNSET))

        entities = []
        _entities = d.pop("entities", UNSET)
        for entities_item_data in _entities or []:
            entities_item = PostV2AuditLogsBodySelectorEntitiesItem.from_dict(entities_item_data)

            entities.append(entities_item)

        job_types = cast(list[str], d.pop("jobTypes", UNSET))

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = PostV2AuditLogsBodySelectorTargetsItem.from_dict(targets_item_data)

            targets.append(targets_item)

        users = cast(list[str], d.pop("users", UNSET))

        post_v2_audit_logs_body_selector = cls(
            categories=categories,
            entities=entities,
            job_types=job_types,
            targets=targets,
            users=users,
        )

        post_v2_audit_logs_body_selector.additional_properties = d
        return post_v2_audit_logs_body_selector

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
