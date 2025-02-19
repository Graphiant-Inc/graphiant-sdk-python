from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1PresharedkeyResponse200")


@_attrs_define
class GetV1PresharedkeyResponse200:
    """
    Attributes:
        presharedkey (Union[Unset, str]):  Example: TYPE_STRING.
    """

    presharedkey: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        presharedkey = self.presharedkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if presharedkey is not UNSET:
            field_dict["presharedkey"] = presharedkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        presharedkey = d.pop("presharedkey", UNSET)

        get_v1_presharedkey_response_200 = cls(
            presharedkey=presharedkey,
        )

        get_v1_presharedkey_response_200.additional_properties = d
        return get_v1_presharedkey_response_200

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
