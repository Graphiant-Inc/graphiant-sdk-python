from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_diagnostic_speedtest_servers_response_200_server_item import (
        GetV1DiagnosticSpeedtestServersResponse200ServerItem,
    )


T = TypeVar("T", bound="GetV1DiagnosticSpeedtestServersResponse200")


@_attrs_define
class GetV1DiagnosticSpeedtestServersResponse200:
    """
    Attributes:
        server (Union[Unset, list['GetV1DiagnosticSpeedtestServersResponse200ServerItem']]):
    """

    server: Union[Unset, list["GetV1DiagnosticSpeedtestServersResponse200ServerItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.server, Unset):
            server = []
            for server_item_data in self.server:
                server_item = server_item_data.to_dict()
                server.append(server_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_diagnostic_speedtest_servers_response_200_server_item import (
            GetV1DiagnosticSpeedtestServersResponse200ServerItem,
        )

        d = src_dict.copy()
        server = []
        _server = d.pop("server", UNSET)
        for server_item_data in _server or []:
            server_item = GetV1DiagnosticSpeedtestServersResponse200ServerItem.from_dict(server_item_data)

            server.append(server_item)

        get_v1_diagnostic_speedtest_servers_response_200 = cls(
            server=server,
        )

        get_v1_diagnostic_speedtest_servers_response_200.additional_properties = d
        return get_v1_diagnostic_speedtest_servers_response_200

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
