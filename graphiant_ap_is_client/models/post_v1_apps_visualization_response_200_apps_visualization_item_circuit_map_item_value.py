from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item_value_stats import (
        PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats,
    )


T = TypeVar("T", bound="PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValue")


@_attrs_define
class PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValue:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        stats (Union[Unset, PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats]):
        usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        usage_pct (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    name: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    stats: Union[Unset, "PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats"] = UNSET
    usage: Union[Unset, str] = UNSET
    usage_pct: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sla_class = self.sla_class

        stats: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        usage = self.usage

        usage_pct = self.usage_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if stats is not UNSET:
            field_dict["stats"] = stats
        if usage is not UNSET:
            field_dict["usage"] = usage
        if usage_pct is not UNSET:
            field_dict["usagePct"] = usage_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item_value_stats import (
            PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Union[Unset, PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats]
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = PostV1AppsVisualizationResponse200AppsVisualizationItemCircuitMapItemValueStats.from_dict(_stats)

        usage = d.pop("usage", UNSET)

        usage_pct = d.pop("usagePct", UNSET)

        post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item_value = cls(
            name=name,
            sla_class=sla_class,
            stats=stats,
            usage=usage,
            usage_pct=usage_pct,
        )

        post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item_value.additional_properties = d
        return post_v1_apps_visualization_response_200_apps_visualization_item_circuit_map_item_value

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
