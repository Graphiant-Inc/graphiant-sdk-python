from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_routing_policies_item_statements_item import (
        PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItemStatementsItem,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItem")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItem:
    """
    Attributes:
        attach_point (Union[Unset, str]):  Example: TYPE_ENUM.
        default_action (Union[Unset, str]):  Example: TYPE_ENUM.
        description (Union[Unset, str]):  Example: TYPE_STRING.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        global_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        statements (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItemStatementsItem']]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    attach_point: Union[Unset, str] = UNSET
    default_action: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    global_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    statements: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItemStatementsItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attach_point = self.attach_point

        default_action = self.default_action

        description = self.description

        error_message = self.error_message

        global_id = self.global_id

        id = self.id

        name = self.name

        statements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attach_point is not UNSET:
            field_dict["attachPoint"] = attach_point
        if default_action is not UNSET:
            field_dict["defaultAction"] = default_action
        if description is not UNSET:
            field_dict["description"] = description
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if statements is not UNSET:
            field_dict["statements"] = statements
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_routing_policies_item_statements_item import (
            PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItemStatementsItem,
        )

        d = src_dict.copy()
        attach_point = d.pop("attachPoint", UNSET)

        default_action = d.pop("defaultAction", UNSET)

        description = d.pop("description", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        statements = []
        _statements = d.pop("statements", UNSET)
        for statements_item_data in _statements or []:
            statements_item = PostV1DevicesDeviceIdDraftBodyDraftRoutingPoliciesItemStatementsItem.from_dict(
                statements_item_data
            )

            statements.append(statements_item)

        status = d.pop("status", UNSET)

        post_v1_devices_device_id_draft_body_draft_routing_policies_item = cls(
            attach_point=attach_point,
            default_action=default_action,
            description=description,
            error_message=error_message,
            global_id=global_id,
            id=id,
            name=name,
            statements=statements,
            status=status,
        )

        post_v1_devices_device_id_draft_body_draft_routing_policies_item.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_routing_policies_item

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
