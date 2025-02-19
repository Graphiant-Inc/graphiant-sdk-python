from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_control_connection_item import (
        GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsControlConnectionItem,
    )
    from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_core_connection_item import (
        GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsCoreConnectionItem,
    )
    from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_management_connection_item import (
        GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsManagementConnectionItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections")


@_attrs_define
class GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnections:
    """
    Attributes:
        control_connection (Union[Unset,
            list['GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsControlConnectionItem']]):
        core_connection (Union[Unset,
            list['GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsCoreConnectionItem']]):
        management_connection (Union[Unset,
            list['GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsManagementConnectionItem']]):
    """

    control_connection: Union[
        Unset, list["GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsControlConnectionItem"]
    ] = UNSET
    core_connection: Union[
        Unset, list["GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsCoreConnectionItem"]
    ] = UNSET
    management_connection: Union[
        Unset, list["GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsManagementConnectionItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_connection: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.control_connection, Unset):
            control_connection = []
            for control_connection_item_data in self.control_connection:
                control_connection_item = control_connection_item_data.to_dict()
                control_connection.append(control_connection_item)

        core_connection: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.core_connection, Unset):
            core_connection = []
            for core_connection_item_data in self.core_connection:
                core_connection_item = core_connection_item_data.to_dict()
                core_connection.append(core_connection_item)

        management_connection: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.management_connection, Unset):
            management_connection = []
            for management_connection_item_data in self.management_connection:
                management_connection_item = management_connection_item_data.to_dict()
                management_connection.append(management_connection_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_connection is not UNSET:
            field_dict["controlConnection"] = control_connection
        if core_connection is not UNSET:
            field_dict["coreConnection"] = core_connection
        if management_connection is not UNSET:
            field_dict["managementConnection"] = management_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_control_connection_item import (
            GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsControlConnectionItem,
        )
        from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_core_connection_item import (
            GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsCoreConnectionItem,
        )
        from ..models.get_v1_devices_device_id_connectivity_response_200_nodes_item_connections_management_connection_item import (
            GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsManagementConnectionItem,
        )

        d = src_dict.copy()
        control_connection = []
        _control_connection = d.pop("controlConnection", UNSET)
        for control_connection_item_data in _control_connection or []:
            control_connection_item = (
                GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsControlConnectionItem.from_dict(
                    control_connection_item_data
                )
            )

            control_connection.append(control_connection_item)

        core_connection = []
        _core_connection = d.pop("coreConnection", UNSET)
        for core_connection_item_data in _core_connection or []:
            core_connection_item = (
                GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsCoreConnectionItem.from_dict(
                    core_connection_item_data
                )
            )

            core_connection.append(core_connection_item)

        management_connection = []
        _management_connection = d.pop("managementConnection", UNSET)
        for management_connection_item_data in _management_connection or []:
            management_connection_item = (
                GetV1DevicesDeviceIdConnectivityResponse200NodesItemConnectionsManagementConnectionItem.from_dict(
                    management_connection_item_data
                )
            )

            management_connection.append(management_connection_item)

        get_v1_devices_device_id_connectivity_response_200_nodes_item_connections = cls(
            control_connection=control_connection,
            core_connection=core_connection,
            management_connection=management_connection,
        )

        get_v1_devices_device_id_connectivity_response_200_nodes_item_connections.additional_properties = d
        return get_v1_devices_device_id_connectivity_response_200_nodes_item_connections

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
