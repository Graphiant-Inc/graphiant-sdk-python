from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1AccountInfoBody")


@_attrs_define
class PatchV1AccountInfoBody:
    """
    Attributes:
        first_name (Union[Unset, str]):  Example: TYPE_STRING.
        last_name (Union[Unset, str]):  Example: TYPE_STRING.
        time_zone (Union[Unset, str]):  Example: TYPE_STRING.
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        time_zone = self.time_zone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        patch_v1_account_info_body = cls(
            first_name=first_name,
            last_name=last_name,
            time_zone=time_zone,
        )

        patch_v1_account_info_body.additional_properties = d
        return patch_v1_account_info_body

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
