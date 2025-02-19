from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_nat_utilization_device_id_response_200_nat_usage import (
        GetV1NatUtilizationDeviceIdResponse200NatUsage,
    )
    from ..models.get_v1_nat_utilization_device_id_response_200_ts import GetV1NatUtilizationDeviceIdResponse200Ts


T = TypeVar("T", bound="GetV1NatUtilizationDeviceIdResponse200")


@_attrs_define
class GetV1NatUtilizationDeviceIdResponse200:
    """
    Attributes:
        nat_usage (Union[Unset, GetV1NatUtilizationDeviceIdResponse200NatUsage]):
        ts (Union[Unset, GetV1NatUtilizationDeviceIdResponse200Ts]):
    """

    nat_usage: Union[Unset, "GetV1NatUtilizationDeviceIdResponse200NatUsage"] = UNSET
    ts: Union[Unset, "GetV1NatUtilizationDeviceIdResponse200Ts"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nat_usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.nat_usage, Unset):
            nat_usage = self.nat_usage.to_dict()

        ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nat_usage is not UNSET:
            field_dict["natUsage"] = nat_usage
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_nat_utilization_device_id_response_200_nat_usage import (
            GetV1NatUtilizationDeviceIdResponse200NatUsage,
        )
        from ..models.get_v1_nat_utilization_device_id_response_200_ts import GetV1NatUtilizationDeviceIdResponse200Ts

        d = src_dict.copy()
        _nat_usage = d.pop("natUsage", UNSET)
        nat_usage: Union[Unset, GetV1NatUtilizationDeviceIdResponse200NatUsage]
        if isinstance(_nat_usage, Unset):
            nat_usage = UNSET
        else:
            nat_usage = GetV1NatUtilizationDeviceIdResponse200NatUsage.from_dict(_nat_usage)

        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, GetV1NatUtilizationDeviceIdResponse200Ts]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = GetV1NatUtilizationDeviceIdResponse200Ts.from_dict(_ts)

        get_v1_nat_utilization_device_id_response_200 = cls(
            nat_usage=nat_usage,
            ts=ts,
        )

        get_v1_nat_utilization_device_id_response_200.additional_properties = d
        return get_v1_nat_utilization_device_id_response_200

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
