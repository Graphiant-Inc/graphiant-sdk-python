from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_v1_global_config_body_snmps_item_value_config import PatchV1GlobalConfigBodySnmpsItemValueConfig


T = TypeVar("T", bound="PatchV1GlobalConfigBodySnmpsItemValue")


@_attrs_define
class PatchV1GlobalConfigBodySnmpsItemValue:
    """
    Attributes:
        config (Union[Unset, PatchV1GlobalConfigBodySnmpsItemValueConfig]):
    """

    config: Union[Unset, "PatchV1GlobalConfigBodySnmpsItemValueConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.patch_v1_global_config_body_snmps_item_value_config import (
            PatchV1GlobalConfigBodySnmpsItemValueConfig,
        )

        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, PatchV1GlobalConfigBodySnmpsItemValueConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = PatchV1GlobalConfigBodySnmpsItemValueConfig.from_dict(_config)

        patch_v1_global_config_body_snmps_item_value = cls(
            config=config,
        )

        patch_v1_global_config_body_snmps_item_value.additional_properties = d
        return patch_v1_global_config_body_snmps_item_value

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
