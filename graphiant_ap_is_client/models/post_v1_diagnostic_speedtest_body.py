from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_diagnostic_speedtest_body_params import PostV1DiagnosticSpeedtestBodyParams


T = TypeVar("T", bound="PostV1DiagnosticSpeedtestBody")


@_attrs_define
class PostV1DiagnosticSpeedtestBody:
    """
    Attributes:
        device_id (Union[Unset, str]):  Example: 30000000555.
        params (Union[Unset, PostV1DiagnosticSpeedtestBodyParams]):
    """

    device_id: Union[Unset, str] = UNSET
    params: Union[Unset, "PostV1DiagnosticSpeedtestBodyParams"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_diagnostic_speedtest_body_params import PostV1DiagnosticSpeedtestBodyParams

        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, PostV1DiagnosticSpeedtestBodyParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = PostV1DiagnosticSpeedtestBodyParams.from_dict(_params)

        post_v1_diagnostic_speedtest_body = cls(
            device_id=device_id,
            params=params,
        )

        post_v1_diagnostic_speedtest_body.additional_properties = d
        return post_v1_diagnostic_speedtest_body

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
