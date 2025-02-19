from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutV1DiagnosticSpeedtestReportResponse200")


@_attrs_define
class PutV1DiagnosticSpeedtestReportResponse200:
    """
    Attributes:
        report (Union[Unset, str]):  Example: [37,80,68,70,45,49,46,52,10,37,211,235,233,225,10,49,32,48,32,111,98,106,1
            0,60,60,47,67,114,101,97,116,111,114,32,40,67,104,114,111,109,105,117,109,41,10,47,80,114,111,100,117,99,101,114
            ,32,40,83,107,105,97,47,80,68,70,32,109,57,56,41,10,47,67,114,101,97,116,105,111,110,68,97,116,101,32,40,68,58,5
            0,48,50,50,48,54,48,57,48,54,52,49,50,55,43,48,48,39,48,48,39,41,10,47,77,111,100,68,97,116,101,32,40,68,58,50,4
            8,50,50,48,54,48,57,48,54,52,49,50,55,43,48,48,39,48,48].
        report_id (Union[Unset, str]):  Example: 10.
    """

    report: Union[Unset, str] = UNSET
    report_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report = self.report

        report_id = self.report_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report is not UNSET:
            field_dict["report"] = report
        if report_id is not UNSET:
            field_dict["reportId"] = report_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        report = d.pop("report", UNSET)

        report_id = d.pop("reportId", UNSET)

        put_v1_diagnostic_speedtest_report_response_200 = cls(
            report=report,
            report_id=report_id,
        )

        put_v1_diagnostic_speedtest_report_response_200.additional_properties = d
        return put_v1_diagnostic_speedtest_report_response_200

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
