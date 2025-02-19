from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem")


@_attrs_define
class PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitAvailabilityItem:
    """
    Attributes:
        key (Union[Unset, str]):  Example: TYPE_STRING.
        value (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        post_v1_apps_visualization_response_200_apps_visualization_item_circuit_availability_item = cls(
            key=key,
            value=value,
        )

        post_v1_apps_visualization_response_200_apps_visualization_item_circuit_availability_item.additional_properties = d
        return post_v1_apps_visualization_response_200_apps_visualization_item_circuit_availability_item

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
