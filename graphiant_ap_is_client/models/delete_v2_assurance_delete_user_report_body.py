from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteV2AssuranceDeleteUserReportBody")


@_attrs_define
class DeleteV2AssuranceDeleteUserReportBody:
    """
    Attributes:
        report_id (Union[Unset, str]):  Example: TYPE_INT64.
    """

    report_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_id is not UNSET:
            field_dict["reportId"] = report_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        report_id = d.pop("reportId", UNSET)

        delete_v2_assurance_delete_user_report_body = cls(
            report_id=report_id,
        )

        delete_v2_assurance_delete_user_report_body.additional_properties = d
        return delete_v2_assurance_delete_user_report_body

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
