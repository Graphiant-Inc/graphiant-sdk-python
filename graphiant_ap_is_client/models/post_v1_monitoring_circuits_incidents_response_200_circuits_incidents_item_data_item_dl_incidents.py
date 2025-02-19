from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItemDataItemDlIncidents")


@_attrs_define
class PostV1MonitoringCircuitsIncidentsResponse200CircuitsIncidentsItemDataItemDlIncidents:
    """
    Attributes:
        num_fair_incidents (Union[Unset, str]):  Example: TYPE_UINT32.
        num_poor_incidents (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    num_fair_incidents: Union[Unset, str] = UNSET
    num_poor_incidents: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_fair_incidents = self.num_fair_incidents

        num_poor_incidents = self.num_poor_incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_fair_incidents is not UNSET:
            field_dict["numFairIncidents"] = num_fair_incidents
        if num_poor_incidents is not UNSET:
            field_dict["numPoorIncidents"] = num_poor_incidents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        num_fair_incidents = d.pop("numFairIncidents", UNSET)

        num_poor_incidents = d.pop("numPoorIncidents", UNSET)

        post_v1_monitoring_circuits_incidents_response_200_circuits_incidents_item_data_item_dl_incidents = cls(
            num_fair_incidents=num_fair_incidents,
            num_poor_incidents=num_poor_incidents,
        )

        post_v1_monitoring_circuits_incidents_response_200_circuits_incidents_item_data_item_dl_incidents.additional_properties = d
        return post_v1_monitoring_circuits_incidents_response_200_circuits_incidents_item_data_item_dl_incidents

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
