from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_troubleshooting_site_site_id_response_200_edge_statuses_item import (
        GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem,
    )


T = TypeVar("T", bound="GetV1TroubleshootingSiteSiteIdResponse200")


@_attrs_define
class GetV1TroubleshootingSiteSiteIdResponse200:
    """
    Attributes:
        edge_statuses (Union[Unset, list['GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem']]):
        site_name (Union[Unset, str]):  Example: TYPE_STRING.
        site_status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    edge_statuses: Union[Unset, list["GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem"]] = UNSET
    site_name: Union[Unset, str] = UNSET
    site_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edge_statuses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edge_statuses, Unset):
            edge_statuses = []
            for edge_statuses_item_data in self.edge_statuses:
                edge_statuses_item = edge_statuses_item_data.to_dict()
                edge_statuses.append(edge_statuses_item)

        site_name = self.site_name

        site_status = self.site_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edge_statuses is not UNSET:
            field_dict["edgeStatuses"] = edge_statuses
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if site_status is not UNSET:
            field_dict["siteStatus"] = site_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_troubleshooting_site_site_id_response_200_edge_statuses_item import (
            GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem,
        )

        d = src_dict.copy()
        edge_statuses = []
        _edge_statuses = d.pop("edgeStatuses", UNSET)
        for edge_statuses_item_data in _edge_statuses or []:
            edge_statuses_item = GetV1TroubleshootingSiteSiteIdResponse200EdgeStatusesItem.from_dict(
                edge_statuses_item_data
            )

            edge_statuses.append(edge_statuses_item)

        site_name = d.pop("siteName", UNSET)

        site_status = d.pop("siteStatus", UNSET)

        get_v1_troubleshooting_site_site_id_response_200 = cls(
            edge_statuses=edge_statuses,
            site_name=site_name,
            site_status=site_status,
        )

        get_v1_troubleshooting_site_site_id_response_200.additional_properties = d
        return get_v1_troubleshooting_site_site_id_response_200

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
