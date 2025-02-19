from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem")


@_attrs_define
class GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem:
    """
    Attributes:
        address (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    address: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        status = d.pop("status", UNSET)

        get_v2_monitoring_extranet_site_status_response_200_statuses_item_statuses_item = cls(
            address=address,
            status=status,
        )

        get_v2_monitoring_extranet_site_status_response_200_statuses_item_statuses_item.additional_properties = d
        return get_v2_monitoring_extranet_site_status_response_200_statuses_item_statuses_item

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
