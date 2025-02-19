from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_lldp_interface_id_vendors_response_200_vendors_item import (
        GetV1LldpInterfaceIdVendorsResponse200VendorsItem,
    )


T = TypeVar("T", bound="GetV1LldpInterfaceIdVendorsResponse200")


@_attrs_define
class GetV1LldpInterfaceIdVendorsResponse200:
    """
    Attributes:
        vendors (Union[Unset, list['GetV1LldpInterfaceIdVendorsResponse200VendorsItem']]):
    """

    vendors: Union[Unset, list["GetV1LldpInterfaceIdVendorsResponse200VendorsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vendors, Unset):
            vendors = []
            for vendors_item_data in self.vendors:
                vendors_item = vendors_item_data.to_dict()
                vendors.append(vendors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendors is not UNSET:
            field_dict["vendors"] = vendors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_lldp_interface_id_vendors_response_200_vendors_item import (
            GetV1LldpInterfaceIdVendorsResponse200VendorsItem,
        )

        d = src_dict.copy()
        vendors = []
        _vendors = d.pop("vendors", UNSET)
        for vendors_item_data in _vendors or []:
            vendors_item = GetV1LldpInterfaceIdVendorsResponse200VendorsItem.from_dict(vendors_item_data)

            vendors.append(vendors_item)

        get_v1_lldp_interface_id_vendors_response_200 = cls(
            vendors=vendors,
        )

        get_v1_lldp_interface_id_vendors_response_200.additional_properties = d
        return get_v1_lldp_interface_id_vendors_response_200

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
