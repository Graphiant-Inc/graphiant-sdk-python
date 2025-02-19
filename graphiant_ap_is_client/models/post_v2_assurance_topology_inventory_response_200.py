from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_inventory_response_200_client_sites_item import (
        PostV2AssuranceTopologyInventoryResponse200ClientSitesItem,
    )
    from ..models.post_v2_assurance_topology_inventory_response_200_regions_item import (
        PostV2AssuranceTopologyInventoryResponse200RegionsItem,
    )
    from ..models.post_v2_assurance_topology_inventory_response_200_server_sites_item import (
        PostV2AssuranceTopologyInventoryResponse200ServerSitesItem,
    )
    from ..models.post_v2_assurance_topology_inventory_response_200_topology_change_ts_item import (
        PostV2AssuranceTopologyInventoryResponse200TopologyChangeTsItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyInventoryResponse200")


@_attrs_define
class PostV2AssuranceTopologyInventoryResponse200:
    """
    Attributes:
        app_names (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        client_sites (Union[Unset, list['PostV2AssuranceTopologyInventoryResponse200ClientSitesItem']]):
        regions (Union[Unset, list['PostV2AssuranceTopologyInventoryResponse200RegionsItem']]):
        server_sites (Union[Unset, list['PostV2AssuranceTopologyInventoryResponse200ServerSitesItem']]):
        topology_change_ts (Union[Unset, list['PostV2AssuranceTopologyInventoryResponse200TopologyChangeTsItem']]):
    """

    app_names: Union[Unset, list[str]] = UNSET
    client_sites: Union[Unset, list["PostV2AssuranceTopologyInventoryResponse200ClientSitesItem"]] = UNSET
    regions: Union[Unset, list["PostV2AssuranceTopologyInventoryResponse200RegionsItem"]] = UNSET
    server_sites: Union[Unset, list["PostV2AssuranceTopologyInventoryResponse200ServerSitesItem"]] = UNSET
    topology_change_ts: Union[Unset, list["PostV2AssuranceTopologyInventoryResponse200TopologyChangeTsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.app_names, Unset):
            app_names = self.app_names

        client_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.client_sites, Unset):
            client_sites = []
            for client_sites_item_data in self.client_sites:
                client_sites_item = client_sites_item_data.to_dict()
                client_sites.append(client_sites_item)

        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        server_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.server_sites, Unset):
            server_sites = []
            for server_sites_item_data in self.server_sites:
                server_sites_item = server_sites_item_data.to_dict()
                server_sites.append(server_sites_item)

        topology_change_ts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.topology_change_ts, Unset):
            topology_change_ts = []
            for topology_change_ts_item_data in self.topology_change_ts:
                topology_change_ts_item = topology_change_ts_item_data.to_dict()
                topology_change_ts.append(topology_change_ts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_names is not UNSET:
            field_dict["appNames"] = app_names
        if client_sites is not UNSET:
            field_dict["clientSites"] = client_sites
        if regions is not UNSET:
            field_dict["regions"] = regions
        if server_sites is not UNSET:
            field_dict["serverSites"] = server_sites
        if topology_change_ts is not UNSET:
            field_dict["topologyChangeTs"] = topology_change_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_inventory_response_200_client_sites_item import (
            PostV2AssuranceTopologyInventoryResponse200ClientSitesItem,
        )
        from ..models.post_v2_assurance_topology_inventory_response_200_regions_item import (
            PostV2AssuranceTopologyInventoryResponse200RegionsItem,
        )
        from ..models.post_v2_assurance_topology_inventory_response_200_server_sites_item import (
            PostV2AssuranceTopologyInventoryResponse200ServerSitesItem,
        )
        from ..models.post_v2_assurance_topology_inventory_response_200_topology_change_ts_item import (
            PostV2AssuranceTopologyInventoryResponse200TopologyChangeTsItem,
        )

        d = src_dict.copy()
        app_names = cast(list[str], d.pop("appNames", UNSET))

        client_sites = []
        _client_sites = d.pop("clientSites", UNSET)
        for client_sites_item_data in _client_sites or []:
            client_sites_item = PostV2AssuranceTopologyInventoryResponse200ClientSitesItem.from_dict(
                client_sites_item_data
            )

            client_sites.append(client_sites_item)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = PostV2AssuranceTopologyInventoryResponse200RegionsItem.from_dict(regions_item_data)

            regions.append(regions_item)

        server_sites = []
        _server_sites = d.pop("serverSites", UNSET)
        for server_sites_item_data in _server_sites or []:
            server_sites_item = PostV2AssuranceTopologyInventoryResponse200ServerSitesItem.from_dict(
                server_sites_item_data
            )

            server_sites.append(server_sites_item)

        topology_change_ts = []
        _topology_change_ts = d.pop("topologyChangeTs", UNSET)
        for topology_change_ts_item_data in _topology_change_ts or []:
            topology_change_ts_item = PostV2AssuranceTopologyInventoryResponse200TopologyChangeTsItem.from_dict(
                topology_change_ts_item_data
            )

            topology_change_ts.append(topology_change_ts_item)

        post_v2_assurance_topology_inventory_response_200 = cls(
            app_names=app_names,
            client_sites=client_sites,
            regions=regions,
            server_sites=server_sites,
            topology_change_ts=topology_change_ts,
        )

        post_v2_assurance_topology_inventory_response_200.additional_properties = d
        return post_v2_assurance_topology_inventory_response_200

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
