from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_rulelist_response_200_rule_list_item import PostV2RulelistResponse200RuleListItem


T = TypeVar("T", bound="PostV2RulelistResponse200")


@_attrs_define
class PostV2RulelistResponse200:
    """
    Attributes:
        rule_list (Union[Unset, list['PostV2RulelistResponse200RuleListItem']]):
    """

    rule_list: Union[Unset, list["PostV2RulelistResponse200RuleListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rule_list, Unset):
            rule_list = []
            for rule_list_item_data in self.rule_list:
                rule_list_item = rule_list_item_data.to_dict()
                rule_list.append(rule_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_list is not UNSET:
            field_dict["ruleList"] = rule_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_rulelist_response_200_rule_list_item import PostV2RulelistResponse200RuleListItem

        d = src_dict.copy()
        rule_list = []
        _rule_list = d.pop("ruleList", UNSET)
        for rule_list_item_data in _rule_list or []:
            rule_list_item = PostV2RulelistResponse200RuleListItem.from_dict(rule_list_item_data)

            rule_list.append(rule_list_item)

        post_v2_rulelist_response_200 = cls(
            rule_list=rule_list,
        )

        post_v2_rulelist_response_200.additional_properties = d
        return post_v2_rulelist_response_200

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
