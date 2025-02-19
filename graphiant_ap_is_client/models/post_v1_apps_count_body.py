from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_count_body_time_window import PostV1AppsCountBodyTimeWindow


T = TypeVar("T", bound="PostV1AppsCountBody")


@_attrs_define
class PostV1AppsCountBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        is_dia (Union[Unset, str]):  Example: TYPE_BOOL.
        time_window (Union[Unset, PostV1AppsCountBodyTimeWindow]):
    """

    device_id: Union[Unset, str] = UNSET
    is_dia: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1AppsCountBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        is_dia = self.is_dia

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if is_dia is not UNSET:
            field_dict["isDia"] = is_dia
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_count_body_time_window import PostV1AppsCountBodyTimeWindow

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        is_dia = d.pop("isDia", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1AppsCountBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1AppsCountBodyTimeWindow.from_dict(_time_window)

        post_v1_apps_count_body = cls(
            device_id=device_id,
            is_dia=is_dia,
            time_window=time_window,
        )

        post_v1_apps_count_body.additional_properties = d
        return post_v1_apps_count_body

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
