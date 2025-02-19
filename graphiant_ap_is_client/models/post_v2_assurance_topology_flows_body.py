from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_flows_body_time_window import PostV2AssuranceTopologyFlowsBodyTimeWindow


T = TypeVar("T", bound="PostV2AssuranceTopologyFlowsBody")


@_attrs_define
class PostV2AssuranceTopologyFlowsBody:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        time_window (Union[Unset, PostV2AssuranceTopologyFlowsBodyTimeWindow]):
        topology_id (Union[Unset, str]):  Example: TYPE_INT32.
        topology_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    app_name: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2AssuranceTopologyFlowsBodyTimeWindow"] = UNSET
    topology_id: Union[Unset, str] = UNSET
    topology_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        topology_id = self.topology_id

        topology_type = self.topology_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window
        if topology_id is not UNSET:
            field_dict["topologyId"] = topology_id
        if topology_type is not UNSET:
            field_dict["topologyType"] = topology_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_flows_body_time_window import (
            PostV2AssuranceTopologyFlowsBodyTimeWindow,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceTopologyFlowsBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceTopologyFlowsBodyTimeWindow.from_dict(_time_window)

        topology_id = d.pop("topologyId", UNSET)

        topology_type = d.pop("topologyType", UNSET)

        post_v2_assurance_topology_flows_body = cls(
            app_name=app_name,
            time_window=time_window,
            topology_id=topology_id,
            topology_type=topology_type,
        )

        post_v2_assurance_topology_flows_body.additional_properties = d
        return post_v2_assurance_topology_flows_body

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
