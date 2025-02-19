from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceCreateUserReportBody")


@_attrs_define
class PostV2AssuranceCreateUserReportBody:
    """
    Attributes:
        created_on (Union[Unset, str]):  Example: TYPE_INT64.
        email_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        pdf_content (Union[Unset, str]):  Example: TYPE_BYTES.
        raw_content (Union[Unset, list[str]]):  Example: ['TYPE_BYTES'].
        report_name (Union[Unset, str]):  Example: TYPE_STRING.
        report_type (Union[Unset, str]):  Example: TYPE_ENUM.
        time_period (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    created_on: Union[Unset, str] = UNSET
    email_list: Union[Unset, list[str]] = UNSET
    pdf_content: Union[Unset, str] = UNSET
    raw_content: Union[Unset, list[str]] = UNSET
    report_name: Union[Unset, str] = UNSET
    report_type: Union[Unset, str] = UNSET
    time_period: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_on = self.created_on

        email_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email_list, Unset):
            email_list = self.email_list

        pdf_content = self.pdf_content

        raw_content: Union[Unset, list[str]] = UNSET
        if not isinstance(self.raw_content, Unset):
            raw_content = self.raw_content

        report_name = self.report_name

        report_type = self.report_type

        time_period = self.time_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if email_list is not UNSET:
            field_dict["emailList"] = email_list
        if pdf_content is not UNSET:
            field_dict["pdfContent"] = pdf_content
        if raw_content is not UNSET:
            field_dict["rawContent"] = raw_content
        if report_name is not UNSET:
            field_dict["reportName"] = report_name
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if time_period is not UNSET:
            field_dict["timePeriod"] = time_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        created_on = d.pop("createdOn", UNSET)

        email_list = cast(list[str], d.pop("emailList", UNSET))

        pdf_content = d.pop("pdfContent", UNSET)

        raw_content = cast(list[str], d.pop("rawContent", UNSET))

        report_name = d.pop("reportName", UNSET)

        report_type = d.pop("reportType", UNSET)

        time_period = d.pop("timePeriod", UNSET)

        post_v2_assurance_create_user_report_body = cls(
            created_on=created_on,
            email_list=email_list,
            pdf_content=pdf_content,
            raw_content=raw_content,
            report_name=report_name,
            report_type=report_type,
            time_period=time_period,
        )

        post_v2_assurance_create_user_report_body.additional_properties = d
        return post_v2_assurance_create_user_report_body

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
