from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1DiagnosticOtpDeviceIdResponse200")


@_attrs_define
class GetV1DiagnosticOtpDeviceIdResponse200:
    """
    Attributes:
        pass_code (Union[Unset, str]):  Example: 123456.
    """

    pass_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_code = self.pass_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_code is not UNSET:
            field_dict["passCode"] = pass_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pass_code = d.pop("passCode", UNSET)

        get_v1_diagnostic_otp_device_id_response_200 = cls(
            pass_code=pass_code,
        )

        get_v1_diagnostic_otp_device_id_response_200.additional_properties = d
        return get_v1_diagnostic_otp_device_id_response_200

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
