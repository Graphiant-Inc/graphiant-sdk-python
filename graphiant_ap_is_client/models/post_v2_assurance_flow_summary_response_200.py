from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_flow_summary_response_200_client_endpoint import (
        PostV2AssuranceFlowSummaryResponse200ClientEndpoint,
    )
    from ..models.post_v2_assurance_flow_summary_response_200_first_seen_ts import (
        PostV2AssuranceFlowSummaryResponse200FirstSeenTs,
    )
    from ..models.post_v2_assurance_flow_summary_response_200_last_seen_ts import (
        PostV2AssuranceFlowSummaryResponse200LastSeenTs,
    )
    from ..models.post_v2_assurance_flow_summary_response_200_server_endpoint import (
        PostV2AssuranceFlowSummaryResponse200ServerEndpoint,
    )


T = TypeVar("T", bound="PostV2AssuranceFlowSummaryResponse200")


@_attrs_define
class PostV2AssuranceFlowSummaryResponse200:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        bucket (Union[Unset, str]):  Example: TYPE_ENUM.
        client_endpoint (Union[Unset, PostV2AssuranceFlowSummaryResponse200ClientEndpoint]):
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        first_seen_ts (Union[Unset, PostV2AssuranceFlowSummaryResponse200FirstSeenTs]):
        lan_segment (Union[Unset, str]):  Example: TYPE_STRING.
        last_seen_ts (Union[Unset, PostV2AssuranceFlowSummaryResponse200LastSeenTs]):
        risk_status (Union[Unset, str]):  Example: TYPE_ENUM.
        server_endpoint (Union[Unset, PostV2AssuranceFlowSummaryResponse200ServerEndpoint]):
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_INT32.
        sla_class (Union[Unset, str]):  Example: TYPE_STRING.
    """

    app_name: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    client_endpoint: Union[Unset, "PostV2AssuranceFlowSummaryResponse200ClientEndpoint"] = UNSET
    client_ip: Union[Unset, str] = UNSET
    first_seen_ts: Union[Unset, "PostV2AssuranceFlowSummaryResponse200FirstSeenTs"] = UNSET
    lan_segment: Union[Unset, str] = UNSET
    last_seen_ts: Union[Unset, "PostV2AssuranceFlowSummaryResponse200LastSeenTs"] = UNSET
    risk_status: Union[Unset, str] = UNSET
    server_endpoint: Union[Unset, "PostV2AssuranceFlowSummaryResponse200ServerEndpoint"] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        bucket = self.bucket

        client_endpoint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_endpoint, Unset):
            client_endpoint = self.client_endpoint.to_dict()

        client_ip = self.client_ip

        first_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first_seen_ts, Unset):
            first_seen_ts = self.first_seen_ts.to_dict()

        lan_segment = self.lan_segment

        last_seen_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_seen_ts, Unset):
            last_seen_ts = self.last_seen_ts.to_dict()

        risk_status = self.risk_status

        server_endpoint: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.server_endpoint, Unset):
            server_endpoint = self.server_endpoint.to_dict()

        server_ip = self.server_ip

        server_port = self.server_port

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
        if first_seen_ts is not UNSET:
            field_dict["firstSeenTs"] = first_seen_ts
        if lan_segment is not UNSET:
            field_dict["lanSegment"] = lan_segment
        if last_seen_ts is not UNSET:
            field_dict["lastSeenTs"] = last_seen_ts
        if risk_status is not UNSET:
            field_dict["riskStatus"] = risk_status
        if server_endpoint is not UNSET:
            field_dict["serverEndpoint"] = server_endpoint
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_flow_summary_response_200_client_endpoint import (
            PostV2AssuranceFlowSummaryResponse200ClientEndpoint,
        )
        from ..models.post_v2_assurance_flow_summary_response_200_first_seen_ts import (
            PostV2AssuranceFlowSummaryResponse200FirstSeenTs,
        )
        from ..models.post_v2_assurance_flow_summary_response_200_last_seen_ts import (
            PostV2AssuranceFlowSummaryResponse200LastSeenTs,
        )
        from ..models.post_v2_assurance_flow_summary_response_200_server_endpoint import (
            PostV2AssuranceFlowSummaryResponse200ServerEndpoint,
        )

        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        bucket = d.pop("bucket", UNSET)

        _client_endpoint = d.pop("clientEndpoint", UNSET)
        client_endpoint: Union[Unset, PostV2AssuranceFlowSummaryResponse200ClientEndpoint]
        if isinstance(_client_endpoint, Unset):
            client_endpoint = UNSET
        else:
            client_endpoint = PostV2AssuranceFlowSummaryResponse200ClientEndpoint.from_dict(_client_endpoint)

        client_ip = d.pop("clientIp", UNSET)

        _first_seen_ts = d.pop("firstSeenTs", UNSET)
        first_seen_ts: Union[Unset, PostV2AssuranceFlowSummaryResponse200FirstSeenTs]
        if isinstance(_first_seen_ts, Unset):
            first_seen_ts = UNSET
        else:
            first_seen_ts = PostV2AssuranceFlowSummaryResponse200FirstSeenTs.from_dict(_first_seen_ts)

        lan_segment = d.pop("lanSegment", UNSET)

        _last_seen_ts = d.pop("lastSeenTs", UNSET)
        last_seen_ts: Union[Unset, PostV2AssuranceFlowSummaryResponse200LastSeenTs]
        if isinstance(_last_seen_ts, Unset):
            last_seen_ts = UNSET
        else:
            last_seen_ts = PostV2AssuranceFlowSummaryResponse200LastSeenTs.from_dict(_last_seen_ts)

        risk_status = d.pop("riskStatus", UNSET)

        _server_endpoint = d.pop("serverEndpoint", UNSET)
        server_endpoint: Union[Unset, PostV2AssuranceFlowSummaryResponse200ServerEndpoint]
        if isinstance(_server_endpoint, Unset):
            server_endpoint = UNSET
        else:
            server_endpoint = PostV2AssuranceFlowSummaryResponse200ServerEndpoint.from_dict(_server_endpoint)

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        post_v2_assurance_flow_summary_response_200 = cls(
            app_name=app_name,
            bucket=bucket,
            client_endpoint=client_endpoint,
            client_ip=client_ip,
            first_seen_ts=first_seen_ts,
            lan_segment=lan_segment,
            last_seen_ts=last_seen_ts,
            risk_status=risk_status,
            server_endpoint=server_endpoint,
            server_ip=server_ip,
            server_port=server_port,
            sla_class=sla_class,
        )

        post_v2_assurance_flow_summary_response_200.additional_properties = d
        return post_v2_assurance_flow_summary_response_200

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
