from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_bfd import (
        GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd,
    )
    from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_bfd_neighbors_item import (
        GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfdNeighborsItem,
    )
    from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_interfaces_item import (
        GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemInterfacesItem,
    )


T = TypeVar("T", bound="GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItem")


@_attrs_define
class GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItem:
    """
    Attributes:
        area_id (Union[Unset, str]):  Example: TYPE_STRING.
        bfd (Union[Unset, GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd]):
        bfd_neighbors (Union[Unset,
            list['GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfdNeighborsItem']]):
        id (Union[Unset, str]):  Example: TYPE_INT64.
        interfaces (Union[Unset, list['GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemInterfacesItem']]):
        name (Union[Unset, str]):  Example: TYPE_STRING.
        type_ (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    area_id: Union[Unset, str] = UNSET
    bfd: Union[Unset, "GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd"] = UNSET
    bfd_neighbors: Union[
        Unset, list["GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfdNeighborsItem"]
    ] = UNSET
    id: Union[Unset, str] = UNSET
    interfaces: Union[Unset, list["GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemInterfacesItem"]] = (
        UNSET
    )
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_id = self.area_id

        bfd: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bfd, Unset):
            bfd = self.bfd.to_dict()

        bfd_neighbors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bfd_neighbors, Unset):
            bfd_neighbors = []
            for bfd_neighbors_item_data in self.bfd_neighbors:
                bfd_neighbors_item = bfd_neighbors_item_data.to_dict()
                bfd_neighbors.append(bfd_neighbors_item)

        id = self.id

        interfaces: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_id is not UNSET:
            field_dict["areaId"] = area_id
        if bfd is not UNSET:
            field_dict["bfd"] = bfd
        if bfd_neighbors is not UNSET:
            field_dict["bfdNeighbors"] = bfd_neighbors
        if id is not UNSET:
            field_dict["id"] = id
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_bfd import (
            GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd,
        )
        from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_bfd_neighbors_item import (
            GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfdNeighborsItem,
        )
        from ..models.get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item_interfaces_item import (
            GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemInterfacesItem,
        )

        d = src_dict.copy()
        area_id = d.pop("areaId", UNSET)

        _bfd = d.pop("bfd", UNSET)
        bfd: Union[Unset, GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd]
        if isinstance(_bfd, Unset):
            bfd = UNSET
        else:
            bfd = GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfd.from_dict(_bfd)

        bfd_neighbors = []
        _bfd_neighbors = d.pop("bfdNeighbors", UNSET)
        for bfd_neighbors_item_data in _bfd_neighbors or []:
            bfd_neighbors_item = (
                GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemBfdNeighborsItem.from_dict(
                    bfd_neighbors_item_data
                )
            )

            bfd_neighbors.append(bfd_neighbors_item)

        id = d.pop("id", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = GetV1LanSegmentsResponse200SegmentsItemOspfv2ProcessAreasItemInterfacesItem.from_dict(
                interfaces_item_data
            )

            interfaces.append(interfaces_item)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item = cls(
            area_id=area_id,
            bfd=bfd,
            bfd_neighbors=bfd_neighbors,
            id=id,
            interfaces=interfaces,
            name=name,
            type_=type_,
        )

        get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item.additional_properties = d
        return get_v1_lan_segments_response_200_segments_item_ospfv_2_process_areas_item

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
