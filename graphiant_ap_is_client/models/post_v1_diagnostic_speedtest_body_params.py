from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_speedtest_body_params_target import PostV1DiagnosticSpeedtestBodyParamsTarget


T = TypeVar("T", bound="PostV1DiagnosticSpeedtestBodyParams")


@_attrs_define
class PostV1DiagnosticSpeedtestBodyParams:
    """
    Attributes:
        provider (Union[Unset, str]):  Example: ookla.
        server_id (Union[Unset, str]):  Example: 234123.
        target (Union[Unset, PostV1DiagnosticSpeedtestBodyParamsTarget]):
        token (Union[Unset, str]):  Example: TYPE_STRING.
    """

    provider: Union[Unset, str] = UNSET
    server_id: Union[Unset, str] = UNSET
    target: Union[Unset, "PostV1DiagnosticSpeedtestBodyParamsTarget"] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        server_id = self.server_id

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if target is not UNSET:
            field_dict["target"] = target
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_speedtest_body_params_target import PostV1DiagnosticSpeedtestBodyParamsTarget

        d = src_dict.copy()
        provider = d.pop("provider", UNSET)

        server_id = d.pop("serverId", UNSET)

        _target = d.pop("target", UNSET)
        target: Union[Unset, PostV1DiagnosticSpeedtestBodyParamsTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PostV1DiagnosticSpeedtestBodyParamsTarget.from_dict(_target)

        token = d.pop("token", UNSET)

        post_v1_diagnostic_speedtest_body_params = cls(
            provider=provider,
            server_id=server_id,
            target=target,
            token=token,
        )

        post_v1_diagnostic_speedtest_body_params.additional_properties = d
        return post_v1_diagnostic_speedtest_body_params

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
