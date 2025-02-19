from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_availability_item import (
        PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem,
    )
    from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item import (
        PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItem,
    )


T = TypeVar("T", bound="PostV1AppsVisualizationResponse200AppsVisualizationItem")


@_attrs_define
class PostV1AppsVisualizationResponse200AppsVisualizationItem:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_availability (Union[Unset,
            list['PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem']]):
        circuit_map (Union[Unset, list['PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItem']]):
        current_status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    app_id: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    circuit_availability: Union[
        Unset, list["PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem"]
    ] = UNSET
    circuit_map: Union[Unset, list["PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItem"]] = UNSET
    current_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        circuit_availability: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_availability, Unset):
            circuit_availability = []
            for circuit_availability_item_data in self.circuit_availability:
                circuit_availability_item = circuit_availability_item_data.to_dict()
                circuit_availability.append(circuit_availability_item)

        circuit_map: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.circuit_map, Unset):
            circuit_map = []
            for circuit_map_item_data in self.circuit_map:
                circuit_map_item = circuit_map_item_data.to_dict()
                circuit_map.append(circuit_map_item)

        current_status = self.current_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if circuit_availability is not UNSET:
            field_dict["circuitAvailability"] = circuit_availability
        if circuit_map is not UNSET:
            field_dict["circuitMap"] = circuit_map
        if current_status is not UNSET:
            field_dict["currentStatus"] = current_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_availability_item import (
            PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem,
        )
        from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item import (
            PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItem,
        )

        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        app_name = d.pop("appName", UNSET)

        circuit_availability = []
        _circuit_availability = d.pop("circuitAvailability", UNSET)
        for circuit_availability_item_data in _circuit_availability or []:
            circuit_availability_item = (
                PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem.from_dict(
                    circuit_availability_item_data
                )
            )

            circuit_availability.append(circuit_availability_item)

        circuit_map = []
        _circuit_map = d.pop("circuitMap", UNSET)
        for circuit_map_item_data in _circuit_map or []:
            circuit_map_item = PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItem.from_dict(
                circuit_map_item_data
            )

            circuit_map.append(circuit_map_item)

        current_status = d.pop("currentStatus", UNSET)

        post_v1_apps_visualization_response_200_apps_visualization_item = cls(
            app_id=app_id,
            app_name=app_name,
            circuit_availability=circuit_availability,
            circuit_map=circuit_map,
            current_status=current_status,
        )

        post_v1_apps_visualization_response_200_apps_visualization_item.additional_properties = d
        return post_v1_apps_visualization_response_200_apps_visualization_item

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
