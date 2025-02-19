from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2AssuranceReadUserReportListResponse200UserReportListItem")


@_attrs_define
class GetV2AssuranceReadUserReportListResponse200UserReportListItem:
    """
    Attributes:
        created_by (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        created_on (Union[Unset, str]):  Example: TYPE_INT64.
        email_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        enterprise_id (Union[Unset, str]):  Example: TYPE_STRING.
        report_id (Union[Unset, str]):  Example: TYPE_INT64.
        report_name (Union[Unset, str]):  Example: TYPE_STRING.
        report_type (Union[Unset, str]):  Example: TYPE_ENUM.
        time_period (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    created_by: Union[Unset, list[str]] = UNSET
    created_on: Union[Unset, str] = UNSET
    email_list: Union[Unset, list[str]] = UNSET
    enterprise_id: Union[Unset, str] = UNSET
    report_id: Union[Unset, str] = UNSET
    report_name: Union[Unset, str] = UNSET
    report_type: Union[Unset, str] = UNSET
    time_period: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by: Union[Unset, list[str]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by

        created_on = self.created_on

        email_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email_list, Unset):
            email_list = self.email_list

        enterprise_id = self.enterprise_id

        report_id = self.report_id

        report_name = self.report_name

        report_type = self.report_type

        time_period = self.time_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if email_list is not UNSET:
            field_dict["emailList"] = email_list
        if enterprise_id is not UNSET:
            field_dict["enterpriseId"] = enterprise_id
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
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
        created_by = cast(list[str], d.pop("createdBy", UNSET))

        created_on = d.pop("createdOn", UNSET)

        email_list = cast(list[str], d.pop("emailList", UNSET))

        enterprise_id = d.pop("enterpriseId", UNSET)

        report_id = d.pop("reportId", UNSET)

        report_name = d.pop("reportName", UNSET)

        report_type = d.pop("reportType", UNSET)

        time_period = d.pop("timePeriod", UNSET)

        get_v2_assurance_read_user_report_list_response_200_user_report_list_item = cls(
            created_by=created_by,
            created_on=created_on,
            email_list=email_list,
            enterprise_id=enterprise_id,
            report_id=report_id,
            report_name=report_name,
            report_type=report_type,
            time_period=time_period,
        )

        get_v2_assurance_read_user_report_list_response_200_user_report_list_item.additional_properties = d
        return get_v2_assurance_read_user_report_list_response_200_user_report_list_item

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
