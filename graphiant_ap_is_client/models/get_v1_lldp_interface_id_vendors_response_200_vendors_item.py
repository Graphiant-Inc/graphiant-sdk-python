from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1LldpInterfaceIdVendorsResponse200VendorsItem")


@_attrs_define
class GetV1LldpInterfaceIdVendorsResponse200VendorsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        neighbor_count (Union[Unset, str]):  Example: TYPE_INT64.
    """

    name: Union[Unset, str] = UNSET
    neighbor_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        neighbor_count = self.neighbor_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if neighbor_count is not UNSET:
            field_dict["neighborCount"] = neighbor_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        neighbor_count = d.pop("neighborCount", UNSET)

        get_v1_lldp_interface_id_vendors_response_200_vendors_item = cls(
            name=name,
            neighbor_count=neighbor_count,
        )

        get_v1_lldp_interface_id_vendors_response_200_vendors_item.additional_properties = d
        return get_v1_lldp_interface_id_vendors_response_200_vendors_item

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
