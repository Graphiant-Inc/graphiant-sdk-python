from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceEndpointIntelBody")


@_attrs_define
class PostV2AssuranceEndpointIntelBody:
    """
    Attributes:
        domain_name (Union[Unset, str]):  Example: TYPE_STRING.
        ip_address (Union[Unset, str]):  Example: TYPE_STRING.
        path (Union[Unset, str]):  Example: TYPE_STRING.
    """

    domain_name: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        ip_address = self.ip_address

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        domain_name = d.pop("domainName", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        path = d.pop("path", UNSET)

        post_v2_assurance_endpoint_intel_body = cls(
            domain_name=domain_name,
            ip_address=ip_address,
            path=path,
        )

        post_v2_assurance_endpoint_intel_body.additional_properties = d
        return post_v2_assurance_endpoint_intel_body

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
