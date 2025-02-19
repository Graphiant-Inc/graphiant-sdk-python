from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem")


@_attrs_define
class PostV1GlobalTrafficPoliciesResponse200TrafficPolicyDpiApplicationsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: TYPE_STRING.
        destination_network (Union[Unset, str]):  Example: TYPE_STRING.
        destination_network_list (Union[Unset, str]):  Example: TYPE_STRING.
        destination_port (Union[Unset, str]):  Example: TYPE_UINT32.
        destination_port_list (Union[Unset, str]):  Example: TYPE_STRING.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        ip_protocol (Union[Unset, str]):  Example: TYPE_ENUM.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        source_network (Union[Unset, str]):  Example: TYPE_STRING.
        source_network_list (Union[Unset, str]):  Example: TYPE_STRING.
        source_port (Union[Unset, str]):  Example: TYPE_UINT32.
        source_port_list (Union[Unset, str]):  Example: TYPE_STRING.
    """

    description: Union[Unset, str] = UNSET
    destination_network: Union[Unset, str] = UNSET
    destination_network_list: Union[Unset, str] = UNSET
    destination_port: Union[Unset, str] = UNSET
    destination_port_list: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    ip_protocol: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    source_network: Union[Unset, str] = UNSET
    source_network_list: Union[Unset, str] = UNSET
    source_port: Union[Unset, str] = UNSET
    source_port_list: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        destination_network = self.destination_network

        destination_network_list = self.destination_network_list

        destination_port = self.destination_port

        destination_port_list = self.destination_port_list

        id = self.id

        ip_protocol = self.ip_protocol

        name = self.name

        source_network = self.source_network

        source_network_list = self.source_network_list

        source_port = self.source_port

        source_port_list = self.source_port_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if destination_network is not UNSET:
            field_dict["destinationNetwork"] = destination_network
        if destination_network_list is not UNSET:
            field_dict["destinationNetworkList"] = destination_network_list
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port
        if destination_port_list is not UNSET:
            field_dict["destinationPortList"] = destination_port_list
        if id is not UNSET:
            field_dict["id"] = id
        if ip_protocol is not UNSET:
            field_dict["ipProtocol"] = ip_protocol
        if name is not UNSET:
            field_dict["name"] = name
        if source_network is not UNSET:
            field_dict["sourceNetwork"] = source_network
        if source_network_list is not UNSET:
            field_dict["sourceNetworkList"] = source_network_list
        if source_port is not UNSET:
            field_dict["sourcePort"] = source_port
        if source_port_list is not UNSET:
            field_dict["sourcePortList"] = source_port_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        destination_network = d.pop("destinationNetwork", UNSET)

        destination_network_list = d.pop("destinationNetworkList", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        destination_port_list = d.pop("destinationPortList", UNSET)

        id = d.pop("id", UNSET)

        ip_protocol = d.pop("ipProtocol", UNSET)

        name = d.pop("name", UNSET)

        source_network = d.pop("sourceNetwork", UNSET)

        source_network_list = d.pop("sourceNetworkList", UNSET)

        source_port = d.pop("sourcePort", UNSET)

        source_port_list = d.pop("sourcePortList", UNSET)

        post_v1_global_traffic_policies_response_200_traffic_policy_dpi_applications_item = cls(
            description=description,
            destination_network=destination_network,
            destination_network_list=destination_network_list,
            destination_port=destination_port,
            destination_port_list=destination_port_list,
            id=id,
            ip_protocol=ip_protocol,
            name=name,
            source_network=source_network,
            source_network_list=source_network_list,
            source_port=source_port,
            source_port_list=source_port_list,
        )

        post_v1_global_traffic_policies_response_200_traffic_policy_dpi_applications_item.additional_properties = d
        return post_v1_global_traffic_policies_response_200_traffic_policy_dpi_applications_item

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
