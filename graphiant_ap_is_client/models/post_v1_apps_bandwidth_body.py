from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_apps_bandwidth_body_time_window import PostV1AppsBandwidthBodyTimeWindow


T = TypeVar("T", bound="PostV1AppsBandwidthBody")


@_attrs_define
class PostV1AppsBandwidthBody:
    """
    Attributes:
        app_id (Union[Unset, str]):  Example: TYPE_UINT32.
        device_id (Union[Unset, str]):  Example: TYPE_INT64.
        dl_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
        is_dia (Union[Unset, str]):  Example: TYPE_BOOL.
        sla_class (Union[Unset, str]):  Example: TYPE_ENUM.
        time_window (Union[Unset, PostV1AppsBandwidthBodyTimeWindow]):
        ul_circuit_name (Union[Unset, str]):  Example: TYPE_STRING.
    """

    app_id: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    dl_circuit_name: Union[Unset, str] = UNSET
    is_dia: Union[Unset, str] = UNSET
    sla_class: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV1AppsBandwidthBodyTimeWindow"] = UNSET
    ul_circuit_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        device_id = self.device_id

        dl_circuit_name = self.dl_circuit_name

        is_dia = self.is_dia

        sla_class = self.sla_class

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        ul_circuit_name = self.ul_circuit_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if dl_circuit_name is not UNSET:
            field_dict["dlCircuitName"] = dl_circuit_name
        if is_dia is not UNSET:
            field_dict["isDia"] = is_dia
        if sla_class is not UNSET:
            field_dict["slaClass"] = sla_class
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window
        if ul_circuit_name is not UNSET:
            field_dict["ulCircuitName"] = ul_circuit_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_apps_bandwidth_body_time_window import PostV1AppsBandwidthBodyTimeWindow

        d = src_dict.copy()
        app_id = d.pop("appId", UNSET)

        device_id = d.pop("deviceId", UNSET)

        dl_circuit_name = d.pop("dlCircuitName", UNSET)

        is_dia = d.pop("isDia", UNSET)

        sla_class = d.pop("slaClass", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV1AppsBandwidthBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV1AppsBandwidthBodyTimeWindow.from_dict(_time_window)

        ul_circuit_name = d.pop("ulCircuitName", UNSET)

        post_v1_apps_bandwidth_body = cls(
            app_id=app_id,
            device_id=device_id,
            dl_circuit_name=dl_circuit_name,
            is_dia=is_dia,
            sla_class=sla_class,
            time_window=time_window,
            ul_circuit_name=ul_circuit_name,
        )

        post_v1_apps_bandwidth_body.additional_properties = d
        return post_v1_apps_bandwidth_body

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
