from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_visualization_response_200_app_health_item import (
        PostV1AppsVisualizationResponse200AppHealthItem,
    )
    from ..models.post_v1_apps_visualization_response_200_apps_visualization_item import (
        PostV1AppsVisualizationResponse200AppsVisualizationItem,
    )


T = TypeVar("T", bound="PostV1AppsVisualizationResponse200")


@_attrs_define
class PostV1AppsVisualizationResponse200:
    """
    Attributes:
        app_health (Union[Unset, list['PostV1AppsVisualizationResponse200AppHealthItem']]):
        apps_on_device_count (Union[Unset, str]):  Example: TYPE_UINT32.
        apps_visualization (Union[Unset, list['PostV1AppsVisualizationResponse200AppsVisualizationItem']]):
        average_qoe (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    app_health: Union[Unset, list["PostV1AppsVisualizationResponse200AppHealthItem"]] = UNSET
    apps_on_device_count: Union[Unset, str] = UNSET
    apps_visualization: Union[Unset, list["PostV1AppsVisualizationResponse200AppsVisualizationItem"]] = UNSET
    average_qoe: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_health: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_health, Unset):
            app_health = []
            for app_health_item_data in self.app_health:
                app_health_item = app_health_item_data.to_dict()
                app_health.append(app_health_item)

        apps_on_device_count = self.apps_on_device_count

        apps_visualization: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.apps_visualization, Unset):
            apps_visualization = []
            for apps_visualization_item_data in self.apps_visualization:
                apps_visualization_item = apps_visualization_item_data.to_dict()
                apps_visualization.append(apps_visualization_item)

        average_qoe = self.average_qoe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_health is not UNSET:
            field_dict["appHealth"] = app_health
        if apps_on_device_count is not UNSET:
            field_dict["appsOnDeviceCount"] = apps_on_device_count
        if apps_visualization is not UNSET:
            field_dict["appsVisualization"] = apps_visualization
        if average_qoe is not UNSET:
            field_dict["averageQoe"] = average_qoe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_visualization_response_200_app_health_item import (
            PostV1AppsVisualizationResponse200AppHealthItem,
        )
        from ..models.post_v1_apps_visualization_response_200_apps_visualization_item import (
            PostV1AppsVisualizationResponse200AppsVisualizationItem,
        )

        d = src_dict.copy()
        app_health = []
        _app_health = d.pop("appHealth", UNSET)
        for app_health_item_data in _app_health or []:
            app_health_item = PostV1AppsVisualizationResponse200AppHealthItem.from_dict(app_health_item_data)

            app_health.append(app_health_item)

        apps_on_device_count = d.pop("appsOnDeviceCount", UNSET)

        apps_visualization = []
        _apps_visualization = d.pop("appsVisualization", UNSET)
        for apps_visualization_item_data in _apps_visualization or []:
            apps_visualization_item = PostV1AppsVisualizationResponse200AppsVisualizationItem.from_dict(
                apps_visualization_item_data
            )

            apps_visualization.append(apps_visualization_item)

        average_qoe = d.pop("averageQoe", UNSET)

        post_v1_apps_visualization_response_200 = cls(
            app_health=app_health,
            apps_on_device_count=apps_on_device_count,
            apps_visualization=apps_visualization,
            average_qoe=average_qoe,
        )

        post_v1_apps_visualization_response_200.additional_properties = d
        return post_v1_apps_visualization_response_200

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
