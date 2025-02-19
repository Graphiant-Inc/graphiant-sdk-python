from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_device_device_id_topology_response_200_edges_item_circuits_info_item_uptime import (
        PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime,
    )


T = TypeVar("T", bound="PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItem")


@_attrs_define
class PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItem:
    """
    Attributes:
        circuit_carrier (Union[Unset, str]):  Example: TYPE_STRING.
        circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        device_hostname (Union[Unset, str]):  Example: TYPE_STRING.
        interface_name (Union[Unset, str]):  Example: TYPE_STRING.
        label (Union[Unset, str]):  Example: TYPE_ENUM.
        last_resort_circuit (Union[Unset, str]):  Example: TYPE_BOOL.
        quality (Union[Unset, str]):  Example: TYPE_ENUM.
        source_ip (Union[Unset, str]):  Example: TYPE_STRING.
        source_public_ip (Union[Unset, str]):  Example: TYPE_STRING.
        uptime (Union[Unset, PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime]):
    """

    circuit_carrier: Union[Unset, str] = UNSET
    circuit_name: Union[Unset, str] = UNSET
    device_hostname: Union[Unset, str] = UNSET
    interface_name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    last_resort_circuit: Union[Unset, str] = UNSET
    quality: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    source_public_ip: Union[Unset, str] = UNSET
    uptime: Union[Unset, "PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        circuit_carrier = self.circuit_carrier

        circuit_name = self.circuit_name

        device_hostname = self.device_hostname

        interface_name = self.interface_name

        label = self.label

        last_resort_circuit = self.last_resort_circuit

        quality = self.quality

        source_ip = self.source_ip

        source_public_ip = self.source_public_ip

        uptime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uptime, Unset):
            uptime = self.uptime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if circuit_carrier is not UNSET:
            field_dict["circuitCarrier"] = circuit_carrier
        if circuit_name is not UNSET:
            field_dict["circuitName"] = circuit_name
        if device_hostname is not UNSET:
            field_dict["deviceHostname"] = device_hostname
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if label is not UNSET:
            field_dict["label"] = label
        if last_resort_circuit is not UNSET:
            field_dict["lastResortCircuit"] = last_resort_circuit
        if quality is not UNSET:
            field_dict["quality"] = quality
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if source_public_ip is not UNSET:
            field_dict["sourcePublicIp"] = source_public_ip
        if uptime is not UNSET:
            field_dict["uptime"] = uptime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_device_device_id_topology_response_200_edges_item_circuits_info_item_uptime import (
            PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime,
        )

        d = src_dict.copy()
        circuit_carrier = d.pop("circuitCarrier", UNSET)

        circuit_name = d.pop("circuitName", UNSET)

        device_hostname = d.pop("deviceHostname", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        label = d.pop("label", UNSET)

        last_resort_circuit = d.pop("lastResortCircuit", UNSET)

        quality = d.pop("quality", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        source_public_ip = d.pop("sourcePublicIp", UNSET)

        _uptime = d.pop("uptime", UNSET)
        uptime: Union[Unset, PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime]
        if isinstance(_uptime, Unset):
            uptime = UNSET
        else:
            uptime = PostV2DeviceDeviceIdTopologyResponse200EdgesItemCircuitsInfoItemUptime.from_dict(_uptime)

        post_v2_device_device_id_topology_response_200_edges_item_circuits_info_item = cls(
            circuit_carrier=circuit_carrier,
            circuit_name=circuit_name,
            device_hostname=device_hostname,
            interface_name=interface_name,
            label=label,
            last_resort_circuit=last_resort_circuit,
            quality=quality,
            source_ip=source_ip,
            source_public_ip=source_public_ip,
            uptime=uptime,
        )

        post_v2_device_device_id_topology_response_200_edges_item_circuits_info_item.additional_properties = d
        return post_v2_device_device_id_topology_response_200_edges_item_circuits_info_item

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
