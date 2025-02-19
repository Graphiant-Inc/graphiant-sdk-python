from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_diagnostic_gnmi_ping_response_200_results_item_rtt import (
        GetV1DiagnosticGnmiPingResponse200ResultsItemRtt,
    )


T = TypeVar("T", bound="GetV1DiagnosticGnmiPingResponse200ResultsItem")


@_attrs_define
class GetV1DiagnosticGnmiPingResponse200ResultsItem:
    """
    Attributes:
        address (Union[Unset, str]):  Example: 12001:0db8:85a3:0000:0000:8a2e:0370:7334.
        error (Union[Unset, str]):  Example: device offline.
        rtt (Union[Unset, GetV1DiagnosticGnmiPingResponse200ResultsItemRtt]):
    """

    address: Union[Unset, str] = UNSET
    error: Union[Unset, str] = UNSET
    rtt: Union[Unset, "GetV1DiagnosticGnmiPingResponse200ResultsItemRtt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        error = self.error

        rtt: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rtt, Unset):
            rtt = self.rtt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if error is not UNSET:
            field_dict["error"] = error
        if rtt is not UNSET:
            field_dict["rtt"] = rtt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_diagnostic_gnmi_ping_response_200_results_item_rtt import (
            GetV1DiagnosticGnmiPingResponse200ResultsItemRtt,
        )

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        error = d.pop("error", UNSET)

        _rtt = d.pop("rtt", UNSET)
        rtt: Union[Unset, GetV1DiagnosticGnmiPingResponse200ResultsItemRtt]
        if isinstance(_rtt, Unset):
            rtt = UNSET
        else:
            rtt = GetV1DiagnosticGnmiPingResponse200ResultsItemRtt.from_dict(_rtt)

        get_v1_diagnostic_gnmi_ping_response_200_results_item = cls(
            address=address,
            error=error,
            rtt=rtt,
        )

        get_v1_diagnostic_gnmi_ping_response_200_results_item.additional_properties = d
        return get_v1_diagnostic_gnmi_ping_response_200_results_item

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
