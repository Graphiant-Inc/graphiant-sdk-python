from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_flow_table_response_200_cursor_ref import PostV1FlowsFlowTableResponse200CursorRef
    from ..models.post_v1_flows_flow_table_response_200_flow_table_item import (
        PostV1FlowsFlowTableResponse200FlowTableItem,
    )


T = TypeVar("T", bound="PostV1FlowsFlowTableResponse200")


@_attrs_define
class PostV1FlowsFlowTableResponse200:
    """
    Attributes:
        cursor_ref (Union[Unset, PostV1FlowsFlowTableResponse200CursorRef]):
        flow_table (Union[Unset, list['PostV1FlowsFlowTableResponse200FlowTableItem']]):
    """

    cursor_ref: Union[Unset, "PostV1FlowsFlowTableResponse200CursorRef"] = UNSET
    flow_table: Union[Unset, list["PostV1FlowsFlowTableResponse200FlowTableItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cursor_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cursor_ref, Unset):
            cursor_ref = self.cursor_ref.to_dict()

        flow_table: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.flow_table, Unset):
            flow_table = []
            for flow_table_item_data in self.flow_table:
                flow_table_item = flow_table_item_data.to_dict()
                flow_table.append(flow_table_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if flow_table is not UNSET:
            field_dict["flowTable"] = flow_table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_flow_table_response_200_cursor_ref import PostV1FlowsFlowTableResponse200CursorRef
        from ..models.post_v1_flows_flow_table_response_200_flow_table_item import (
            PostV1FlowsFlowTableResponse200FlowTableItem,
        )

        d = src_dict.copy()
        _cursor_ref = d.pop("cursorRef", UNSET)
        cursor_ref: Union[Unset, PostV1FlowsFlowTableResponse200CursorRef]
        if isinstance(_cursor_ref, Unset):
            cursor_ref = UNSET
        else:
            cursor_ref = PostV1FlowsFlowTableResponse200CursorRef.from_dict(_cursor_ref)

        flow_table = []
        _flow_table = d.pop("flowTable", UNSET)
        for flow_table_item_data in _flow_table or []:
            flow_table_item = PostV1FlowsFlowTableResponse200FlowTableItem.from_dict(flow_table_item_data)

            flow_table.append(flow_table_item)

        post_v1_flows_flow_table_response_200 = cls(
            cursor_ref=cursor_ref,
            flow_table=flow_table,
        )

        post_v1_flows_flow_table_response_200.additional_properties = d
        return post_v1_flows_flow_table_response_200

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
