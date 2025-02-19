from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1AppsCountResponse200CircuitsItemQueuesItem")


@_attrs_define
class PostV1AppsCountResponse200CircuitsItemQueuesItem:
    """
    Attributes:
        apps_count (Union[Unset, str]):  Example: TYPE_UINT32.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    apps_count: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps_count = self.apps_count

        sla_class = self.sla_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if apps_count is not UNSET:
            field_dict["appsCount"] = apps_count
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        apps_count = d.pop("appsCount", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        post_v1_apps_count_response_200_circuits_item_queues_item = cls(
            apps_count=apps_count,
            sla_class=sla_class,
        )

        post_v1_apps_count_response_200_circuits_item_queues_item.additional_properties = d
        return post_v1_apps_count_response_200_circuits_item_queues_item

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
