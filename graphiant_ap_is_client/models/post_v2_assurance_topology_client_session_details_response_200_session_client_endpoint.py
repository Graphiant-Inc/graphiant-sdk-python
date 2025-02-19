from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_edges_item import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointEdgesItem,
    )
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_jitter import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter,
    )
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_latency import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency,
    )
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_loss import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss,
    )
    from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_site import (
        PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite,
    )


T = TypeVar("T", bound="PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpoint")


@_attrs_define
class PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpoint:
    """
    Attributes:
        circuits (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        edges (Union[Unset,
            list['PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointEdgesItem']]):
        jitter (Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter]):
        latency (Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency]):
        loss (Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss]):
        site (Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite]):
        total_downlink_usage (Union[Unset, str]):  Example: TYPE_INT64.
        total_uplink_usage (Union[Unset, str]):  Example: TYPE_INT64.
    """

    circuits: Union[Unset, list[str]] = UNSET
    edges: Union[
        Unset, list["PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointEdgesItem"]
    ] = UNSET
    jitter: Union[Unset, "PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter"] = UNSET
    latency: Union[Unset, "PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency"] = UNSET
    loss: Union[Unset, "PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss"] = UNSET
    site: Union[Unset, "PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite"] = UNSET
    total_downlink_usage: Union[Unset, str] = UNSET
    total_uplink_usage: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuits: Union[Unset, list[str]] = UNSET
        if not isinstance(self.circuits, Unset):
            circuits = self.circuits

        edges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        jitter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.jitter, Unset):
            jitter = self.jitter.to_dict()

        latency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.latency, Unset):
            latency = self.latency.to_dict()

        loss: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.loss, Unset):
            loss = self.loss.to_dict()

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        total_downlink_usage = self.total_downlink_usage

        total_uplink_usage = self.total_uplink_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuits is not UNSET:
            field_dict["circuits"] = circuits
        if edges is not UNSET:
            field_dict["edges"] = edges
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if site is not UNSET:
            field_dict["site"] = site
        if total_downlink_usage is not UNSET:
            field_dict["totalDownlinkUsage"] = total_downlink_usage
        if total_uplink_usage is not UNSET:
            field_dict["totalUplinkUsage"] = total_uplink_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_edges_item import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointEdgesItem,
        )
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_jitter import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter,
        )
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_latency import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency,
        )
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_loss import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss,
        )
        from ..models.post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint_site import (
            PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite,
        )

        d = src_dict.copy()
        circuits = cast(list[str], d.pop("circuits", UNSET))

        edges = []
        _edges = d.pop("edges", UNSET)
        for edges_item_data in _edges or []:
            edges_item = PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointEdgesItem.from_dict(
                edges_item_data
            )

            edges.append(edges_item)

        _jitter = d.pop("jitter", UNSET)
        jitter: Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter]
        if isinstance(_jitter, Unset):
            jitter = UNSET
        else:
            jitter = PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointJitter.from_dict(
                _jitter
            )

        _latency = d.pop("latency", UNSET)
        latency: Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency]
        if isinstance(_latency, Unset):
            latency = UNSET
        else:
            latency = PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLatency.from_dict(
                _latency
            )

        _loss = d.pop("loss", UNSET)
        loss: Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss]
        if isinstance(_loss, Unset):
            loss = UNSET
        else:
            loss = PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointLoss.from_dict(_loss)

        _site = d.pop("site", UNSET)
        site: Union[Unset, PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = PostV2AssuranceTopologyClientSessionDetailsResponse200SessionClientEndpointSite.from_dict(_site)

        total_downlink_usage = d.pop("totalDownlinkUsage", UNSET)

        total_uplink_usage = d.pop("totalUplinkUsage", UNSET)

        post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint = cls(
            circuits=circuits,
            edges=edges,
            jitter=jitter,
            latency=latency,
            loss=loss,
            site=site,
            total_downlink_usage=total_downlink_usage,
            total_uplink_usage=total_uplink_usage,
        )

        post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint.additional_properties = d
        return post_v2_assurance_topology_client_session_details_response_200_session_client_endpoint

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
