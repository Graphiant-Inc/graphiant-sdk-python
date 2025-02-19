from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_topology_response_200_edges_item_connections_item_last_established_time import (
        PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItem")


@_attrs_define
class PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItem:
    """
    Attributes:
        active (Union[Unset, str]):  Example: TYPE_BOOL.
        circuit_carrier (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        destination_ip (Union[Unset, str]):  Example: TYPE_STRING.
        hostname (Union[Unset, str]):  Example: TYPE_STRING.
        last_established_time (Union[Unset,
            PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime]):
        last_resort (Union[Unset, str]):  Example: TYPE_BOOL.
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
        source_ip (Union[Unset, str]):  Example: TYPE_STRING.
        source_public_ip (Union[Unset, str]):  Example: TYPE_STRING.
    """

    active: Union[Unset, str] = UNSET
    circuit_carrier: Union[Unset, str] = UNSET
    circuit_name: Union[Unset, str] = UNSET
    destination_ip: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    last_established_time: Union[
        Unset, "PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime"
    ] = UNSET
    last_resort: Union[Unset, str] = UNSET
    quality: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    source_public_ip: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        circuit_carrier = self.circuit_carrier

        circuit_name = self.circuit_name

        destination_ip = self.destination_ip

        hostname = self.hostname

        last_established_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_established_time, Unset):
            last_established_time = self.last_established_time.to_dict()

        last_resort = self.last_resort

        quality = self.quality

        source_ip = self.source_ip

        source_public_ip = self.source_public_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if circuit_carrier is not UNSET:
            field_dict["circuitCarrier"] = circuit_carrier
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if destination_ip is not UNSET:
            field_dict["destinationIp"] = destination_ip
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if last_established_time is not UNSET:
            field_dict["lastEstablishedTime"] = last_established_time
        if last_resort is not UNSET:
            field_dict["lastResort"] = last_resort
        if quality is not UNSET:
            field_dict["quality"] = quality
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if source_public_ip is not UNSET:
            field_dict["sourcePublicIp"] = source_public_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_topology_response_200_edges_item_connections_item_last_established_time import (
            PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime,
        )

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        circuit_carrier = d.pop("circuitCarrier", UNSET)

        circuit_name = d.pop("circuitName", UNSET)

        destination_ip = d.pop("destinationIp", UNSET)

        hostname = d.pop("hostname", UNSET)

        _last_established_time = d.pop("lastEstablishedTime", UNSET)
        last_established_time: Union[
            Unset, PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime
        ]
        if isinstance(_last_established_time, Unset):
            last_established_time = UNSET
        else:
            last_established_time = (
                PostV2DeviceDeviceIdTopologyResponse200EdgesItemConnectionsItemLastEstablishedTime.from_dict(
                    _last_established_time
                )
            )

        last_resort = d.pop("lastResort", UNSET)

        quality = d.pop("quality", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        source_public_ip = d.pop("sourcePublicIp", UNSET)

        post_v2_device_device_id_topology_response_200_edges_item_connections_item = cls(
            active=active,
            circuit_carrier=circuit_carrier,
            circuit_name=circuit_name,
            destination_ip=destination_ip,
            hostname=hostname,
            last_established_time=last_established_time,
            last_resort=last_resort,
            quality=quality,
            source_ip=source_ip,
            source_public_ip=source_public_ip,
        )

        post_v2_device_device_id_topology_response_200_edges_item_connections_item.additional_properties = d
        return post_v2_device_device_id_topology_response_200_edges_item_connections_item

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
