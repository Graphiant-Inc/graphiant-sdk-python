from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringQueueResponse200DataItemSelector")


@_attrs_define
class PostV2MonitoringQueueResponse200DataItemSelector:
    """
    Attributes:
        group_name (Union[Unset, str]):  Example: TYPE_STRING.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    group_name: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        interface_name = self.interface_name

        sla_class = self.sla_class

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        group_name = d.pop("groupName", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        type_ = d.pop("type", UNSET)

        post_v2_monitoring_queue_response_200_data_item_selector = cls(
            group_name=group_name,
            interface_name=interface_name,
            sla_class=sla_class,
            type_=type_,
        )

        post_v2_monitoring_queue_response_200_data_item_selector.additional_properties = d
        return post_v2_monitoring_queue_response_200_data_item_selector

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
