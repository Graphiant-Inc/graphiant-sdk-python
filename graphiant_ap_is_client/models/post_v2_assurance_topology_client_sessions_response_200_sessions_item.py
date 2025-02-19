from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_client_endpoint import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_client_links_item import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientLinksItem,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_first_seen_ts import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_last_seen_ts import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_local_dia_links_item import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLocalDiaLinksItem,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_pop_links_item import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemPopLinksItem,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_remote_dia_links_item import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemRemoteDiaLinksItem,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_endpoint import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint,
    )
    from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_links_item import (
        PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionsResponse200SessionsItem")


@_attrs_define
class PostV2AssuranceTopologyClientSessionsResponse200SessionsItem:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        bucket (Union[Unset, str]):  Example: TYPE_ENUM.
        client_endpoint (Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint]):
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        client_links (Union[Unset,
            list['PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientLinksItem']]):
        first_seen_ts (Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs]):
        lan_segment (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        last_seen_ts (Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs]):
        local_dia_links (Union[Unset,
            list['PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLocalDiaLinksItem']]):
        pop_links (Union[Unset, list['PostV2AssuranceTopologyClientSessionsResponse200SessionsItemPopLinksItem']]):
        remote_dia_links (Union[Unset,
            list['PostV2AssuranceTopologyClientSessionsResponse200SessionsItemRemoteDiaLinksItem']]):
        risk_status (Union[Unset, str]):  Example: TYPE_ENUM.
        server_endpoint (Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint]):
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_links (Union[Unset,
            list['PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem']]):
        server_port (Union[Unset, str]):  Example: TYPE_INT32.
        session_id (Union[Unset, str]):  Example: TYPE_STRING.
        sla (Union[Unset, str]):  Example: TYPE_ENUM.
        sla_class (Union[Unset, str]):  Example: TYPE_STRING.
    """

    app_name: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    client_endpoint: Union[Unset, "PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint"] = UNSET
    client_ip: Union[Unset, str] = UNSET
    client_links: Union[Unset, list["PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientLinksItem"]] = (
        UNSET
    )
    first_seen_ts: Union[Unset, "PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs"] = UNSET
    lan_segment: Union[Unset, list[str]] = UNSET
    last_seen_ts: Union[Unset, "PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs"] = UNSET
    local_dia_links: Union[
        Unset, list["PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLocalDiaLinksItem"]
    ] = UNSET
    pop_links: Union[Unset, list["PostV2AssuranceTopologyClientSessionsResponse200SessionsItemPopLinksItem"]] = UNSET
    remote_dia_links: Union[
        Unset, list["PostV2AssuranceTopologyClientSessionsResponse200SessionsItemRemoteDiaLinksItem"]
    ] = UNSET
    risk_status: Union[Unset, str] = UNSET
    server_endpoint: Union[Unset, "PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint"] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_links: Union[Unset, list["PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem"]] = (
        UNSET
    )
    server_port: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    sla: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        bucket = self.bucket

        client_endpoint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_endpoint, Unset):
            client_endpoint = self.client_endpoint.to_dict()

        client_ip = self.client_ip

        client_links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.client_links, Unset):
            client_links = []
            for client_links_item_data in self.client_links:
                client_links_item = client_links_item_data.to_dict()
                client_links.append(client_links_item)

        first_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_seen_ts, Unset):
            first_seen_ts = self.first_seen_ts.to_dict()

        lan_segment: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lan_segment, Unset):
            lan_segment = self.lan_segment

        last_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_seen_ts, Unset):
            last_seen_ts = self.last_seen_ts.to_dict()

        local_dia_links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.local_dia_links, Unset):
            local_dia_links = []
            for local_dia_links_item_data in self.local_dia_links:
                local_dia_links_item = local_dia_links_item_data.to_dict()
                local_dia_links.append(local_dia_links_item)

        pop_links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pop_links, Unset):
            pop_links = []
            for pop_links_item_data in self.pop_links:
                pop_links_item = pop_links_item_data.to_dict()
                pop_links.append(pop_links_item)

        remote_dia_links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.remote_dia_links, Unset):
            remote_dia_links = []
            for remote_dia_links_item_data in self.remote_dia_links:
                remote_dia_links_item = remote_dia_links_item_data.to_dict()
                remote_dia_links.append(remote_dia_links_item)

        risk_status = self.risk_status

        server_endpoint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_endpoint, Unset):
            server_endpoint = self.server_endpoint.to_dict()

        server_ip = self.server_ip

        server_links: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.server_links, Unset):
            server_links = []
            for server_links_item_data in self.server_links:
                server_links_item = server_links_item_data.to_dict()
                server_links.append(server_links_item)

        server_port = self.server_port

        session_id = self.session_id

        sla = self.sla

        sla_class = self.sla_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if client_endpoint is not UNSET:
            field_dict["clientEndpoint"] = client_endpoint
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if client_links is not UNSET:
            field_dict["clientLinks"] = client_links
        if first_seen_ts is not UNSET:
            field_dict["firstSeenTs"] = first_seen_ts
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if last_seen_ts is not UNSET:
            field_dict["lastSeenTs"] = last_seen_ts
        if local_dia_links is not UNSET:
            field_dict["localDiaLinks"] = local_dia_links
        if pop_links is not UNSET:
            field_dict["popLinks"] = pop_links
        if remote_dia_links is not UNSET:
            field_dict["remoteDiaLinks"] = remote_dia_links
        if risk_status is not UNSET:
            field_dict["riskStatus"] = risk_status
        if server_endpoint is not UNSET:
            field_dict["serverEndpoint"] = server_endpoint
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_links is not UNSET:
            field_dict["serverLinks"] = server_links
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if sla is not UNSET:
            field_dict["sla"] = sla
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_client_endpoint import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_client_links_item import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientLinksItem,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_first_seen_ts import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_last_seen_ts import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_local_dia_links_item import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLocalDiaLinksItem,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_pop_links_item import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemPopLinksItem,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_remote_dia_links_item import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemRemoteDiaLinksItem,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_endpoint import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint,
        )
        from ..models.post_v2_assurance_topology_client_sessions_response_200_sessions_item_server_links_item import (
            PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        bucket = d.pop("bucket", UNSET)

        _client_endpoint = d.pop("clientEndpoint", UNSET)
        client_endpoint: Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint]
        if isinstance(_client_endpoint, Unset):
            client_endpoint = UNSET
        else:
            client_endpoint = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientEndpoint.from_dict(
                _client_endpoint
            )

        client_ip = d.pop("clientIp", UNSET)

        client_links = []
        _client_links = d.pop("clientLinks", UNSET)
        for client_links_item_data in _client_links or []:
            client_links_item = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemClientLinksItem.from_dict(
                client_links_item_data
            )

            client_links.append(client_links_item)

        _first_seen_ts = d.pop("firstSeenTs", UNSET)
        first_seen_ts: Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs]
        if isinstance(_first_seen_ts, Unset):
            first_seen_ts = UNSET
        else:
            first_seen_ts = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemFirstSeenTs.from_dict(
                _first_seen_ts
            )

        lan_segment = cast(list[str], d.pop("lanSegment", UNSET))

        _last_seen_ts = d.pop("lastSeenTs", UNSET)
        last_seen_ts: Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs]
        if isinstance(_last_seen_ts, Unset):
            last_seen_ts = UNSET
        else:
            last_seen_ts = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLastSeenTs.from_dict(
                _last_seen_ts
            )

        local_dia_links = []
        _local_dia_links = d.pop("localDiaLinks", UNSET)
        for local_dia_links_item_data in _local_dia_links or []:
            local_dia_links_item = (
                PostV2AssuranceTopologyClientSessionsResponse200SessionsItemLocalDiaLinksItem.from_dict(
                    local_dia_links_item_data
                )
            )

            local_dia_links.append(local_dia_links_item)

        pop_links = []
        _pop_links = d.pop("popLinks", UNSET)
        for pop_links_item_data in _pop_links or []:
            pop_links_item = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemPopLinksItem.from_dict(
                pop_links_item_data
            )

            pop_links.append(pop_links_item)

        remote_dia_links = []
        _remote_dia_links = d.pop("remoteDiaLinks", UNSET)
        for remote_dia_links_item_data in _remote_dia_links or []:
            remote_dia_links_item = (
                PostV2AssuranceTopologyClientSessionsResponse200SessionsItemRemoteDiaLinksItem.from_dict(
                    remote_dia_links_item_data
                )
            )

            remote_dia_links.append(remote_dia_links_item)

        risk_status = d.pop("riskStatus", UNSET)

        _server_endpoint = d.pop("serverEndpoint", UNSET)
        server_endpoint: Union[Unset, PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint]
        if isinstance(_server_endpoint, Unset):
            server_endpoint = UNSET
        else:
            server_endpoint = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerEndpoint.from_dict(
                _server_endpoint
            )

        server_ip = d.pop("serverIp", UNSET)

        server_links = []
        _server_links = d.pop("serverLinks", UNSET)
        for server_links_item_data in _server_links or []:
            server_links_item = PostV2AssuranceTopologyClientSessionsResponse200SessionsItemServerLinksItem.from_dict(
                server_links_item_data
            )

            server_links.append(server_links_item)

        server_port = d.pop("serverPort", UNSET)

        session_id = d.pop("sessionId", UNSET)

        sla = d.pop("sla", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        post_v2_assurance_topology_client_sessions_response_200_sessions_item = cls(
            app_name=app_name,
            bucket=bucket,
            client_endpoint=client_endpoint,
            client_ip=client_ip,
            client_links=client_links,
            first_seen_ts=first_seen_ts,
            lan_segment=lan_segment,
            last_seen_ts=last_seen_ts,
            local_dia_links=local_dia_links,
            pop_links=pop_links,
            remote_dia_links=remote_dia_links,
            risk_status=risk_status,
            server_endpoint=server_endpoint,
            server_ip=server_ip,
            server_links=server_links,
            server_port=server_port,
            session_id=session_id,
            sla=sla,
            sla_class=sla_class,
        )

        post_v2_assurance_topology_client_sessions_response_200_sessions_item.additional_properties = d
        return post_v2_assurance_topology_client_sessions_response_200_sessions_item

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
