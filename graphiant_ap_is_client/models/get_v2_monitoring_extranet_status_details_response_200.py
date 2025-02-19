from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_monitoring_extranet_status_details_response_200_edge_statuses_item import (
        GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem,
    )
    from ..models.get_v2_monitoring_extranet_status_details_response_200_site_status import (
        GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus,
    )


T = TypeVar("T", bound="GetV2MonitoringExtranetStatusDetailsResponse200")


@_attrs_define
class GetV2MonitoringExtranetStatusDetailsResponse200:
    """
    Attributes:
        edge_statuses (Union[Unset, list['GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem']]):
        site_status (Union[Unset, GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus]):
    """

    edge_statuses: Union[Unset, list["GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem"]] = UNSET
    site_status: Union[Unset, "GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge_statuses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edge_statuses, Unset):
            edge_statuses = []
            for edge_statuses_item_data in self.edge_statuses:
                edge_statuses_item = edge_statuses_item_data.to_dict()
                edge_statuses.append(edge_statuses_item)

        site_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site_status, Unset):
            site_status = self.site_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_statuses is not UNSET:
            field_dict["edgeStatuses"] = edge_statuses
        if site_status is not UNSET:
            field_dict["siteStatus"] = site_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_monitoring_extranet_status_details_response_200_edge_statuses_item import (
            GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem,
        )
        from ..models.get_v2_monitoring_extranet_status_details_response_200_site_status import (
            GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus,
        )

        d = src_dict.copy()
        edge_statuses = []
        _edge_statuses = d.pop("edgeStatuses", UNSET)
        for edge_statuses_item_data in _edge_statuses or []:
            edge_statuses_item = GetV2MonitoringExtranetStatusDetailsResponse200EdgeStatusesItem.from_dict(
                edge_statuses_item_data
            )

            edge_statuses.append(edge_statuses_item)

        _site_status = d.pop("siteStatus", UNSET)
        site_status: Union[Unset, GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus]
        if isinstance(_site_status, Unset):
            site_status = UNSET
        else:
            site_status = GetV2MonitoringExtranetStatusDetailsResponse200SiteStatus.from_dict(_site_status)

        get_v2_monitoring_extranet_status_details_response_200 = cls(
            edge_statuses=edge_statuses,
            site_status=site_status,
        )

        get_v2_monitoring_extranet_status_details_response_200.additional_properties = d
        return get_v2_monitoring_extranet_status_details_response_200

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
