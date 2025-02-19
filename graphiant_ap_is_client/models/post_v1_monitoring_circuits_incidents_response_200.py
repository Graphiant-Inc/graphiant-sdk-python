from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_monitoring_circuits_incidents_response_200_circuits_incidents_item import (
        PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItem,
    )


T = TypeVar("T", bound="PostV1MonitoringCircuitsIncidentsResponse200")


@_attrs_define
class PostV1MonitoringCircuitsIncidentsResponse200:
    """
    Attributes:
        circuits_incidents (Union[Unset, list['PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItem']]):
    """

    circuits_incidents: Union[Unset, list["PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuits_incidents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuits_incidents, Unset):
            circuits_incidents = []
            for circuits_incidents_item_data in self.circuits_incidents:
                circuits_incidents_item = circuits_incidents_item_data.to_dict()
                circuits_incidents.append(circuits_incidents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuits_incidents is not UNSET:
            field_dict["circuitsIncidents"] = circuits_incidents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_monitoring_circuits_incidents_response_200_circuits_incidents_item import (
            PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItem,
        )

        d = src_dict.copy()
        circuits_incidents = []
        _circuits_incidents = d.pop("circuitsIncidents", UNSET)
        for circuits_incidents_item_data in _circuits_incidents or []:
            circuits_incidents_item = PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItem.from_dict(
                circuits_incidents_item_data
            )

            circuits_incidents.append(circuits_incidents_item)

        post_v1_monitoring_circuits_incidents_response_200 = cls(
            circuits_incidents=circuits_incidents,
        )

        post_v1_monitoring_circuits_incidents_response_200.additional_properties = d
        return post_v1_monitoring_circuits_incidents_response_200

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
