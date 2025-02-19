from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV2AckCreateupdateBody")


@_attrs_define
class PostV2AckCreateupdateBody:
    """
    Attributes:
        alert_id_list (Union[Unset, list[str]]):  Example: ['TYPE_STRING'].
        reason (Union[Unset, str]):  Example: TYPE_STRING.
    """

    alert_id_list: Union[Unset, list[str]] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_id_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_id_list, Unset):
            alert_id_list = self.alert_id_list

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_id_list is not UNSET:
            field_dict["alertIdList"] = alert_id_list
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id_list = cast(list[str], d.pop("alertIdList", UNSET))

        reason = d.pop("reason", UNSET)

        post_v2_ack_createupdate_body = cls(
            alert_id_list=alert_id_list,
            reason=reason,
        )

        post_v2_ack_createupdate_body.additional_properties = d
        return post_v2_ack_createupdate_body

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
