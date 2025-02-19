from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_session_status_response_200_bgp_session_data_map_item import (
        PostV1DevicesSessionStatusResponse200BgpSessionDataMapItem,
    )
    from ..models.post_v1_devices_session_status_response_200_bgp_session_map_item import (
        PostV1DevicesSessionStatusResponse200BgpSessionMapItem,
    )
    from ..models.post_v1_devices_session_status_response_200_bgp_session_states_item import (
        PostV1DevicesSessionStatusResponse200BgpSessionStatesItem,
    )


T = TypeVar("T", bound="PostV1DevicesSessionStatusResponse200")


@_attrs_define
class PostV1DevicesSessionStatusResponse200:
    """
    Attributes:
        bgp_session_data_map (Union[Unset, list['PostV1DevicesSessionStatusResponse200BgpSessionDataMapItem']]):
        bgp_session_map (Union[Unset, list['PostV1DevicesSessionStatusResponse200BgpSessionMapItem']]):
        bgp_session_states (Union[Unset, list['PostV1DevicesSessionStatusResponse200BgpSessionStatesItem']]):
    """

    bgp_session_data_map: Union[Unset, list["PostV1DevicesSessionStatusResponse200BgpSessionDataMapItem"]] = UNSET
    bgp_session_map: Union[Unset, list["PostV1DevicesSessionStatusResponse200BgpSessionMapItem"]] = UNSET
    bgp_session_states: Union[Unset, list["PostV1DevicesSessionStatusResponse200BgpSessionStatesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgp_session_data_map: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_session_data_map, Unset):
            bgp_session_data_map = []
            for bgp_session_data_map_item_data in self.bgp_session_data_map:
                bgp_session_data_map_item = bgp_session_data_map_item_data.to_dict()
                bgp_session_data_map.append(bgp_session_data_map_item)

        bgp_session_map: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_session_map, Unset):
            bgp_session_map = []
            for bgp_session_map_item_data in self.bgp_session_map:
                bgp_session_map_item = bgp_session_map_item_data.to_dict()
                bgp_session_map.append(bgp_session_map_item)

        bgp_session_states: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bgp_session_states, Unset):
            bgp_session_states = []
            for bgp_session_states_item_data in self.bgp_session_states:
                bgp_session_states_item = bgp_session_states_item_data.to_dict()
                bgp_session_states.append(bgp_session_states_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgp_session_data_map is not UNSET:
            field_dict["bgpSessionDataMap"] = bgp_session_data_map
        if bgp_session_map is not UNSET:
            field_dict["bgpSessionMap"] = bgp_session_map
        if bgp_session_states is not UNSET:
            field_dict["bgpSessionStates"] = bgp_session_states

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_session_status_response_200_bgp_session_data_map_item import (
            PostV1DevicesSessionStatusResponse200BgpSessionDataMapItem,
        )
        from ..models.post_v1_devices_session_status_response_200_bgp_session_map_item import (
            PostV1DevicesSessionStatusResponse200BgpSessionMapItem,
        )
        from ..models.post_v1_devices_session_status_response_200_bgp_session_states_item import (
            PostV1DevicesSessionStatusResponse200BgpSessionStatesItem,
        )

        d = src_dict.copy()
        bgp_session_data_map = []
        _bgp_session_data_map = d.pop("bgpSessionDataMap", UNSET)
        for bgp_session_data_map_item_data in _bgp_session_data_map or []:
            bgp_session_data_map_item = PostV1DevicesSessionStatusResponse200BgpSessionDataMapItem.from_dict(
                bgp_session_data_map_item_data
            )

            bgp_session_data_map.append(bgp_session_data_map_item)

        bgp_session_map = []
        _bgp_session_map = d.pop("bgpSessionMap", UNSET)
        for bgp_session_map_item_data in _bgp_session_map or []:
            bgp_session_map_item = PostV1DevicesSessionStatusResponse200BgpSessionMapItem.from_dict(
                bgp_session_map_item_data
            )

            bgp_session_map.append(bgp_session_map_item)

        bgp_session_states = []
        _bgp_session_states = d.pop("bgpSessionStates", UNSET)
        for bgp_session_states_item_data in _bgp_session_states or []:
            bgp_session_states_item = PostV1DevicesSessionStatusResponse200BgpSessionStatesItem.from_dict(
                bgp_session_states_item_data
            )

            bgp_session_states.append(bgp_session_states_item)

        post_v1_devices_session_status_response_200 = cls(
            bgp_session_data_map=bgp_session_data_map,
            bgp_session_map=bgp_session_map,
            bgp_session_states=bgp_session_states,
        )

        post_v1_devices_session_status_response_200.additional_properties = d
        return post_v1_devices_session_status_response_200

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
