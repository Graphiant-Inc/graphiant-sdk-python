from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1ExtranetsIdResponse200PolicyAuto")


@_attrs_define
class GetV1ExtranetsIdResponse200PolicyAuto:
    """
    Attributes:
        auto_propagate (Union[Unset, str]):  Example: TYPE_BOOL.
        excluded_prefixes (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    auto_propagate: Union[Unset, str] = UNSET
    excluded_prefixes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_propagate = self.auto_propagate

        excluded_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.excluded_prefixes, Unset):
            excluded_prefixes = self.excluded_prefixes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_propagate is not UNSET:
            field_dict["autoPropagate"] = auto_propagate
        if excluded_prefixes is not UNSET:
            field_dict["excludedPrefixes"] = excluded_prefixes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_propagate = d.pop("autoPropagate", UNSET)

        excluded_prefixes = cast(list[str], d.pop("excludedPrefixes", UNSET))

        get_v1_extranets_id_response_200_policy_auto = cls(
            auto_propagate=auto_propagate,
            excluded_prefixes=excluded_prefixes,
        )

        get_v1_extranets_id_response_200_policy_auto.additional_properties = d
        return get_v1_extranets_id_response_200_policy_auto

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
