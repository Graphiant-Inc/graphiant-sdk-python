from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem")


@_attrs_define
class GetV1TroubleshootingSiteConnectivityStatusResponse200ConnectivityStatusItem:
    """
    Attributes:
        site_id (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    site_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        site_id = d.pop("siteId", UNSET)

        status = d.pop("status", UNSET)

        get_v1_troubleshooting_site_connectivity_status_response_200_connectivity_status_item = cls(
            site_id=site_id,
            status=status,
        )

        get_v1_troubleshooting_site_connectivity_status_response_200_connectivity_status_item.additional_properties = d
        return get_v1_troubleshooting_site_connectivity_status_response_200_connectivity_status_item

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
