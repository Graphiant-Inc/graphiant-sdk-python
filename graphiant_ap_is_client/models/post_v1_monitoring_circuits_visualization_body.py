from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_monitoring_circuits_visualization_body_selectors_item import (
        PostV1MonitoringCircuitsVisualizationBodySelectorsItem,
    )
    from ..models.post_v1_monitoring_circuits_visualization_body_time_window import (
        PostV1MonitoringCircuitsVisualizationBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV1MonitoringCircuitsVisualizationBody")


@_attrs_define
class PostV1MonitoringCircuitsVisualizationBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_UINT64.
        selectors (Union[Unset, list['PostV1MonitoringCircuitsVisualizationBodySelectorsItem']]):
        time_window (Union[Unset, PostV1MonitoringCircuitsVisualizationBodyTimeWindow]):
    """

    device_id: Union[Unset, str] = UNSET
    selectors: Union[Unset, list["PostV1MonitoringCircuitsVisualizationBodySelectorsItem"]] = UNSET
    time_window: Union[Unset, "PostV1MonitoringCircuitsVisualizationBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        selectors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.selectors, Unset):
            selectors = []
            for selectors_item_data in self.selectors:
                selectors_item = selectors_item_data.to_dict()
                selectors.append(selectors_item)

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if selectors is not UNSET:
            field_dict["selectors"] = selectors
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_monitoring_circuits_visualization_body_selectors_item import (
            PostV1MonitoringCircuitsVisualizationBodySelectorsItem,
        )
        from ..models.post_v1_monitoring_circuits_visualization_body_time_window import (
            PostV1MonitoringCircuitsVisualizationBodyTimeWindow,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        selectors = []
        _selectors = d.pop("selectors", UNSET)
        for selectors_item_data in _selectors or []:
            selectors_item = PostV1MonitoringCircuitsVisualizationBodySelectorsItem.from_dict(selectors_item_data)

            selectors.append(selectors_item)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1MonitoringCircuitsVisualizationBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1MonitoringCircuitsVisualizationBodyTimeWindow.from_dict(_time_window)

        post_v1_monitoring_circuits_visualization_body = cls(
            device_id=device_id,
            selectors=selectors,
            time_window=time_window,
        )

        post_v1_monitoring_circuits_visualization_body.additional_properties = d
        return post_v1_monitoring_circuits_visualization_body

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
