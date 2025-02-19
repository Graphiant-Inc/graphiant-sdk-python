from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_flow_table_body_cursor_ref import PostV1FlowsFlowTableBodyCursorRef
    from ..models.post_v1_flows_flow_table_body_selector import PostV1FlowsFlowTableBodySelector
    from ..models.post_v1_flows_flow_table_body_time_window import PostV1FlowsFlowTableBodyTimeWindow


T = TypeVar("T", bound="PostV1FlowsFlowTableBody")


@_attrs_define
class PostV1FlowsFlowTableBody:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        cursor_ref (Union[Unset, PostV1FlowsFlowTableBodyCursorRef]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_dia (Union[Unset, str]):  Example: TYPE_BOOL.
        num_flow_records (Union[Unset, str]):  Example: TYPE_UINT32.
        selector (Union[Unset, PostV1FlowsFlowTableBodySelector]):
        time_window (Union[Unset, PostV1FlowsFlowTableBodyTimeWindow]):
    """

    app_id: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    cursor_ref: Union[Unset, "PostV1FlowsFlowTableBodyCursorRef"] = UNSET
    device_id: Union[Unset, str] = UNSET
    is_dia: Union[Unset, str] = UNSET
    num_flow_records: Union[Unset, str] = UNSET
    selector: Union[Unset, "PostV1FlowsFlowTableBodySelector"] = UNSET
    time_window: Union[Unset, "PostV1FlowsFlowTableBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        cursor_ref: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cursor_ref, Unset):
            cursor_ref = self.cursor_ref.to_dict()

        device_id = self.device_id

        is_dia = self.is_dia

        num_flow_records = self.num_flow_records

        selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if cursor_ref is not UNSET:
            field_dict["cursorRef"] = cursor_ref
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if is_dia is not UNSET:
            field_dict["isDia"] = is_dia
        if num_flow_records is not UNSET:
            field_dict["numFlowRecords"] = num_flow_records
        if selector is not UNSET:
            field_dict["selector"] = selector
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_flow_table_body_cursor_ref import PostV1FlowsFlowTableBodyCursorRef
        from ..models.post_v1_flows_flow_table_body_selector import PostV1FlowsFlowTableBodySelector
        from ..models.post_v1_flows_flow_table_body_time_window import PostV1FlowsFlowTableBodyTimeWindow

        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        app_name = d.pop("appName", UNSET)

        _cursor_ref = d.pop("cursorRef", UNSET)
        cursor_ref: Union[Unset, PostV1FlowsFlowTableBodyCursorRef]
        if isinstance(_cursor_ref, Unset):
            cursor_ref = UNSET
        else:
            cursor_ref = PostV1FlowsFlowTableBodyCursorRef.from_dict(_cursor_ref)

        device_id = d.pop("deviceId", UNSET)

        is_dia = d.pop("isDia", UNSET)

        num_flow_records = d.pop("numFlowRecords", UNSET)

        _selector = d.pop("selector", UNSET)
        selector: Union[Unset, PostV1FlowsFlowTableBodySelector]
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PostV1FlowsFlowTableBodySelector.from_dict(_selector)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1FlowsFlowTableBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1FlowsFlowTableBodyTimeWindow.from_dict(_time_window)

        post_v1_flows_flow_table_body = cls(
            app_id=app_id,
            app_name=app_name,
            cursor_ref=cursor_ref,
            device_id=device_id,
            is_dia=is_dia,
            num_flow_records=num_flow_records,
            selector=selector,
            time_window=time_window,
        )

        post_v1_flows_flow_table_body.additional_properties = d
        return post_v1_flows_flow_table_body

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
