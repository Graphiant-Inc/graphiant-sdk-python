from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1FlowsTopologyBodyAppSelector")


@_attrs_define
class PostV1FlowsTopologyBodyAppSelector:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    app_id: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        app_name = self.app_name

        sla_class = self.sla_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        app_name = d.pop("appName", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        post_v1_flows_topology_body_app_selector = cls(
            app_id=app_id,
            app_name=app_name,
            sla_class=sla_class,
        )

        post_v1_flows_topology_body_app_selector.additional_properties = d
        return post_v1_flows_topology_body_app_selector

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
