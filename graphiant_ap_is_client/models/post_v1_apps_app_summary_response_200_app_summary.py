from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_app_summary_response_200_app_summary_app_health_item import (
        PostV1AppsAppSummaryResponse200AppSummaryAppHealthItem,
    )
    from ..models.post_v1_apps_app_summary_response_200_app_summary_app_incidents import (
        PostV1AppsAppSummaryResponse200AppSummaryAppIncidents,
    )
    from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item import (
        PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem,
    )
    from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item import (
        PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item,
    )


T = TypeVar("T", bound="PostV1AppsAppSummaryResponse200AppSummary")


@_attrs_define
class PostV1AppsAppSummaryResponse200AppSummary:
    """
    Attributes:
        app_health (Union[Unset, list['PostV1AppsAppSummaryResponse200AppSummaryAppHealthItem']]):
        app_incidents (Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryAppIncidents]):
        apps_on_device_count (Union[Unset, str]):  Example: TYPE_UINT32.
        average_qoe (Union[Unset, str]):  Example: TYPE_DOUBLE.
        circuits_incidents (Union[Unset, list['PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem']]):
        circuits_incidentsv_2 (Union[Unset, list['PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item']]):
    """

    app_health: Union[Unset, list["PostV1AppsAppSummaryResponse200AppSummaryAppHealthItem"]] = UNSET
    app_incidents: Union[Unset, "PostV1AppsAppSummaryResponse200AppSummaryAppIncidents"] = UNSET
    apps_on_device_count: Union[Unset, str] = UNSET
    average_qoe: Union[Unset, str] = UNSET
    circuits_incidents: Union[Unset, list["PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem"]] = UNSET
    circuits_incidentsv_2: Union[Unset, list["PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item"]] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_health: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.app_health, Unset):
            app_health = []
            for app_health_item_data in self.app_health:
                app_health_item = app_health_item_data.to_dict()
                app_health.append(app_health_item)

        app_incidents: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_incidents, Unset):
            app_incidents = self.app_incidents.to_dict()

        apps_on_device_count = self.apps_on_device_count

        average_qoe = self.average_qoe

        circuits_incidents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits_incidents, Unset):
            circuits_incidents = []
            for circuits_incidents_item_data in self.circuits_incidents:
                circuits_incidents_item = circuits_incidents_item_data.to_dict()
                circuits_incidents.append(circuits_incidents_item)

        circuits_incidentsv_2: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits_incidentsv_2, Unset):
            circuits_incidentsv_2 = []
            for circuits_incidentsv_2_item_data in self.circuits_incidentsv_2:
                circuits_incidentsv_2_item = circuits_incidentsv_2_item_data.to_dict()
                circuits_incidentsv_2.append(circuits_incidentsv_2_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_health is not UNSET:
            field_dict["appHealth"] = app_health
        if app_incidents is not UNSET:
            field_dict["appIncidents"] = app_incidents
        if apps_on_device_count is not UNSET:
            field_dict["appsOnDeviceCount"] = apps_on_device_count
        if average_qoe is not UNSET:
            field_dict["averageQoe"] = average_qoe
        if circuits_incidents is not UNSET:
            field_dict["circuitsIncidents"] = circuits_incidents
        if circuits_incidentsv_2 is not UNSET:
            field_dict["circuitsIncidentsv2"] = circuits_incidentsv_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_app_summary_response_200_app_summary_app_health_item import (
            PostV1AppsAppSummaryResponse200AppSummaryAppHealthItem,
        )
        from ..models.post_v1_apps_app_summary_response_200_app_summary_app_incidents import (
            PostV1AppsAppSummaryResponse200AppSummaryAppIncidents,
        )
        from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidents_item import (
            PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem,
        )
        from ..models.post_v1_apps_app_summary_response_200_app_summary_circuits_incidentsv_2_item import (
            PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item,
        )

        d = src_dict.copy()
        app_health = []
        _app_health = d.pop("appHealth", UNSET)
        for app_health_item_data in _app_health or []:
            app_health_item = PostV1AppsAppSummaryResponse200AppSummaryAppHealthItem.from_dict(app_health_item_data)

            app_health.append(app_health_item)

        _app_incidents = d.pop("appIncidents", UNSET)
        app_incidents: Union[Unset, PostV1AppsAppSummaryResponse200AppSummaryAppIncidents]
        if isinstance(_app_incidents, Unset):
            app_incidents = UNSET
        else:
            app_incidents = PostV1AppsAppSummaryResponse200AppSummaryAppIncidents.from_dict(_app_incidents)

        apps_on_device_count = d.pop("appsOnDeviceCount", UNSET)

        average_qoe = d.pop("averageQoe", UNSET)

        circuits_incidents = []
        _circuits_incidents = d.pop("circuitsIncidents", UNSET)
        for circuits_incidents_item_data in _circuits_incidents or []:
            circuits_incidents_item = PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsItem.from_dict(
                circuits_incidents_item_data
            )

            circuits_incidents.append(circuits_incidents_item)

        circuits_incidentsv_2 = []
        _circuits_incidentsv_2 = d.pop("circuitsIncidentsv2", UNSET)
        for circuits_incidentsv_2_item_data in _circuits_incidentsv_2 or []:
            circuits_incidentsv_2_item = PostV1AppsAppSummaryResponse200AppSummaryCircuitsIncidentsv2Item.from_dict(
                circuits_incidentsv_2_item_data
            )

            circuits_incidentsv_2.append(circuits_incidentsv_2_item)

        post_v1_apps_app_summary_response_200_app_summary = cls(
            app_health=app_health,
            app_incidents=app_incidents,
            apps_on_device_count=apps_on_device_count,
            average_qoe=average_qoe,
            circuits_incidents=circuits_incidents,
            circuits_incidentsv_2=circuits_incidentsv_2,
        )

        post_v1_apps_app_summary_response_200_app_summary.additional_properties = d
        return post_v1_apps_app_summary_response_200_app_summary

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
