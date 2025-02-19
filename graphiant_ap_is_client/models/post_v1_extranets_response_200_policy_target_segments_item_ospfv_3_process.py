from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process_areas_item import (
        PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessAreasItem,
    )
    from ..models.post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process_redistributed_protocols_item import (
        PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessRedistributedProtocolsItem,
    )


T = TypeVar("T", bound="PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3Process")


@_attrs_define
class PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3Process:
    """
    Attributes:
        admin_distance (Union[Unset, str]):  Example: 100.
        areas (Union[Unset, list['PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessAreasItem']]):
        default_originate (Union[Unset, str]):  Example: TYPE_ENUM.
        id (Union[Unset, str]):  Example: TYPE_INT64.
        redistributed_protocols (Union[Unset,
            list['PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessRedistributedProtocolsItem']]):
        router_id (Union[Unset, str]):  Example: TYPE_STRING.
        version (Union[Unset, str]):  Example: TYPE_UINT32.
    """

    admin_distance: Union[Unset, str] = UNSET
    areas: Union[Unset, list["PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessAreasItem"]] = UNSET
    default_originate: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    redistributed_protocols: Union[
        Unset, list["PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessRedistributedProtocolsItem"]
    ] = UNSET
    router_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_distance = self.admin_distance

        areas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.areas, Unset):
            areas = []
            for areas_item_data in self.areas:
                areas_item = areas_item_data.to_dict()
                areas.append(areas_item)

        default_originate = self.default_originate

        id = self.id

        redistributed_protocols: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.redistributed_protocols, Unset):
            redistributed_protocols = []
            for redistributed_protocols_item_data in self.redistributed_protocols:
                redistributed_protocols_item = redistributed_protocols_item_data.to_dict()
                redistributed_protocols.append(redistributed_protocols_item)

        router_id = self.router_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin_distance is not UNSET:
            field_dict["adminDistance"] = admin_distance
        if areas is not UNSET:
            field_dict["areas"] = areas
        if default_originate is not UNSET:
            field_dict["defaultOriginate"] = default_originate
        if id is not UNSET:
            field_dict["id"] = id
        if redistributed_protocols is not UNSET:
            field_dict["redistributedProtocols"] = redistributed_protocols
        if router_id is not UNSET:
            field_dict["routerId"] = router_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process_areas_item import (
            PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessAreasItem,
        )
        from ..models.post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process_redistributed_protocols_item import (
            PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessRedistributedProtocolsItem,
        )

        d = src_dict.copy()
        admin_distance = d.pop("adminDistance", UNSET)

        areas = []
        _areas = d.pop("areas", UNSET)
        for areas_item_data in _areas or []:
            areas_item = PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessAreasItem.from_dict(
                areas_item_data
            )

            areas.append(areas_item)

        default_originate = d.pop("defaultOriginate", UNSET)

        id = d.pop("id", UNSET)

        redistributed_protocols = []
        _redistributed_protocols = d.pop("redistributedProtocols", UNSET)
        for redistributed_protocols_item_data in _redistributed_protocols or []:
            redistributed_protocols_item = (
                PostV1ExtranetsResponse200PolicyTargetSegmentsItemOspfv3ProcessRedistributedProtocolsItem.from_dict(
                    redistributed_protocols_item_data
                )
            )

            redistributed_protocols.append(redistributed_protocols_item)

        router_id = d.pop("routerId", UNSET)

        version = d.pop("version", UNSET)

        post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process = cls(
            admin_distance=admin_distance,
            areas=areas,
            default_originate=default_originate,
            id=id,
            redistributed_protocols=redistributed_protocols,
            router_id=router_id,
            version=version,
        )

        post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process.additional_properties = d
        return post_v1_extranets_response_200_policy_target_segments_item_ospfv_3_process

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
