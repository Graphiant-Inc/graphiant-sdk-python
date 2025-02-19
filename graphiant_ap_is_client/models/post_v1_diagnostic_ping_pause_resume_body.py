from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_ping_pause_resume_body_params import PostV1DiagnosticPingPauseResumeBodyParams


T = TypeVar("T", bound="PostV1DiagnosticPingPauseResumeBody")


@_attrs_define
class PostV1DiagnosticPingPauseResumeBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: 10000000.
        params (Union[Unset, PostV1DiagnosticPingPauseResumeBodyParams]):
        token (Union[Unset, str]):  Example: TYPE_STRING.
        transport_type (Union[Unset, str]):  Example: TYPE_ENUM.
    """

    device_id: Union[Unset, str] = UNSET
    params: Union[Unset, "PostV1DiagnosticPingPauseResumeBodyParams"] = UNSET
    token: Union[Unset, str] = UNSET
    transport_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        token = self.token

        transport_type = self.transport_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if params is not UNSET:
            field_dict["params"] = params
        if token is not UNSET:
            field_dict["token"] = token
        if transport_type is not UNSET:
            field_dict["transportType"] = transport_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_ping_pause_resume_body_params import PostV1DiagnosticPingPauseResumeBodyParams

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, PostV1DiagnosticPingPauseResumeBodyParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = PostV1DiagnosticPingPauseResumeBodyParams.from_dict(_params)

        token = d.pop("token", UNSET)

        transport_type = d.pop("transportType", UNSET)

        post_v1_diagnostic_ping_pause_resume_body = cls(
            device_id=device_id,
            params=params,
            token=token,
            transport_type=transport_type,
        )

        post_v1_diagnostic_ping_pause_resume_body.additional_properties = d
        return post_v1_diagnostic_ping_pause_resume_body

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
