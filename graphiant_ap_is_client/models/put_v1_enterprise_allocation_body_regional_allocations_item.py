from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1EnterpriseAllocationBodyRegionalAllocationsItem")


@_attrs_define
class PutV1EnterpriseAllocationBodyRegionalAllocationsItem:
    """
    Attributes:
        allocation_core (Union[Unset, str]):  Example: TYPE_FLOAT.
        allocation_gw (Union[Unset, str]):  Example: TYPE_FLOAT.
        region_id (Union[Unset, str]):  Example: TYPE_INT32.
        region_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    allocation_core: Union[Unset, str] = UNSET
    allocation_gw: Union[Unset, str] = UNSET
    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_core = self.allocation_core

        allocation_gw = self.allocation_gw

        region_id = self.region_id

        region_name = self.region_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_core is not UNSET:
            field_dict["allocationCore"] = allocation_core
        if allocation_gw is not UNSET:
            field_dict["allocationGw"] = allocation_gw
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        allocation_core = d.pop("allocationCore", UNSET)

        allocation_gw = d.pop("allocationGw", UNSET)

        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        put_v1_enterprise_allocation_body_regional_allocations_item = cls(
            allocation_core=allocation_core,
            allocation_gw=allocation_gw,
            region_id=region_id,
            region_name=region_name,
        )

        put_v1_enterprise_allocation_body_regional_allocations_item.additional_properties = d
        return put_v1_enterprise_allocation_body_regional_allocations_item

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
