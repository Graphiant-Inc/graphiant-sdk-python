from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_v1_devices_bringup_token_body_valid_till_ts import PostV1DevicesBringupTokenBodyValidTillTs


T = TypeVar("T", bound="PostV1DevicesBringupTokenBody")


@_attrs_define
class PostV1DevicesBringupTokenBody:
    """
    Attributes:
        valid_till_ts (Union[Unset, PostV1DevicesBringupTokenBodyValidTillTs]):
    """

    valid_till_ts: Union[Unset, "PostV1DevicesBringupTokenBodyValidTillTs"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid_till_ts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.valid_till_ts, Unset):
            valid_till_ts = self.valid_till_ts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid_till_ts is not UNSET:
            field_dict["validTillTs"] = valid_till_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.post_v1_devices_bringup_token_body_valid_till_ts import PostV1DevicesBringupTokenBodyValidTillTs

        d = src_dict.copy()
        _valid_till_ts = d.pop("validTillTs", UNSET)
        valid_till_ts: Union[Unset, PostV1DevicesBringupTokenBodyValidTillTs]
        if isinstance(_valid_till_ts, Unset):
            valid_till_ts = UNSET
        else:
            valid_till_ts = PostV1DevicesBringupTokenBodyValidTillTs.from_dict(_valid_till_ts)

        post_v1_devices_bringup_token_body = cls(
            valid_till_ts=valid_till_ts,
        )

        post_v1_devices_bringup_token_body.additional_properties = d
        return post_v1_devices_bringup_token_body

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
