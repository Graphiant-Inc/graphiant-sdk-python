from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_flows_response_200_flows_item_client_site import (
        PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite,
    )
    from ..models.post_v2_assurance_topology_flows_response_200_flows_item_first_seen_ts import (
        PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs,
    )
    from ..models.post_v2_assurance_topology_flows_response_200_flows_item_last_seen_ts import (
        PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs,
    )
    from ..models.post_v2_assurance_topology_flows_response_200_flows_item_server_site import (
        PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyFlowsResponse200FlowsItem")


@_attrs_define
class PostV2AssuranceTopologyFlowsResponse200FlowsItem:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        client_site (Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite]):
        first_seen_ts (Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs]):
        lan_segment (Union[Unset, str]):  Example: TYPE_STRING.
        last_seen_ts (Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs]):
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_INT32.
        server_site (Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite]):
    """

    app_name: Union[Unset, str] = UNSET
    client_ip: Union[Unset, str] = UNSET
    client_site: Union[Unset, "PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite"] = UNSET
    first_seen_ts: Union[Unset, "PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs"] = UNSET
    lan_segment: Union[Unset, str] = UNSET
    last_seen_ts: Union[Unset, "PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs"] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    server_site: Union[Unset, "PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        client_ip = self.client_ip

        client_site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_site, Unset):
            client_site = self.client_site.to_dict()

        first_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_seen_ts, Unset):
            first_seen_ts = self.first_seen_ts.to_dict()

        lan_segment = self.lan_segment

        last_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_seen_ts, Unset):
            last_seen_ts = self.last_seen_ts.to_dict()

        server_ip = self.server_ip

        server_port = self.server_port

        server_site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_site, Unset):
            server_site = self.server_site.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if client_site is not UNSET:
            field_dict["clientSite"] = client_site
        if first_seen_ts is not UNSET:
            field_dict["firstSeenTs"] = first_seen_ts
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if last_seen_ts is not UNSET:
            field_dict["lastSeenTs"] = last_seen_ts
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if server_site is not UNSET:
            field_dict["serverSite"] = server_site

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_flows_response_200_flows_item_client_site import (
            PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite,
        )
        from ..models.post_v2_assurance_topology_flows_response_200_flows_item_first_seen_ts import (
            PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs,
        )
        from ..models.post_v2_assurance_topology_flows_response_200_flows_item_last_seen_ts import (
            PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs,
        )
        from ..models.post_v2_assurance_topology_flows_response_200_flows_item_server_site import (
            PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        client_ip = d.pop("clientIp", UNSET)

        _client_site = d.pop("clientSite", UNSET)
        client_site: Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite]
        if isinstance(_client_site, Unset):
            client_site = UNSET
        else:
            client_site = PostV2AssuranceTopologyFlowsResponse200FlowsItemClientSite.from_dict(_client_site)

        _first_seen_ts = d.pop("firstSeenTs", UNSET)
        first_seen_ts: Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs]
        if isinstance(_first_seen_ts, Unset):
            first_seen_ts = UNSET
        else:
            first_seen_ts = PostV2AssuranceTopologyFlowsResponse200FlowsItemFirstSeenTs.from_dict(_first_seen_ts)

        lan_segment = d.pop("lanSegment", UNSET)

        _last_seen_ts = d.pop("lastSeenTs", UNSET)
        last_seen_ts: Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs]
        if isinstance(_last_seen_ts, Unset):
            last_seen_ts = UNSET
        else:
            last_seen_ts = PostV2AssuranceTopologyFlowsResponse200FlowsItemLastSeenTs.from_dict(_last_seen_ts)

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        _server_site = d.pop("serverSite", UNSET)
        server_site: Union[Unset, PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite]
        if isinstance(_server_site, Unset):
            server_site = UNSET
        else:
            server_site = PostV2AssuranceTopologyFlowsResponse200FlowsItemServerSite.from_dict(_server_site)

        post_v2_assurance_topology_flows_response_200_flows_item = cls(
            app_name=app_name,
            client_ip=client_ip,
            client_site=client_site,
            first_seen_ts=first_seen_ts,
            lan_segment=lan_segment,
            last_seen_ts=last_seen_ts,
            server_ip=server_ip,
            server_port=server_port,
            server_site=server_site,
        )

        post_v2_assurance_topology_flows_response_200_flows_item.additional_properties = d
        return post_v2_assurance_topology_flows_response_200_flows_item

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
