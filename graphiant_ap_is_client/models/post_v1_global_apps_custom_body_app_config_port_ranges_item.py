from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalAppsCustomBodyAppConfigPortRangesItem")


@_attrs_define
class PostV1GlobalAppsCustomBodyAppConfigPortRangesItem:
    """
    Attributes:
        lower (Union[Unset, str]):  Example: TYPE_UINT32.
        upper (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    lower: Union[Unset, str] = UNSET
    upper: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lower = self.lower

        upper = self.upper

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower is not UNSET:
            field_dict["lower"] = lower
        if upper is not UNSET:
            field_dict["upper"] = upper

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        lower = d.pop("lower", UNSET)

        upper = d.pop("upper", UNSET)

        post_v1_global_apps_custom_body_app_config_port_ranges_item = cls(
            lower=lower,
            upper=upper,
        )

        post_v1_global_apps_custom_body_app_config_port_ranges_item.additional_properties = d
        return post_v1_global_apps_custom_body_app_config_port_ranges_item

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
