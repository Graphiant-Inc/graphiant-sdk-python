from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItemBwusageRoleSummaryItem"
)


@_attrs_define
class PostV1BwtrackerEnterpriseSummaryResponse200BwusageSummaryBwusageTopRegionsItemBwusageRoleSummaryItem:
    """
    Attributes:
        role_id (Union[Unset, str]):  Example: TYPE_UINT64.
        role_name (Union[Unset, str]):  Example: TYPE_STRING.
        usage_kbps (Union[Unset, str]):  Example: TYPE_DOUBLE.
    """

    role_id: Union[Unset, str] = UNSET
    role_name: Union[Unset, str] = UNSET
    usage_kbps: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        role_name = self.role_name

        usage_kbps = self.usage_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if usage_kbps is not UNSET:
            field_dict["usageKbps"] = usage_kbps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        usage_kbps = d.pop("usageKbps", UNSET)

        post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_top_regions_item_bwusage_role_summary_item = cls(
            role_id=role_id,
            role_name=role_name,
            usage_kbps=usage_kbps,
        )

        post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_top_regions_item_bwusage_role_summary_item.additional_properties = d
        return post_v1_bwtracker_enterprise_summary_response_200_bwusage_summary_bwusage_top_regions_item_bwusage_role_summary_item

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
