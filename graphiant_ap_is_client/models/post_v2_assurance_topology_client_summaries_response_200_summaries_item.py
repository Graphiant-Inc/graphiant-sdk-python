from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceTopologyClientSummariesResponse200SummariesItem")


@_attrs_define
class PostV2AssuranceTopologyClientSummariesResponse200SummariesItem:
    """
    Attributes:
        app_server_key (Union[Unset, str]):  Example: TYPE_STRING.
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        lan_segments (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_INT32.
        server_site_name (Union[Unset, str]):  Example: TYPE_STRING.
        session_count (Union[Unset, str]):  Example: TYPE_INT32.
    """

    app_server_key: Union[Unset, str] = UNSET
    client_ip: Union[Unset, str] = UNSET
    lan_segments: Union[Unset, list[str]] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    server_site_name: Union[Unset, str] = UNSET
    session_count: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_server_key = self.app_server_key

        client_ip = self.client_ip

        lan_segments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.lan_segments, Unset):
            lan_segments = self.lan_segments

        server_ip = self.server_ip

        server_port = self.server_port

        server_site_name = self.server_site_name

        session_count = self.session_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_server_key is not UNSET:
            field_dict["appServerKey"] = app_server_key
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if lan_segments is not UNSET:
            field_dict["lanSegments"] = lan_segments
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if server_site_name is not UNSET:
            field_dict["serverSiteName"] = server_site_name
        if session_count is not UNSET:
            field_dict["sessionCount"] = session_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_server_key = d.pop("appServerKey", UNSET)

        client_ip = d.pop("clientIp", UNSET)

        lan_segments = cast(list[str], d.pop("lanSegments", UNSET))

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        server_site_name = d.pop("serverSiteName", UNSET)

        session_count = d.pop("sessionCount", UNSET)

        post_v2_assurance_topology_client_summaries_response_200_summaries_item = cls(
            app_server_key=app_server_key,
            client_ip=client_ip,
            lan_segments=lan_segments,
            server_ip=server_ip,
            server_port=server_port,
            server_site_name=server_site_name,
            session_count=session_count,
        )

        post_v2_assurance_topology_client_summaries_response_200_summaries_item.additional_properties = d
        return post_v2_assurance_topology_client_summaries_response_200_summaries_item

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
