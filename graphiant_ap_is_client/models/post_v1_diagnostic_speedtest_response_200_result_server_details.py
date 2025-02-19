from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1DiagnosticSpeedtestResponse200ResultServerDetails")


@_attrs_define
class PostV1DiagnosticSpeedtestResponse200ResultServerDetails:
    """
    Attributes:
        country (Union[Unset, str]):  Example: United Kingdom.
        host (Union[Unset, str]):  Example: speedtest.fastmetrics.com.
        id (Union[Unset, str]):  Example: 29113.
        ip_address (Union[Unset, str]):  Example: 1213:1::6451.
        location (Union[Unset, str]):  Example: Sheffield.
        name (Union[Unset, str]):  Example: Google Fiber.
    """

    country: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_address: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        host = self.host

        id = self.id

        ip_address = self.ip_address

        location = self.location

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if host is not UNSET:
            field_dict["host"] = host
        if id is not UNSET:
            field_dict["id"] = id
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        country = d.pop("country", UNSET)

        host = d.pop("host", UNSET)

        id = d.pop("id", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        location = d.pop("location", UNSET)

        name = d.pop("name", UNSET)

        post_v1_diagnostic_speedtest_response_200_result_server_details = cls(
            country=country,
            host=host,
            id=id,
            ip_address=ip_address,
            location=location,
            name=name,
        )

        post_v1_diagnostic_speedtest_response_200_result_server_details.additional_properties = d
        return post_v1_diagnostic_speedtest_response_200_result_server_details

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
