from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item import (
        GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem,
    )


T = TypeVar("T", bound="GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem")


@_attrs_define
class GetV1DevicesDeviceIdSlicePeersResponse200SlicesItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: TYPE_INT32.
        peers (Union[Unset, list['GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem']]):
        slice_index (Union[Unset, str]):  Example: TYPE_INT32.
        tags (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
    """

    id: Union[Unset, str] = UNSET
    peers: Union[Unset, list["GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem"]] = UNSET
    slice_index: Union[Unset, str] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        peers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.peers, Unset):
            peers = []
            for peers_item_data in self.peers:
                peers_item = peers_item_data.to_dict()
                peers.append(peers_item)

        slice_index = self.slice_index

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if peers is not UNSET:
            field_dict["peers"] = peers
        if slice_index is not UNSET:
            field_dict["sliceIndex"] = slice_index
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_v1_devices_device_id_slice_peers_response_200_slices_item_peers_item import (
            GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem,
        )

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        peers = []
        _peers = d.pop("peers", UNSET)
        for peers_item_data in _peers or []:
            peers_item = GetV1DevicesDeviceIdSlicePeersResponse200SlicesItemPeersItem.from_dict(peers_item_data)

            peers.append(peers_item)

        slice_index = d.pop("sliceIndex", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        get_v1_devices_device_id_slice_peers_response_200_slices_item = cls(
            id=id,
            peers=peers,
            slice_index=slice_index,
            tags=tags,
        )

        get_v1_devices_device_id_slice_peers_response_200_slices_item.additional_properties = d
        return get_v1_devices_device_id_slice_peers_response_200_slices_item

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
