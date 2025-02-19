from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_extranets_monitoring_nat_usage_response_200_allocations_item import (
        GetV1ExtranetsMonitoringNatUsageResponse200AllocationsItem,
    )


T = TypeVar("T", bound="GetV1ExtranetsMonitoringNatUsageResponse200")


@_attrs_define
class GetV1ExtranetsMonitoringNatUsageResponse200:
    """
    Attributes:
        allocated_count (Union[Unset, str]):  Example: TYPE_UINT32.
        allocations (Union[Unset, list['GetV1ExtranetsMonitoringNatUsageResponse200AllocationsItem']]):
        usage_count (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    allocated_count: Union[Unset, str] = UNSET
    allocations: Union[Unset, list["GetV1ExtranetsMonitoringNatUsageResponse200AllocationsItem"]] = UNSET
    usage_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocated_count = self.allocated_count

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        usage_count = self.usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocated_count is not UNSET:
            field_dict["allocatedCount"] = allocated_count
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if usage_count is not UNSET:
            field_dict["usageCount"] = usage_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_extranets_monitoring_nat_usage_response_200_allocations_item import (
            GetV1ExtranetsMonitoringNatUsageResponse200AllocationsItem,
        )

        d = src_dict.copy()
        allocated_count = d.pop("allocatedCount", UNSET)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = GetV1ExtranetsMonitoringNatUsageResponse200AllocationsItem.from_dict(
                allocations_item_data
            )

            allocations.append(allocations_item)

        usage_count = d.pop("usageCount", UNSET)

        get_v1_extranets_monitoring_nat_usage_response_200 = cls(
            allocated_count=allocated_count,
            allocations=allocations,
            usage_count=usage_count,
        )

        get_v1_extranets_monitoring_nat_usage_response_200.additional_properties = d
        return get_v1_extranets_monitoring_nat_usage_response_200

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
