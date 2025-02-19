from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringExtranetLogDetailsBody")


@_attrs_define
class PostV2MonitoringExtranetLogDetailsBody:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        is_b2b (Union[Unset, str]):  Example: TYPE_BOOL.
        is_provider (Union[Unset, str]):  Example: TYPE_BOOL.
    """

    id: Union[Unset, str] = UNSET
    is_b2b: Union[Unset, str] = UNSET
    is_provider: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_b2b = self.is_b2b

        is_provider = self.is_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_b2b is not UNSET:
            field_dict["isB2B"] = is_b2b
        if is_provider is not UNSET:
            field_dict["isProvider"] = is_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_b2b = d.pop("isB2B", UNSET)

        is_provider = d.pop("isProvider", UNSET)

        post_v2_monitoring_extranet_log_details_body = cls(
            id=id,
            is_b2b=is_b2b,
            is_provider=is_provider,
        )

        post_v2_monitoring_extranet_log_details_body.additional_properties = d
        return post_v2_monitoring_extranet_log_details_body

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
