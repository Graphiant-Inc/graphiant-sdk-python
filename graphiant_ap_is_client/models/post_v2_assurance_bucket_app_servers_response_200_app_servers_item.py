from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AssuranceBucketAppServersResponse200AppServersItem")


@_attrs_define
class PostV2AssuranceBucketAppServersResponse200AppServersItem:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TYPE_STRING.
        app_server_key (Union[Unset, str]):  Example: TYPE_STRING.
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_STRING.
        server_protocol (Union[Unset, str]):  Example: TYPE_STRING.
    """

    app_name: Union[Unset, str] = UNSET
    app_server_key: Union[Unset, str] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    server_protocol: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_name = self.app_name

        app_server_key = self.app_server_key

        server_ip = self.server_ip

        server_port = self.server_port

        server_protocol = self.server_protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if app_server_key is not UNSET:
            field_dict["appServerKey"] = app_server_key
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if server_protocol is not UNSET:
            field_dict["serverProtocol"] = server_protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        app_name = d.pop("appName", UNSET)

        app_server_key = d.pop("appServerKey", UNSET)

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        server_protocol = d.pop("serverProtocol", UNSET)

        post_v2_assurance_bucket_app_servers_response_200_app_servers_item = cls(
            app_name=app_name,
            app_server_key=app_server_key,
            server_ip=server_ip,
            server_port=server_port,
            server_protocol=server_protocol,
        )

        post_v2_assurance_bucket_app_servers_response_200_app_servers_item.additional_properties = d
        return post_v2_assurance_bucket_app_servers_response_200_app_servers_item

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
