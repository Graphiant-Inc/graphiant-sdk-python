from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections import (
        GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdConnectivityResponse200NodesItem")


@_attrs_define
class GetV1DevicesDeviceIdConnectivityResponse200NodesItem:
    """
    Attributes:
        connections (Union[Unset, GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections]):
        id (Union[Unset, str]):  Example: TYPE_UINT32.
        name (Union[Unset, str]):  Example: TYPE_STRING.
        override_region (Union[Unset, str]):  Example: TYPE_STRING.
        region (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_STRING.
    """

    connections: Union[Unset, "GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections"] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    override_region: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.connections, Unset):
            connections = self.connections.to_dict()

        id = self.id

        name = self.name

        override_region = self.override_region

        region = self.region

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if override_region is not UNSET:
            field_dict["overrideRegion"] = override_region
        if region is not UNSET:
            field_dict["region"] = region
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections import (
            GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections,
        )

        d = src_dict.copy()
        _connections = d.pop("connections", UNSET)
        connections: Union[Unset, GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections]
        if isinstance(_connections, Unset):
            connections = UNSET
        else:
            connections = GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections.from_dict(_connections)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        override_region = d.pop("overrideRegion", UNSET)

        region = d.pop("region", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_devices_device_id_connectivity_response_200_nodes_item = cls(
            connections=connections,
            id=id,
            name=name,
            override_region=override_region,
            region=region,
            type_=type_,
        )

        get_v1_devices_device_id_connectivity_response_200_nodes_item.additional_properties = d
        return get_v1_devices_device_id_connectivity_response_200_nodes_item

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
