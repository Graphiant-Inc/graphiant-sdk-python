from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus")


@_attrs_define
class PostV2MonitoringCircuitsStatusResponse200NetworkStatusCoreStatus:
    """
    Attributes:
        down_count (Union[Unset, str]):  Example: TYPE_INT32.
        healthy_count (Union[Unset, str]):  Example: TYPE_INT32.
        suboptimal_count (Union[Unset, str]):  Example: TYPE_INT32.
        total_count (Union[Unset, str]):  Example: TYPE_INT32.
        unhealthy_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    down_count: Union[Unset, str] = UNSET
    healthy_count: Union[Unset, str] = UNSET
    suboptimal_count: Union[Unset, str] = UNSET
    total_count: Union[Unset, str] = UNSET
    unhealthy_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        down_count = self.down_count

        healthy_count = self.healthy_count

        suboptimal_count = self.suboptimal_count

        total_count = self.total_count

        unhealthy_count = self.unhealthy_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if down_count is not UNSET:
            field_dict["downCount"] = down_count
        if healthy_count is not UNSET:
            field_dict["healthyCount"] = healthy_count
        if suboptimal_count is not UNSET:
            field_dict["suboptimalCount"] = suboptimal_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if unhealthy_count is not UNSET:
            field_dict["unhealthyCount"] = unhealthy_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        down_count = d.pop("downCount", UNSET)

        healthy_count = d.pop("healthyCount", UNSET)

        suboptimal_count = d.pop("suboptimalCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        unhealthy_count = d.pop("unhealthyCount", UNSET)

        post_v2_monitoring_circuits_status_response_200_network_status_core_status = cls(
            down_count=down_count,
            healthy_count=healthy_count,
            suboptimal_count=suboptimal_count,
            total_count=total_count,
            unhealthy_count=unhealthy_count,
        )

        post_v2_monitoring_circuits_status_response_200_network_status_core_status.additional_properties = d
        return post_v2_monitoring_circuits_status_response_200_network_status_core_status

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
