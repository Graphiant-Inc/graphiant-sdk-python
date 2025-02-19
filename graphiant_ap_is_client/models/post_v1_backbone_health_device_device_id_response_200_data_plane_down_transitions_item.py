from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane_down_transitions_item_transitions_item import (
        PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItemTransitionsItem,
    )


T = TypeVar("T", bound="PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItem")


@_attrs_define
class PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: TYPE_STRING.
        transitions (Union[Unset,
            list['PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItemTransitionsItem']]):
    """

    name: Union[Unset, str] = UNSET
    transitions: Union[
        Unset, list["PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItemTransitionsItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transitions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if transitions is not UNSET:
            field_dict["transitions"] = transitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_backbone_health_device_device_id_response_200_data_plane_down_transitions_item_transitions_item import (
            PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItemTransitionsItem,
        )

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        transitions = []
        _transitions = d.pop("transitions", UNSET)
        for transitions_item_data in _transitions or []:
            transitions_item = (
                PostV1BackboneHealthDeviceDeviceIdResponse200DataPlaneDownTransitionsItemTransitionsItem.from_dict(
                    transitions_item_data
                )
            )

            transitions.append(transitions_item)

        post_v1_backbone_health_device_device_id_response_200_data_plane_down_transitions_item = cls(
            name=name,
            transitions=transitions,
        )

        post_v1_backbone_health_device_device_id_response_200_data_plane_down_transitions_item.additional_properties = d
        return post_v1_backbone_health_device_device_id_response_200_data_plane_down_transitions_item

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
