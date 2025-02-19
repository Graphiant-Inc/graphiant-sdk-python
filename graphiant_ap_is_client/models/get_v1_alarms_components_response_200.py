from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1AlarmsComponentsResponse200")


@_attrs_define
class GetV1AlarmsComponentsResponse200:
    """
    Attributes:
        components (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    components: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: Union[Unset, list[str]] = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        components = cast(list[str], d.pop("components", UNSET))

        get_v1_alarms_components_response_200 = cls(
            components=components,
        )

        get_v1_alarms_components_response_200.additional_properties = d
        return get_v1_alarms_components_response_200

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
