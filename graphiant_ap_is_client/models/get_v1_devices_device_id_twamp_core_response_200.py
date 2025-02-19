from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DevicesDeviceIdTwampCoreResponse200")


@_attrs_define
class GetV1DevicesDeviceIdTwampCoreResponse200:
    """
    Attributes:
        links (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    links: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, list[str]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        links = cast(list[str], d.pop("links", UNSET))

        get_v1_devices_device_id_twamp_core_response_200 = cls(
            links=links,
        )

        get_v1_devices_device_id_twamp_core_response_200.additional_properties = d
        return get_v1_devices_device_id_twamp_core_response_200

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
