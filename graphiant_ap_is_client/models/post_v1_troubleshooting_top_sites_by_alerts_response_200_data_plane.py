from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane_site_counts_item import (
        PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem,
    )


T = TypeVar("T", bound="PostV1TroubleshootingTopSitesByAlertsResponse200DataPlane")


@_attrs_define
class PostV1TroubleshootingTopSitesByAlertsResponse200DataPlane:
    """
    Attributes:
        site_counts (Union[Unset, list['PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem']]):
    """

    site_counts: Union[Unset, list["PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_counts, Unset):
            site_counts = []
            for site_counts_item_data in self.site_counts:
                site_counts_item = site_counts_item_data.to_dict()
                site_counts.append(site_counts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_counts is not UNSET:
            field_dict["siteCounts"] = site_counts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane_site_counts_item import (
            PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem,
        )

        d = src_dict.copy()
        site_counts = []
        _site_counts = d.pop("siteCounts", UNSET)
        for site_counts_item_data in _site_counts or []:
            site_counts_item = PostV1TroubleshootingTopSitesByAlertsResponse200DataPlaneSiteCountsItem.from_dict(
                site_counts_item_data
            )

            site_counts.append(site_counts_item)

        post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane = cls(
            site_counts=site_counts,
        )

        post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane.additional_properties = d
        return post_v1_troubleshooting_top_sites_by_alerts_response_200_data_plane

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
