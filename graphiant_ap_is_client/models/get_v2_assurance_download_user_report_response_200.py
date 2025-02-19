from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2AssuranceDownloadUserReportResponse200")


@_attrs_define
class GetV2AssuranceDownloadUserReportResponse200:
    """
    Attributes:
        pdf_content (Union[Unset, str]):  Example: TYPE_BYTES.
    """

    pdf_content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pdf_content = self.pdf_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pdf_content is not UNSET:
            field_dict["pdfContent"] = pdf_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        pdf_content = d.pop("pdfContent", UNSET)

        get_v2_assurance_download_user_report_response_200 = cls(
            pdf_content=pdf_content,
        )

        get_v2_assurance_download_user_report_response_200.additional_properties = d
        return get_v2_assurance_download_user_report_response_200

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
