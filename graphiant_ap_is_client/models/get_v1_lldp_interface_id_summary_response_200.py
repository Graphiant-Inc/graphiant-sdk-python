from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1LldpInterfaceIdSummaryResponse200")


@_attrs_define
class GetV1LldpInterfaceIdSummaryResponse200:
    """
    Attributes:
        num_neighbors (Union[Unset, str]):  Example: TYPE_INT64.
        num_vendors (Union[Unset, str]):  Example: TYPE_INT64.
    """

    num_neighbors: Union[Unset, str] = UNSET
    num_vendors: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_neighbors = self.num_neighbors

        num_vendors = self.num_vendors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_neighbors is not UNSET:
            field_dict["numNeighbors"] = num_neighbors
        if num_vendors is not UNSET:
            field_dict["numVendors"] = num_vendors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        num_neighbors = d.pop("numNeighbors", UNSET)

        num_vendors = d.pop("numVendors", UNSET)

        get_v1_lldp_interface_id_summary_response_200 = cls(
            num_neighbors=num_neighbors,
            num_vendors=num_vendors,
        )

        get_v1_lldp_interface_id_summary_response_200.additional_properties = d
        return get_v1_lldp_interface_id_summary_response_200

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
