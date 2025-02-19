from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_talkers_device_device_id_top_body_time_window import (
        PostV1TalkersDeviceDeviceIdTopBodyTimeWindow,
    )


T = TypeVar("T", bound="PostV1TalkersDeviceDeviceIdTopBody")


@_attrs_define
class PostV1TalkersDeviceDeviceIdTopBody:
    """
    Attributes:
        num_clients (Union[Unset, str]):  Example: 10.
        time_window (Union[Unset, PostV1TalkersDeviceDeviceIdTopBodyTimeWindow]):
    """

    num_clients: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1TalkersDeviceDeviceIdTopBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_clients = self.num_clients

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_clients is not UNSET:
            field_dict["numClients"] = num_clients
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_talkers_device_device_id_top_body_time_window import (
            PostV1TalkersDeviceDeviceIdTopBodyTimeWindow,
        )

        d = src_dict.copy()
        num_clients = d.pop("numClients", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1TalkersDeviceDeviceIdTopBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1TalkersDeviceDeviceIdTopBodyTimeWindow.from_dict(_time_window)

        post_v1_talkers_device_device_id_top_body = cls(
            num_clients=num_clients,
            time_window=time_window,
        )

        post_v1_talkers_device_device_id_top_body.additional_properties = d
        return post_v1_talkers_device_device_id_top_body

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
