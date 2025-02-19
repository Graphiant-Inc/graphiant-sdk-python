from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DiagnosticSpeedtestProvidersResponse200")


@_attrs_define
class GetV1DiagnosticSpeedtestProvidersResponse200:
    """
    Attributes:
        provider (Union[Unset, list[str]]):  Example: ['Ookla'].
    """

    provider: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: Union[Unset, list[str]] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = cast(list[str], d.pop("provider", UNSET))

        get_v1_diagnostic_speedtest_providers_response_200 = cls(
            provider=provider,
        )

        get_v1_diagnostic_speedtest_providers_response_200.additional_properties = d
        return get_v1_diagnostic_speedtest_providers_response_200

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
