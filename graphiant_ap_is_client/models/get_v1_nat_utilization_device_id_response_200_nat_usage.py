from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1NatUtilizationDeviceIdResponse200NatUsage")


@_attrs_define
class GetV1NatUtilizationDeviceIdResponse200NatUsage:
    """
    Attributes:
        current_count (Union[Unset, str]):  Example: TYPE_UINT64.
        current_count_extranet (Union[Unset, str]):  Example: TYPE_UINT64.
        current_count_pat (Union[Unset, str]):  Example: TYPE_UINT64.
        current_count_static (Union[Unset, str]):  Example: TYPE_UINT64.
        max_count (Union[Unset, str]):  Example: TYPE_UINT64.
    """

    current_count: Union[Unset, str] = UNSET
    current_count_extranet: Union[Unset, str] = UNSET
    current_count_pat: Union[Unset, str] = UNSET
    current_count_static: Union[Unset, str] = UNSET
    max_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_count = self.current_count

        current_count_extranet = self.current_count_extranet

        current_count_pat = self.current_count_pat

        current_count_static = self.current_count_static

        max_count = self.max_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_count is not UNSET:
            field_dict["currentCount"] = current_count
        if current_count_extranet is not UNSET:
            field_dict["currentCountExtranet"] = current_count_extranet
        if current_count_pat is not UNSET:
            field_dict["currentCountPat"] = current_count_pat
        if current_count_static is not UNSET:
            field_dict["currentCountStatic"] = current_count_static
        if max_count is not UNSET:
            field_dict["maxCount"] = max_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        current_count = d.pop("currentCount", UNSET)

        current_count_extranet = d.pop("currentCountExtranet", UNSET)

        current_count_pat = d.pop("currentCountPat", UNSET)

        current_count_static = d.pop("currentCountStatic", UNSET)

        max_count = d.pop("maxCount", UNSET)

        get_v1_nat_utilization_device_id_response_200_nat_usage = cls(
            current_count=current_count,
            current_count_extranet=current_count_extranet,
            current_count_pat=current_count_pat,
            current_count_static=current_count_static,
            max_count=max_count,
        )

        get_v1_nat_utilization_device_id_response_200_nat_usage.additional_properties = d
        return get_v1_nat_utilization_device_id_response_200_nat_usage

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
