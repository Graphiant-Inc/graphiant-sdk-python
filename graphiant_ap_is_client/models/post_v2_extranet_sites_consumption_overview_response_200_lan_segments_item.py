from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item_connections_item import (
        PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItemConnectionsItem,
    )


T = TypeVar("T", bound="PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem")


@_attrs_define
class PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItem:
    """
    Attributes:
        connections (Union[Unset,
            list['PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItemConnectionsItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    connections: Union[
        Unset, list["PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItemConnectionsItem"]
    ] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item_connections_item import (
            PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItemConnectionsItem,
        )

        d = src_dict.copy()
        connections = []
        _connections = d.pop("connections", UNSET)
        for connections_item_data in _connections or []:
            connections_item = (
                PostV2ExtranetSitesConsumptionOverviewResponse200LanSegmentsItemConnectionsItem.from_dict(
                    connections_item_data
                )
            )

            connections.append(connections_item)

        name = d.pop("name", UNSET)

        post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item = cls(
            connections=connections,
            name=name,
        )

        post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item.additional_properties = d
        return post_v2_extranet_sites_consumption_overview_response_200_lan_segments_item

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
