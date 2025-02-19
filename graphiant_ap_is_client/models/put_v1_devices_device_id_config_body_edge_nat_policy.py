from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.put_v1_devices_device_id_config_body_edge_nat_policy_nat_rulesets_item import (
        PutV1DevicesDeviceIdConfigBodyEdgeNatPolicyNatRulesetsItem,
    )


T = TypeVar("T", bound="PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy")


@_attrs_define
class PutV1DevicesDeviceIdConfigBodyEdgeNatPolicy:
    """
    Attributes:
        nat_rulesets (Union[Unset, list['PutV1DevicesDeviceIdConfigBodyEdgeNatPolicyNatRulesetsItem']]):
    """

    nat_rulesets: Union[Unset, list["PutV1DevicesDeviceIdConfigBodyEdgeNatPolicyNatRulesetsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nat_rulesets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.nat_rulesets, Unset):
            nat_rulesets = []
            for nat_rulesets_item_data in self.nat_rulesets:
                nat_rulesets_item = nat_rulesets_item_data.to_dict()
                nat_rulesets.append(nat_rulesets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nat_rulesets is not UNSET:
            field_dict["natRulesets"] = nat_rulesets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.put_v1_devices_device_id_config_body_edge_nat_policy_nat_rulesets_item import (
            PutV1DevicesDeviceIdConfigBodyEdgeNatPolicyNatRulesetsItem,
        )

        d = src_dict.copy()
        nat_rulesets = []
        _nat_rulesets = d.pop("natRulesets", UNSET)
        for nat_rulesets_item_data in _nat_rulesets or []:
            nat_rulesets_item = PutV1DevicesDeviceIdConfigBodyEdgeNatPolicyNatRulesetsItem.from_dict(
                nat_rulesets_item_data
            )

            nat_rulesets.append(nat_rulesets_item)

        put_v1_devices_device_id_config_body_edge_nat_policy = cls(
            nat_rulesets=nat_rulesets,
        )

        put_v1_devices_device_id_config_body_edge_nat_policy.additional_properties = d
        return put_v1_devices_device_id_config_body_edge_nat_policy

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
