from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_assurance_read_user_report_list_response_200_user_report_list_item import (
        GetV2AssuranceReadUserReportListResponse200UserReportListItem,
    )


T = TypeVar("T", bound="GetV2AssuranceReadUserReportListResponse200")


@_attrs_define
class GetV2AssuranceReadUserReportListResponse200:
    """
    Attributes:
        user_report_list (Union[Unset, list['GetV2AssuranceReadUserReportListResponse200UserReportListItem']]):
    """

    user_report_list: Union[Unset, list["GetV2AssuranceReadUserReportListResponse200UserReportListItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_report_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_report_list, Unset):
            user_report_list = []
            for user_report_list_item_data in self.user_report_list:
                user_report_list_item = user_report_list_item_data.to_dict()
                user_report_list.append(user_report_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_report_list is not UNSET:
            field_dict["userReportList"] = user_report_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_assurance_read_user_report_list_response_200_user_report_list_item import (
            GetV2AssuranceReadUserReportListResponse200UserReportListItem,
        )

        d = src_dict.copy()
        user_report_list = []
        _user_report_list = d.pop("userReportList", UNSET)
        for user_report_list_item_data in _user_report_list or []:
            user_report_list_item = GetV2AssuranceReadUserReportListResponse200UserReportListItem.from_dict(
                user_report_list_item_data
            )

            user_report_list.append(user_report_list_item)

        get_v2_assurance_read_user_report_list_response_200 = cls(
            user_report_list=user_report_list,
        )

        get_v2_assurance_read_user_report_list_response_200.additional_properties = d
        return get_v2_assurance_read_user_report_list_response_200

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
