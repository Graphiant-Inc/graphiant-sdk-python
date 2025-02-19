from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchV1AuthBody")


@_attrs_define
class PatchV1AuthBody:
    """
    Attributes:
        cert (Union[Unset, str]):  Example: TYPE_STRING.
        entry_point (Union[Unset, str]):  Example: TYPE_STRING.
        iam_type (Union[Unset, str]):  Example: TYPE_ENUM.
        issuer (Union[Unset, str]):  Example: TYPE_STRING.
    """

    cert: Union[Unset, str] = UNSET
    entry_point: Union[Unset, str] = UNSET
    iam_type: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert = self.cert

        entry_point = self.entry_point

        iam_type = self.iam_type

        issuer = self.issuer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert is not UNSET:
            field_dict["cert"] = cert
        if entry_point is not UNSET:
            field_dict["entryPoint"] = entry_point
        if iam_type is not UNSET:
            field_dict["iamType"] = iam_type
        if issuer is not UNSET:
            field_dict["issuer"] = issuer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cert = d.pop("cert", UNSET)

        entry_point = d.pop("entryPoint", UNSET)

        iam_type = d.pop("iamType", UNSET)

        issuer = d.pop("issuer", UNSET)

        patch_v1_auth_body = cls(
            cert=cert,
            entry_point=entry_point,
            iam_type=iam_type,
            issuer=issuer,
        )

        patch_v1_auth_body.additional_properties = d
        return patch_v1_auth_body

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
