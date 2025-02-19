from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process_areas_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessAreasItem,
    )
    from ..models.get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process_redistributed_protocols_item import (
        GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessRedistributedProtocolsItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2Process")


@_attrs_define
class GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2Process:
    """
    Attributes:
        admin_distance (Union[Unset, str]):  Example: 100.
        areas (Union[Unset, list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessAreasItem']]):
        auto_router_id (Union[Unset, str]):  Example: TYPE_BOOL.
        default_originate (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        redistributed_protocols (Union[Unset,
            list['GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessRedistributedProtocolsItem']]):
        router_id (Union[Unset, str]):  Example: TYPE_STRING.
    """

    admin_distance: Union[Unset, str] = UNSET
    areas: Union[Unset, list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessAreasItem"]] = (
        UNSET
    )
    auto_router_id: Union[Unset, str] = UNSET
    default_originate: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    redistributed_protocols: Union[
        Unset,
        list["GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessRedistributedProtocolsItem"],
    ] = UNSET
    router_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_distance = self.admin_distance

        areas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.areas, Unset):
            areas = []
            for areas_item_data in self.areas:
                areas_item = areas_item_data.to_dict()
                areas.append(areas_item)

        auto_router_id = self.auto_router_id

        default_originate = self.default_originate

        id = self.id

        redistributed_protocols: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.redistributed_protocols, Unset):
            redistributed_protocols = []
            for redistributed_protocols_item_data in self.redistributed_protocols:
                redistributed_protocols_item = redistributed_protocols_item_data.to_dict()
                redistributed_protocols.append(redistributed_protocols_item)

        router_id = self.router_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_distance is not UNSET:
            field_dict["adminDistance"] = admin_distance
        if areas is not UNSET:
            field_dict["areas"] = areas
        if auto_router_id is not UNSET:
            field_dict["autoRouterId"] = auto_router_id
        if default_originate is not UNSET:
            field_dict["defaultOriginate"] = default_originate
        if id is not UNSET:
            field_dict["id"] = id
        if redistributed_protocols is not UNSET:
            field_dict["redistributedProtocols"] = redistributed_protocols
        if router_id is not UNSET:
            field_dict["routerId"] = router_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process_areas_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessAreasItem,
        )
        from ..models.get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process_redistributed_protocols_item import (
            GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessRedistributedProtocolsItem,
        )

        d = src_dict.copy()
        admin_distance = d.pop("adminDistance", UNSET)

        areas = []
        _areas = d.pop("areas", UNSET)
        for areas_item_data in _areas or []:
            areas_item = GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessAreasItem.from_dict(
                areas_item_data
            )

            areas.append(areas_item)

        auto_router_id = d.pop("autoRouterId", UNSET)

        default_originate = d.pop("defaultOriginate", UNSET)

        id = d.pop("id", UNSET)

        redistributed_protocols = []
        _redistributed_protocols = d.pop("redistributedProtocols", UNSET)
        for redistributed_protocols_item_data in _redistributed_protocols or []:
            redistributed_protocols_item = GetV1DevicesDeviceIdEdgesResponse200DevicesItemSegmentsItemOspfv2ProcessRedistributedProtocolsItem.from_dict(
                redistributed_protocols_item_data
            )

            redistributed_protocols.append(redistributed_protocols_item)

        router_id = d.pop("routerId", UNSET)

        get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process = cls(
            admin_distance=admin_distance,
            areas=areas,
            auto_router_id=auto_router_id,
            default_originate=default_originate,
            id=id,
            redistributed_protocols=redistributed_protocols,
            router_id=router_id,
        )

        get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process.additional_properties = d
        return get_v1_devices_device_id_edges_response_200_devices_item_segments_item_ospfv_2_process

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
