from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_policy_applications_response_200_applications_item import (
        GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem,
    )
    from ..models.get_v1_devices_device_id_policy_applications_response_200_page_info import (
        GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdPolicyApplicationsResponse200")


@_attrs_define
class GetV1DevicesDeviceIdPolicyApplicationsResponse200:
    """
    Attributes:
        applications (Union[Unset, list['GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem']]):
        page_info (Union[Unset, GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo]):
    """

    applications: Union[Unset, list["GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem"]] = UNSET
    page_info: Union[Unset, "GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applications: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        page_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_info, Unset):
            page_info = self.page_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applications is not UNSET:
            field_dict["applications"] = applications
        if page_info is not UNSET:
            field_dict["pageInfo"] = page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_policy_applications_response_200_applications_item import (
            GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem,
        )
        from ..models.get_v1_devices_device_id_policy_applications_response_200_page_info import (
            GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo,
        )

        d = src_dict.copy()
        applications = []
        _applications = d.pop("applications", UNSET)
        for applications_item_data in _applications or []:
            applications_item = GetV1DevicesDeviceIdPolicyApplicationsResponse200ApplicationsItem.from_dict(
                applications_item_data
            )

            applications.append(applications_item)

        _page_info = d.pop("pageInfo", UNSET)
        page_info: Union[Unset, GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo]
        if isinstance(_page_info, Unset):
            page_info = UNSET
        else:
            page_info = GetV1DevicesDeviceIdPolicyApplicationsResponse200PageInfo.from_dict(_page_info)

        get_v1_devices_device_id_policy_applications_response_200 = cls(
            applications=applications,
            page_info=page_info,
        )

        get_v1_devices_device_id_policy_applications_response_200.additional_properties = d
        return get_v1_devices_device_id_policy_applications_response_200

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
