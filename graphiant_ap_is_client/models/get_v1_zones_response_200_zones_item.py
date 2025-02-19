from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1ZonesResponse200ZonesItem")


@_attrs_define
class GetV1ZonesResponse200ZonesItem:
    """
    Attributes:
        enterprise_id (Union[Unset, str]):  Example: TYPE_INT64.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    enterprise_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enterprise_id = self.enterprise_id

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        enterprise_id = d.pop("enterpriseId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        get_v1_zones_response_200_zones_item = cls(
            enterprise_id=enterprise_id,
            id=id,
            name=name,
        )

        get_v1_zones_response_200_zones_item.additional_properties = d
        return get_v1_zones_response_200_zones_item

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
