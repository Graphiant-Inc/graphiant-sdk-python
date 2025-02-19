from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AppsUtilizationResponse200AppsUtilizationItem")


@_attrs_define
class PostV1AppsUtilizationResponse200AppsUtilizationItem:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        dl_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        dl_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        dl_usage_pct (Union[Unset, str]):  Example: TYPE_FLOAT.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        ul_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        ul_usage (Union[Unset, str]):  Example: TYPE_DOUBLE.
        ul_usage_pct (Union[Unset, str]):  Example: TYPE_FLOAT.
    """

    app_id: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    dl_circuit_name: Union[Unset, str] = UNSET
    dl_usage: Union[Unset, str] = UNSET
    dl_usage_pct: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    ul_circuit_name: Union[Unset, str] = UNSET
    ul_usage: Union[Unset, str] = UNSET
    ul_usage_pct: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        dl_circuit_name = self.dl_circuit_name

        dl_usage = self.dl_usage

        dl_usage_pct = self.dl_usage_pct

        sla_class = self.sla_class

        ul_circuit_name = self.ul_circuit_name

        ul_usage = self.ul_usage

        ul_usage_pct = self.ul_usage_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if dl_circuit_name is not UNSET:
            field_dict["dlCircuitName"] = dl_circuit_name
        if dl_usage is not UNSET:
            field_dict["dlUsage"] = dl_usage
        if dl_usage_pct is not UNSET:
            field_dict["dlUsagePct"] = dl_usage_pct
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if ul_circuit_name is not UNSET:
            field_dict["ulCircuitName"] = ul_circuit_name
        if ul_usage is not UNSET:
            field_dict["ulUsage"] = ul_usage
        if ul_usage_pct is not UNSET:
            field_dict["ulUsagePct"] = ul_usage_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        app_name = d.pop("appName", UNSET)

        dl_circuit_name = d.pop("dlCircuitName", UNSET)

        dl_usage = d.pop("dlUsage", UNSET)

        dl_usage_pct = d.pop("dlUsagePct", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        ul_circuit_name = d.pop("ulCircuitName", UNSET)

        ul_usage = d.pop("ulUsage", UNSET)

        ul_usage_pct = d.pop("ulUsagePct", UNSET)

        post_v1_apps_utilization_response_200_apps_utilization_item = cls(
            app_id=app_id,
            app_name=app_name,
            dl_circuit_name=dl_circuit_name,
            dl_usage=dl_usage,
            dl_usage_pct=dl_usage_pct,
            sla_class=sla_class,
            ul_circuit_name=ul_circuit_name,
            ul_usage=ul_usage,
            ul_usage_pct=ul_usage_pct,
        )

        post_v1_apps_utilization_response_200_apps_utilization_item.additional_properties = d
        return post_v1_apps_utilization_response_200_apps_utilization_item

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
