from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v2_monitoring_extranet_site_status_response_200_statuses_item_statuses_item import (
        GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem,
    )


T = TypeVar("T", bound="GetV2MonitoringExtranetSiteStatusResponse200StatusesItem")


@_attrs_define
class GetV2MonitoringExtranetSiteStatusResponse200StatusesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT64.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        status (Union[Unset, str]):  Example: TYPE_ENUM.
        statuses (Union[Unset, list['GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem']]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    statuses: Union[Unset, list["GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        statuses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v2_monitoring_extranet_site_status_response_200_statuses_item_statuses_item import (
            GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = GetV2MonitoringExtranetSiteStatusResponse200StatusesItemStatusesItem.from_dict(
                statuses_item_data
            )

            statuses.append(statuses_item)

        get_v2_monitoring_extranet_site_status_response_200_statuses_item = cls(
            id=id,
            name=name,
            status=status,
            statuses=statuses,
        )

        get_v2_monitoring_extranet_site_status_response_200_statuses_item.additional_properties = d
        return get_v2_monitoring_extranet_site_status_response_200_statuses_item

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
