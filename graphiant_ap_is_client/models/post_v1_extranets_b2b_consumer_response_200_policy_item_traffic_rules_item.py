from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item_action import (
        PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction,
    )
    from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item_match import (
        PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch,
    )


T = TypeVar("T", bound="PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItem")


@_attrs_define
class PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItem:
    """
    Attributes:
        action (Union[Unset, PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction]):
        match (Union[Unset, PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch]):
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    action: Union[Unset, "PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction"] = UNSET
    match: Union[Unset, "PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch"] = UNSET
    seq: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        seq = self.seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if match is not UNSET:
            field_dict["match"] = match
        if seq is not UNSET:
            field_dict["seq"] = seq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item_action import (
            PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction,
        )
        from ..models.post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item_match import (
            PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch,
        )

        d = src_dict.copy()
        _action = d.pop("action", UNSET)
        action: Union[Unset, PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction]
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemAction.from_dict(_action)

        _match = d.pop("match", UNSET)
        match: Union[Unset, PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = PostV1ExtranetsB2BConsumerResponse200PolicyItemTrafficRulesItemMatch.from_dict(_match)

        seq = d.pop("seq", UNSET)

        post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item = cls(
            action=action,
            match=match,
            seq=seq,
        )

        post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item.additional_properties = d
        return post_v1_extranets_b2b_consumer_response_200_policy_item_traffic_rules_item

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
