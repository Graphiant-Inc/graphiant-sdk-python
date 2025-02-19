from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_flows_topology_body_app_selector import PostV1FlowsTopologyBodyAppSelector
    from ..models.post_v1_flows_topology_body_time_window import PostV1FlowsTopologyBodyTimeWindow


T = TypeVar("T", bound="PostV1FlowsTopologyBody")


@_attrs_define
class PostV1FlowsTopologyBody:
    """
    Attributes:
        app_selector (Union[Unset, PostV1FlowsTopologyBodyAppSelector]):
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        time_window (Union[Unset, PostV1FlowsTopologyBodyTimeWindow]):
    """

    app_selector: Union[Unset, "PostV1FlowsTopologyBodyAppSelector"] = UNSET
    device_id: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1FlowsTopologyBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_selector, Unset):
            app_selector = self.app_selector.to_dict()

        device_id = self.device_id

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_selector is not UNSET:
            field_dict["appSelector"] = app_selector
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_flows_topology_body_app_selector import PostV1FlowsTopologyBodyAppSelector
        from ..models.post_v1_flows_topology_body_time_window import PostV1FlowsTopologyBodyTimeWindow

        d = src_dict.copy()
        _app_selector = d.pop("appSelector", UNSET)
        app_selector: Union[Unset, PostV1FlowsTopologyBodyAppSelector]
        if isinstance(_app_selector, Unset):
            app_selector = UNSET
        else:
            app_selector = PostV1FlowsTopologyBodyAppSelector.from_dict(_app_selector)

        device_id = d.pop("deviceId", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1FlowsTopologyBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1FlowsTopologyBodyTimeWindow.from_dict(_time_window)

        post_v1_flows_topology_body = cls(
            app_selector=app_selector,
            device_id=device_id,
            time_window=time_window,
        )

        post_v1_flows_topology_body.additional_properties = d
        return post_v1_flows_topology_body

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
