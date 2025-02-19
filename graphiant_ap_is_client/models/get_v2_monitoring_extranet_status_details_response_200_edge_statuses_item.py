from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem")


@_attrs_define
class GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem:
    """
    Attributes:
        disconnected_reason (Union[Unset, str]):  Example: TYPE_STRING.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    disconnected_reason: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disconnected_reason = self.disconnected_reason

        hostname = self.hostname

        id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disconnected_reason is not UNSET:
            field_dict["disconnectedReason"] = disconnected_reason
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        disconnected_reason = d.pop("disconnectedReason", UNSET)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        get_v2_monitoring_extranet_status_details_response_200_edge_statuses_item = cls(
            disconnected_reason=disconnected_reason,
            hostname=hostname,
            id=id,
            status=status,
        )

        get_v2_monitoring_extranet_status_details_response_200_edge_statuses_item.additional_properties = d
        return get_v2_monitoring_extranet_status_details_response_200_edge_statuses_item

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
