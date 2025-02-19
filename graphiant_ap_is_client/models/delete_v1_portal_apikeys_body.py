from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteV1PortalApikeysBody")


@_attrs_define
class DeleteV1PortalApikeysBody:
    """
    Attributes:
        gcs_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    gcs_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gcs_name = self.gcs_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gcs_name is not UNSET:
            field_dict["gcsName"] = gcs_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        gcs_name = d.pop("gcsName", UNSET)

        delete_v1_portal_apikeys_body = cls(
            gcs_name=gcs_name,
        )

        delete_v1_portal_apikeys_body.additional_properties = d
        return delete_v1_portal_apikeys_body

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
