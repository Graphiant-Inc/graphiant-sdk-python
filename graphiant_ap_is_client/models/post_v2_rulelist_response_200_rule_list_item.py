from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2RulelistResponse200RuleListItem")


@_attrs_define
class PostV2RulelistResponse200RuleListItem:
    """
    Attributes:
        alarm_clear (Union[Unset, str]):  Example: TYPE_STRING.
        alarm_set (Union[Unset, str]):  Example: TYPE_STRING.
        allow_count (Union[Unset, str]):  Example: TYPE_INT64.
        category (Union[Unset, str]):  Example: TYPE_STRING.
        enabled (Union[Unset, str]):  Example: TYPE_BOOL.
        plane (Union[Unset, str]):  Example: TYPE_ENUM.
        priority (Union[Unset, str]):  Example: 10000000.
        rule_id (Union[Unset, str]):  Example: TYPE_STRING.
        rule_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    alarm_clear: Union[Unset, str] = UNSET
    alarm_set: Union[Unset, str] = UNSET
    allow_count: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    enabled: Union[Unset, str] = UNSET
    plane: Union[Unset, str] = UNSET
    priority: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    rule_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alarm_clear = self.alarm_clear

        alarm_set = self.alarm_set

        allow_count = self.allow_count

        category = self.category

        enabled = self.enabled

        plane = self.plane

        priority = self.priority

        rule_id = self.rule_id

        rule_name = self.rule_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alarm_clear is not UNSET:
            field_dict["alarmClear"] = alarm_clear
        if alarm_set is not UNSET:
            field_dict["alarmSet"] = alarm_set
        if allow_count is not UNSET:
            field_dict["allowCount"] = allow_count
        if category is not UNSET:
            field_dict["category"] = category
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if plane is not UNSET:
            field_dict["plane"] = plane
        if priority is not UNSET:
            field_dict["priority"] = priority
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alarm_clear = d.pop("alarmClear", UNSET)

        alarm_set = d.pop("alarmSet", UNSET)

        allow_count = d.pop("allowCount", UNSET)

        category = d.pop("category", UNSET)

        enabled = d.pop("enabled", UNSET)

        plane = d.pop("plane", UNSET)

        priority = d.pop("priority", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        rule_name = d.pop("ruleName", UNSET)

        post_v2_rulelist_response_200_rule_list_item = cls(
            alarm_clear=alarm_clear,
            alarm_set=alarm_set,
            allow_count=allow_count,
            category=category,
            enabled=enabled,
            plane=plane,
            priority=priority,
            rule_id=rule_id,
            rule_name=rule_name,
        )

        post_v2_rulelist_response_200_rule_list_item.additional_properties = d
        return post_v2_rulelist_response_200_rule_list_item

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
