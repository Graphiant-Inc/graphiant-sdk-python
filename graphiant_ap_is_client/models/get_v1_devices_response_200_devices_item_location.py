from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesResponse200DevicesItemLocation")


@_attrs_define
class GetV1DevicesResponse200DevicesItemLocation:
    """
    Attributes:
        address_line_1 (Union[Unset, str]):  Example: TYPE_STRING.
        address_line_2 (Union[Unset, str]):  Example: TYPE_STRING.
        city (Union[Unset, str]):  Example: TYPE_STRING.
        country (Union[Unset, str]):  Example: TYPE_STRING.
        country_code (Union[Unset, str]):  Example: TYPE_STRING.
        latitude (Union[Unset, str]):  Example: TYPE_DOUBLE.
        longitude (Union[Unset, str]):  Example: TYPE_DOUBLE.
        notes (Union[Unset, str]):  Example: TYPE_STRING.
        province_code (Union[Unset, str]):  Example: TYPE_STRING.
        state (Union[Unset, str]):  Example: TYPE_STRING.
        state_code (Union[Unset, str]):  Example: TYPE_STRING.
    """

    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    latitude: Union[Unset, str] = UNSET
    longitude: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    province_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        city = self.city

        country = self.country

        country_code = self.country_code

        latitude = self.latitude

        longitude = self.longitude

        notes = self.notes

        province_code = self.province_code

        state = self.state

        state_code = self.state_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if notes is not UNSET:
            field_dict["notes"] = notes
        if province_code is not UNSET:
            field_dict["provinceCode"] = province_code
        if state is not UNSET:
            field_dict["state"] = state
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        notes = d.pop("notes", UNSET)

        province_code = d.pop("provinceCode", UNSET)

        state = d.pop("state", UNSET)

        state_code = d.pop("stateCode", UNSET)

        get_v1_devices_response_200_devices_item_location = cls(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            country=country,
            country_code=country_code,
            latitude=latitude,
            longitude=longitude,
            notes=notes,
            province_code=province_code,
            state=state,
            state_code=state_code,
        )

        get_v1_devices_response_200_devices_item_location.additional_properties = d
        return get_v1_devices_response_200_devices_item_location

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
