from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_enterprise_allocation_response_200_regional_allocations_item import (
        GetV1EnterpriseAllocationResponse200RegionalAllocationsItem,
    )


T = TypeVar("T", bound="GetV1EnterpriseAllocationResponse200")


@_attrs_define
class GetV1EnterpriseAllocationResponse200:
    """
    Attributes:
        regional_allocations (Union[Unset, list['GetV1EnterpriseAllocationResponse200RegionalAllocationsItem']]):
    """

    regional_allocations: Union[Unset, list["GetV1EnterpriseAllocationResponse200RegionalAllocationsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regional_allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regional_allocations, Unset):
            regional_allocations = []
            for regional_allocations_item_data in self.regional_allocations:
                regional_allocations_item = regional_allocations_item_data.to_dict()
                regional_allocations.append(regional_allocations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if regional_allocations is not UNSET:
            field_dict["regionalAllocations"] = regional_allocations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_enterprise_allocation_response_200_regional_allocations_item import (
            GetV1EnterpriseAllocationResponse200RegionalAllocationsItem,
        )

        d = src_dict.copy()
        regional_allocations = []
        _regional_allocations = d.pop("regionalAllocations", UNSET)
        for regional_allocations_item_data in _regional_allocations or []:
            regional_allocations_item = GetV1EnterpriseAllocationResponse200RegionalAllocationsItem.from_dict(
                regional_allocations_item_data
            )

            regional_allocations.append(regional_allocations_item)

        get_v1_enterprise_allocation_response_200 = cls(
            regional_allocations=regional_allocations,
        )

        get_v1_enterprise_allocation_response_200.additional_properties = d
        return get_v1_enterprise_allocation_response_200

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
