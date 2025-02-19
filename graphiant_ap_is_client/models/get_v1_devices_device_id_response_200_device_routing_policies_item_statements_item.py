from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item_actions_item import (
        GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemActionsItem,
    )
    from ..models.get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item_matches_item import (
        GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemMatchesItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItem")


@_attrs_define
class GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItem:
    """
    Attributes:
        actions (Union[Unset,
            list['GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemActionsItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        matches (Union[Unset,
            list['GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemMatchesItem']]):
        seq (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    actions: Union[Unset, list["GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemActionsItem"]] = (
        UNSET
    )
    id: Union[Unset, str] = UNSET
    matches: Union[Unset, list["GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemMatchesItem"]] = (
        UNSET
    )
    seq: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        id = self.id

        matches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matches, Unset):
            matches = []
            for matches_item_data in self.matches:
                matches_item = matches_item_data.to_dict()
                matches.append(matches_item)

        seq = self.seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if id is not UNSET:
            field_dict["id"] = id
        if matches is not UNSET:
            field_dict["matches"] = matches
        if seq is not UNSET:
            field_dict["seq"] = seq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item_actions_item import (
            GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemActionsItem,
        )
        from ..models.get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item_matches_item import (
            GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemMatchesItem,
        )

        d = src_dict.copy()
        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemActionsItem.from_dict(
                actions_item_data
            )

            actions.append(actions_item)

        id = d.pop("id", UNSET)

        matches = []
        _matches = d.pop("matches", UNSET)
        for matches_item_data in _matches or []:
            matches_item = GetV1DevicesDeviceIdResponse200DeviceRoutingPoliciesItemStatementsItemMatchesItem.from_dict(
                matches_item_data
            )

            matches.append(matches_item)

        seq = d.pop("seq", UNSET)

        get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item = cls(
            actions=actions,
            id=id,
            matches=matches,
            seq=seq,
        )

        get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item.additional_properties = d
        return get_v1_devices_device_id_response_200_device_routing_policies_item_statements_item

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
