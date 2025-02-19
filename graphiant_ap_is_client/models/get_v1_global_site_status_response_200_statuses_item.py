from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_global_site_status_response_200_statuses_item_status_since import (
        GetV1GlobalSiteStatusResponse200StatusesItemStatusSince,
    )


T = TypeVar("T", bound="GetV1GlobalSiteStatusResponse200StatusesItem")


@_attrs_define
class GetV1GlobalSiteStatusResponse200StatusesItem:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        error_message (Union[Unset, str]):  Example: TYPE_STRING.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        internal_state (Union[Unset, str]):  Example: TYPE_ENUM.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        status_since (Union[Unset, GetV1GlobalSiteStatusResponse200StatusesItemStatusSince]):
    """

    device_id: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    internal_state: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    status_since: Union[Unset, "GetV1GlobalSiteStatusResponse200StatusesItemStatusSince"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        error_message = self.error_message

        hostname = self.hostname

        internal_state = self.internal_state

        site_name = self.site_name

        status = self.status

        status_since: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status_since, Unset):
            status_since = self.status_since.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if internal_state is not UNSET:
            field_dict["internalState"] = internal_state
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if status is not UNSET:
            field_dict["status"] = status
        if status_since is not UNSET:
            field_dict["statusSince"] = status_since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_global_site_status_response_200_statuses_item_status_since import (
            GetV1GlobalSiteStatusResponse200StatusesItemStatusSince,
        )

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        hostname = d.pop("hostname", UNSET)

        internal_state = d.pop("internalState", UNSET)

        site_name = d.pop("siteName", UNSET)

        status = d.pop("status", UNSET)

        _status_since = d.pop("statusSince", UNSET)
        status_since: Union[Unset, GetV1GlobalSiteStatusResponse200StatusesItemStatusSince]
        if isinstance(_status_since, Unset):
            status_since = UNSET
        else:
            status_since = GetV1GlobalSiteStatusResponse200StatusesItemStatusSince.from_dict(_status_since)

        get_v1_global_site_status_response_200_statuses_item = cls(
            device_id=device_id,
            error_message=error_message,
            hostname=hostname,
            internal_state=internal_state,
            site_name=site_name,
            status=status,
            status_since=status_since,
        )

        get_v1_global_site_status_response_200_statuses_item.additional_properties = d
        return get_v1_global_site_status_response_200_statuses_item

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
