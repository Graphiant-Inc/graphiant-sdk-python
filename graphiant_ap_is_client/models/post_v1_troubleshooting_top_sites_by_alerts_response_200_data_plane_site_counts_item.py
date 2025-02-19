from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem")


@_attrs_define
class PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem:
    """
    Attributes:
        num_alerts (Union[Unset, str]):  Example: TYPE_INT32.
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    num_alerts: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_alerts = self.num_alerts

        site_name = self.site_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_alerts is not UNSET:
            field_dict["numAlerts"] = num_alerts
        if site_name is not UNSET:
            field_dict["siteName"] = site_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        num_alerts = d.pop("numAlerts", UNSET)

        site_name = d.pop("siteName", UNSET)

        post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane_site_counts_item = cls(
            num_alerts=num_alerts,
            site_name=site_name,
        )

        post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane_site_counts_item.additional_properties = d
        return post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane_site_counts_item

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
