from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_connectivity_response_200_edges_item_connections_control_connection_item_last_established_time import (
        GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItem")


@_attrs_define
class GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItem:
    """
    Attributes:
        dest_ip (Union[Unset, str]):  Example: TYPE_STRING.
        dest_port (Union[Unset, str]):  Example: TYPE_UINT32.
        last_established_time (Union[Unset,
            GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime]):
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
        source_ip (Union[Unset, str]):  Example: TYPE_STRING.
        source_port (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    dest_ip: Union[Unset, str] = UNSET
    dest_port: Union[Unset, str] = UNSET
    last_established_time: Union[
        Unset, "GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime"
    ] = UNSET
    quality: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    source_port: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dest_ip = self.dest_ip

        dest_port = self.dest_port

        last_established_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_established_time, Unset):
            last_established_time = self.last_established_time.to_dict()

        quality = self.quality

        source_ip = self.source_ip

        source_port = self.source_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest_ip is not UNSET:
            field_dict["destIp"] = dest_ip
        if dest_port is not UNSET:
            field_dict["destPort"] = dest_port
        if last_established_time is not UNSET:
            field_dict["lastEstablishedTime"] = last_established_time
        if quality is not UNSET:
            field_dict["quality"] = quality
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if source_port is not UNSET:
            field_dict["sourcePort"] = source_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_connectivity_response_200_edges_item_connections_control_connection_item_last_established_time import (
            GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime,
        )

        d = src_dict.copy()
        dest_ip = d.pop("destIp", UNSET)

        dest_port = d.pop("destPort", UNSET)

        _last_established_time = d.pop("lastEstablishedTime", UNSET)
        last_established_time: Union[
            Unset,
            GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime,
        ]
        if isinstance(_last_established_time, Unset):
            last_established_time = UNSET
        else:
            last_established_time = GetV1DevicesDeviceIdConnectivityResponse200EdgesItemConnectionsControlConnectionItemLastEstablishedTime.from_dict(
                _last_established_time
            )

        quality = d.pop("quality", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        source_port = d.pop("sourcePort", UNSET)

        get_v1_devices_device_id_connectivity_response_200_edges_item_connections_control_connection_item = cls(
            dest_ip=dest_ip,
            dest_port=dest_port,
            last_established_time=last_established_time,
            quality=quality,
            source_ip=source_ip,
            source_port=source_port,
        )

        get_v1_devices_device_id_connectivity_response_200_edges_item_connections_control_connection_item.additional_properties = d
        return get_v1_devices_device_id_connectivity_response_200_edges_item_connections_control_connection_item

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
