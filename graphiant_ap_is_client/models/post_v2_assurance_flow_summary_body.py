from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v2_assurance_flow_summary_body_time_window import PostV2AssuranceFlowSummaryBodyTimeWindow


T = TypeVar("T", bound="PostV2AssuranceFlowSummaryBody")


@_attrs_define
class PostV2AssuranceFlowSummaryBody:
    """
    Attributes:
        client_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_ip (Union[Unset, str]):  Example: TYPE_STRING.
        server_port (Union[Unset, str]):  Example: TYPE_INT32.
        time_window (Union[Unset, PostV2AssuranceFlowSummaryBodyTimeWindow]):
    """

    client_ip: Union[Unset, str] = UNSET
    server_ip: Union[Unset, str] = UNSET
    server_port: Union[Unset, str] = UNSET
    time_window: Union[Unset, "PostV2AssuranceFlowSummaryBodyTimeWindow"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_ip = self.client_ip

        server_ip = self.server_ip

        server_port = self.server_port

        time_window: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.time_window, Unset):
            time_window = self.time_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if time_window is not UNSET:
            field_dict["timeWindow"] = time_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v2_assurance_flow_summary_body_time_window import PostV2AssuranceFlowSummaryBodyTimeWindow

        d = src_dict.copy()
        client_ip = d.pop("clientIp", UNSET)

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        _time_window = d.pop("timeWindow", UNSET)
        time_window: Union[Unset, PostV2AssuranceFlowSummaryBodyTimeWindow]
        if isinstance(_time_window, Unset):
            time_window = UNSET
        else:
            time_window = PostV2AssuranceFlowSummaryBodyTimeWindow.from_dict(_time_window)

        post_v2_assurance_flow_summary_body = cls(
            client_ip=client_ip,
            server_ip=server_ip,
            server_port=server_port,
            time_window=time_window,
        )

        post_v2_assurance_flow_summary_body.additional_properties = d
        return post_v2_assurance_flow_summary_body

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
