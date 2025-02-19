from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_syslog_servers_item_value_target import (
        PatchV1GlobalConfigBodySyslogServersItemValueTarget,
    )


T = TypeVar("T", bound="PatchV1GlobalConfigBodySyslogServersItemValue")


@_attrs_define
class PatchV1GlobalConfigBodySyslogServersItemValue:
    """
    Attributes:
        target (Union[Unset, PatchV1GlobalConfigBodySyslogServersItemValueTarget]):
    """

    target: Union[Unset, "PatchV1GlobalConfigBodySyslogServersItemValueTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_syslog_servers_item_value_target import (
            PatchV1GlobalConfigBodySyslogServersItemValueTarget,
        )

        d = src_dict.copy()
        _target = d.pop("target", UNSET)
        target: Union[Unset, PatchV1GlobalConfigBodySyslogServersItemValueTarget]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PatchV1GlobalConfigBodySyslogServersItemValueTarget.from_dict(_target)

        patch_v1_global_config_body_syslog_servers_item_value = cls(
            target=target,
        )

        patch_v1_global_config_body_syslog_servers_item_value.additional_properties = d
        return patch_v1_global_config_body_syslog_servers_item_value

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
