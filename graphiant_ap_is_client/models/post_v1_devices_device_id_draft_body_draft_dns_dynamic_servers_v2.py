from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_device_id_draft_body_draft_dns_dynamic_servers_v2_servers_item import (
        PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2ServersItem,
    )


T = TypeVar("T", bound="PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2")


@_attrs_define
class PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2:
    """
    Attributes:
        circuit (Union[Unset, str]):  Example: TYPE_STRING.
        servers (Union[Unset, list['PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2ServersItem']]):
    """

    circuit: Union[Unset, str] = UNSET
    servers: Union[Unset, list["PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2ServersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit = self.circuit

        servers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit is not UNSET:
            field_dict["circuit"] = circuit
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_device_id_draft_body_draft_dns_dynamic_servers_v2_servers_item import (
            PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2ServersItem,
        )

        d = src_dict.copy()
        circuit = d.pop("circuit", UNSET)

        servers = []
        _servers = d.pop("servers", UNSET)
        for servers_item_data in _servers or []:
            servers_item = PostV1DevicesDeviceIdDraftBodyDraftDnsDynamicServersV2ServersItem.from_dict(
                servers_item_data
            )

            servers.append(servers_item)

        post_v1_devices_device_id_draft_body_draft_dns_dynamic_servers_v2 = cls(
            circuit=circuit,
            servers=servers,
        )

        post_v1_devices_device_id_draft_body_draft_dns_dynamic_servers_v2.additional_properties = d
        return post_v1_devices_device_id_draft_body_draft_dns_dynamic_servers_v2

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
