from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_down_transitions_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneDownTransitionsItem,
    )
    from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item import (
        PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem,
    )


T = TypeVar("T", bound="PostV1TroubleshootingDeviceDeviceIdResponse200DataPlane")


@_attrs_define
class PostV1TroubleshootingDeviceDeviceIdResponse200DataPlane:
    """
    Attributes:
        down_transitions (Union[Unset,
            list['PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneDownTransitionsItem']]):
        session_slas (Union[Unset, list['PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem']]):
        status (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    down_transitions: Union[
        Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneDownTransitionsItem"]
    ] = UNSET
    session_slas: Union[Unset, list["PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        down_transitions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.down_transitions, Unset):
            down_transitions = []
            for down_transitions_item_data in self.down_transitions:
                down_transitions_item = down_transitions_item_data.to_dict()
                down_transitions.append(down_transitions_item)

        session_slas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.session_slas, Unset):
            session_slas = []
            for session_slas_item_data in self.session_slas:
                session_slas_item = session_slas_item_data.to_dict()
                session_slas.append(session_slas_item)

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if down_transitions is not UNSET:
            field_dict["downTransitions"] = down_transitions
        if session_slas is not UNSET:
            field_dict["sessionSlas"] = session_slas
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_down_transitions_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneDownTransitionsItem,
        )
        from ..models.post_v1_troubleshooting_device_device_id_response_200_data_plane_session_slas_item import (
            PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem,
        )

        d = src_dict.copy()
        down_transitions = []
        _down_transitions = d.pop("downTransitions", UNSET)
        for down_transitions_item_data in _down_transitions or []:
            down_transitions_item = (
                PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneDownTransitionsItem.from_dict(
                    down_transitions_item_data
                )
            )

            down_transitions.append(down_transitions_item)

        session_slas = []
        _session_slas = d.pop("sessionSlas", UNSET)
        for session_slas_item_data in _session_slas or []:
            session_slas_item = PostV1TroubleshootingDeviceDeviceIdResponse200DataPlaneSessionSlasItem.from_dict(
                session_slas_item_data
            )

            session_slas.append(session_slas_item)

        status = d.pop("status", UNSET)

        post_v1_troubleshooting_device_device_id_response_200_data_plane = cls(
            down_transitions=down_transitions,
            session_slas=session_slas,
            status=status,
        )

        post_v1_troubleshooting_device_device_id_response_200_data_plane.additional_properties = d
        return post_v1_troubleshooting_device_device_id_response_200_data_plane

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
